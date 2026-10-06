#!/usr/bin/env python3
"""
重新生成 2026-08-06 的小红书信息图（修复 logo 缺失问题）
"""
import os
import json
import requests
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

# 配置
CONTEXT_DIR = Path.home() / "Projects/ph-daily/context"
XHS_DIR = Path.home() / "Projects/ph-daily/xhs/2026-08-06"
DATE = "2026-08-06"

# 信息图尺寸（根据现有图片）
WIDTH = 1500
HEIGHT = 2000
BG_COLOR = "#FFFFFF"
PRIMARY_COLOR = "#FF6154"  # PH 橙色
TEXT_COLOR = "#333333"
LIGHT_GRAY = "#F5F5F5"

# 产品列表（排名顺序）
PRODUCTS = [
    "cloudflare-os",
    "muse-code",
    "annotate",
    "ai-spend-console-by-rippling",
    "brandfetch-mcp",
    "shieldstral",
    "website-to-markdown-api",
    "superlog-responder",
    "aveiro",
    "ododok"
]

def fetch_logo_from_ph(ph_url):
    """从 PH 产品页抓取 logo"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        response = requests.get(ph_url, headers=headers, timeout=10)
        response.raise_for_status()

        # 简单的正则提取（实际应该用更可靠的方法，比如 BeautifulSoup）
        import re
        # 查找 og:image 或产品 logo
        match = re.search(r'<meta property="og:image" content="([^"]+)"', response.text)
        if match:
            return match.group(1)

        # 查找 imgix logo
        match = re.search(r'(https://ph-files\.imgix\.net/[^"\'>\s]+\.(?:png|jpg|jpeg))', response.text)
        if match:
            return match.group(1)

    except Exception as e:
        print(f"  ⚠️  无法从 {ph_url} 抓取 logo: {e}")

    return None

def download_logo(logo_url):
    """下载 logo 图片"""
    try:
        response = requests.get(logo_url, timeout=10)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        return img.convert('RGBA')
    except Exception as e:
        print(f"  ⚠️  下载 logo 失败: {e}")
        return None

def extract_info_from_context(product_slug):
    """从 context 文件提取产品信息"""
    context_file = CONTEXT_DIR / f"{DATE}-{product_slug}.md"

    if not context_file.exists():
        print(f"  ⚠️  context 文件不存在: {context_file}")
        return None

    content = context_file.read_text(encoding='utf-8')

    info = {
        'product': '',
        'tagline_en': '',
        'tagline_zh': '',
        'ph_url': '',
        'logo_url': ''
    }

    # 提取基本信息
    import re

    # 产品名
    match = re.search(r'\| 产品名 \| ([^\n]+) \|', content)
    if match:
        info['product'] = match.group(1).strip()

    # 英文 tagline
    match = re.search(r'\| 英文 tagline \| ([^\n]+) \|', content)
    if match:
        info['tagline_en'] = match.group(1).strip()

    # 中文 tagline
    match = re.search(r'\| 中文 tagline \| ([^\n]+) \|', content)
    if match:
        info['tagline_zh'] = match.group(1).strip()

    # PH 页
    match = re.search(r'\| PH 页 \| ([^\n]+) \|', content)
    if match:
        info['ph_url'] = match.group(1).strip()

    # logo（如果有）
    match = re.search(r'\| logo \| ([^\n]+) \|', content)
    if match:
        info['logo_url'] = match.group(1).strip()

    return info

def create_infographic(rank, product_info, logo_img):
    """创建信息图"""
    # 创建画布
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # 尝试加载字体（如果失败使用默认字体）
    try:
        font_large = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 60)
        font_medium = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 40)
        font_small = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 32)
        font_tiny = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 28)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
        font_tiny = ImageFont.load_default()

    # 顶部：排名和 logo
    y_offset = 80

    # 排名标签
    draw.text((80, y_offset), f"#{rank}", fill=PRIMARY_COLOR, font=font_large)

    # Logo（右上角）
    if logo_img:
        logo_size = 120
        logo_img = logo_img.copy()
        logo_img.thumbnail((logo_size, logo_size), Image.Resampling.LANCZOS)
        logo_x = WIDTH - logo_size - 80
        logo_y = y_offset
        img.paste(logo_img, (logo_x, logo_y), logo_img if logo_img.mode == 'RGBA' else None)

    # 产品名
    y_offset += 180
    draw.text((80, y_offset), product_info['product'], fill=TEXT_COLOR, font=font_large)

    # 英文 tagline
    y_offset += 100
    # 文本换行
    tagline_en = product_info['tagline_en']
    max_width = WIDTH - 160
    words = tagline_en.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + " " + word if current_line else word
        bbox = draw.textbbox((0, 0), test_line, font=font_small)
        if bbox[2] - bbox[0] <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)

    for line in lines[:3]:  # 最多3行
        draw.text((80, y_offset), line, fill="#666666", font=font_small)
        y_offset += 50

    # 中文 tagline
    y_offset += 80
    # 中文也需要换行
    tagline_zh = product_info['tagline_zh']
    zh_lines = []
    current_line = ""

    for char in tagline_zh:
        test_line = current_line + char
        bbox = draw.textbbox((0, 0), test_line, font=font_medium)
        if bbox[2] - bbox[0] <= max_width:
            current_line = test_line
        else:
            if current_line:
                zh_lines.append(current_line)
            current_line = char
    if current_line:
        zh_lines.append(current_line)

    for line in zh_lines[:3]:
        draw.text((80, y_offset), line, fill=TEXT_COLOR, font=font_medium)
        y_offset += 60

    # 底部：日期和标签
    y_offset = HEIGHT - 200
    draw.text((80, y_offset), f"Product Hunt · {DATE}", fill="#999999", font=font_tiny)

    y_offset += 60
    draw.text((80, y_offset), "#ProductHunt #AI工具 #产品观察", fill="#999999", font=font_tiny)

    return img

def main():
    """主函数"""
    print(f"🎨 开始重新生成 {DATE} 的信息图...")
    print()

    XHS_DIR.mkdir(parents=True, exist_ok=True)

    fixed_count = 0
    failed_count = 0

    for rank, product_slug in enumerate(PRODUCTS, 1):
        print(f"[{rank}/10] {product_slug}")

        # 提取产品信息
        info = extract_info_from_context(product_slug)
        if not info:
            print(f"  ❌ 无法提取产品信息")
            failed_count += 1
            continue

        # 获取 logo
        logo_img = None

        # 1. 先尝试从 context 中已有的 logo URL
        if info['logo_url'] and info['logo_url'].startswith('http'):
            print(f"  📥 从 context 下载 logo...")
            logo_img = download_logo(info['logo_url'])

        # 2. 如果没有，从 PH 页面抓取
        if not logo_img and info['ph_url']:
            print(f"  🔍 从 PH 页面抓取 logo...")
            logo_url = fetch_logo_from_ph(info['ph_url'])
            if logo_url:
                print(f"  📥 下载 logo: {logo_url[:60]}...")
                logo_img = download_logo(logo_url)

        if not logo_img:
            print(f"  ⚠️  无法获取 logo，将生成无 logo 的信息图")

        # 生成信息图
        print(f"  🎨 生成信息图...")
        img = create_infographic(rank, info, logo_img)

        # 保存
        output_path = XHS_DIR / f"{rank:02d}-{product_slug}.png"
        img.save(output_path, 'PNG', optimize=True)
        print(f"  ✅ 已保存: {output_path.name}")

        if logo_img:
            fixed_count += 1
        else:
            failed_count += 1

        print()

    print("="*60)
    print(f"✅ 完成！共处理 {len(PRODUCTS)} 个产品")
    print(f"   - 成功修复 logo: {fixed_count} 个")
    print(f"   - logo 缺失: {failed_count} 个")
    print(f"   - 输出目录: {XHS_DIR}")

if __name__ == "__main__":
    main()
