#!/usr/bin/env python3
"""
重新生成 2026-08-06 的小红书信息图（使用已获取的 logo URL）
"""
import os
import requests
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

# 配置
CONTEXT_DIR = Path.home() / "Projects/ph-daily/context"
XHS_DIR = Path.home() / "Projects/ph-daily/xhs/2026-08-06"
DATE = "2026-08-06"

# 信息图尺寸
WIDTH = 1500
HEIGHT = 2000
BG_COLOR = "#FFFFFF"
PRIMARY_COLOR = "#FF6154"  # PH 橙色
TEXT_COLOR = "#333333"
LIGHT_GRAY = "#F5F5F5"

# 产品列表和对应的 logo URL（从 WebFetch 获取）
PRODUCTS = [
    ("cloudflare-os", "https://ph-files.imgix.net/edcb3719-f3b7-49e8-9676-27631af01cb9.png"),
    ("muse-code", "https://ph-files.imgix.net/d03e4bed-f4c2-4dc2-b8fa-8b031eed6fd6.png"),
    ("annotate", "https://ph-files.imgix.net/e75e84d4-a8a6-4678-9315-41e3722bc803.png"),
    ("ai-spend-console-by-rippling", "https://ph-files.imgix.net/83d32504-5be7-498a-90c5-a0d2720149d0.png"),
    ("brandfetch-mcp", "https://ph-files.imgix.net/155640fe-c6ec-473b-b0e0-f9f035874e4f.png"),
    ("shieldstral", "https://ph-files.imgix.net/296959f2-f1f5-408c-803c-58b33e049208.png"),
    ("website-to-markdown-api", "https://ph-files.imgix.net/4e8c2ab3-baf7-485a-b79d-ecad0be8c8fd.png"),
    ("superlog-responder", "https://ph-files.imgix.net/f5e16691-e739-48ba-9494-535f6a7ac36c.png"),
    ("aveiro", "https://ph-files.imgix.net/0b9f6d6b-4980-42fc-af75-acb55e53d825.svg"),
    ("ododok", "https://ph-files.imgix.net/0e15f596-110a-4c86-9c64-51b8faa72ec2.png"),
]

def download_logo(logo_url):
    """下载 logo 图片"""
    try:
        response = requests.get(logo_url, timeout=10)
        response.raise_for_status()

        # 处理 SVG（转换为 PNG）
        if logo_url.endswith('.svg'):
            # SVG 需要特殊处理，这里简单跳过
            print(f"    ⚠️  SVG logo 需要特殊处理，跳过")
            return None

        img = Image.open(BytesIO(response.content))
        return img.convert('RGBA')
    except Exception as e:
        print(f"    ⚠️  下载 logo 失败: {e}")
        return None

def extract_info_from_context(product_slug):
    """从 context 文件提取产品信息"""
    context_file = CONTEXT_DIR / f"{DATE}-{product_slug}.md"

    if not context_file.exists():
        print(f"    ⚠️  context 文件不存在: {context_file}")
        return None

    content = context_file.read_text(encoding='utf-8')

    info = {
        'product': '',
        'tagline_en': '',
        'tagline_zh': '',
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

    return info

def wrap_text(draw, text, font, max_width):
    """文本换行"""
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + " " + word if current_line else word
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)

    return lines

def wrap_text_cjk(draw, text, font, max_width):
    """中文文本换行"""
    lines = []
    current_line = ""

    for char in text:
        test_line = current_line + char
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = char
    if current_line:
        lines.append(current_line)

    return lines

def create_infographic(rank, product_info, logo_img):
    """创建信息图"""
    # 创建画布
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # 尝试加载字体
    try:
        font_large = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 60)
        font_medium = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 40)
        font_small = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 32)
        font_tiny = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 28)
    except:
        print(f"    ⚠️  无法加载字体，使用默认字体")
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

        # 如果 logo 有透明通道，使用它；否则直接粘贴
        if logo_img.mode == 'RGBA':
            img.paste(logo_img, (logo_x, logo_y), logo_img)
        else:
            img.paste(logo_img, (logo_x, logo_y))

    # 产品名
    y_offset += 180
    draw.text((80, y_offset), product_info['product'], fill=TEXT_COLOR, font=font_large)

    # 英文 tagline
    y_offset += 100
    tagline_en = product_info['tagline_en']
    max_width = WIDTH - 160
    lines = wrap_text(draw, tagline_en, font_small, max_width)

    for line in lines[:3]:  # 最多3行
        draw.text((80, y_offset), line, fill="#666666", font=font_small)
        y_offset += 50

    # 中文 tagline
    y_offset += 80
    tagline_zh = product_info['tagline_zh']
    zh_lines = wrap_text_cjk(draw, tagline_zh, font_medium, max_width)

    for line in zh_lines[:3]:  # 最多3行
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
    print(f"🎨 重新生成 {DATE} 的信息图（带 logo）...")
    print()

    XHS_DIR.mkdir(parents=True, exist_ok=True)

    fixed_count = 0
    failed_count = 0

    for rank, (product_slug, logo_url) in enumerate(PRODUCTS, 1):
        print(f"[{rank}/10] {product_slug}")

        # 提取产品信息
        info = extract_info_from_context(product_slug)
        if not info:
            print(f"    ❌ 无法提取产品信息")
            failed_count += 1
            continue

        # 下载 logo
        print(f"    📥 下载 logo...")
        logo_img = download_logo(logo_url)

        if not logo_img:
            print(f"    ⚠️  logo 下载失败，将生成无 logo 的信息图")
            failed_count += 1
        else:
            fixed_count += 1

        # 生成信息图
        print(f"    🎨 生成信息图...")
        img = create_infographic(rank, info, logo_img)

        # 保存
        output_path = XHS_DIR / f"{rank:02d}-{product_slug}.png"
        img.save(output_path, 'PNG', optimize=True)
        print(f"    ✅ 已保存: {output_path.name}")
        print()

    print("="*60)
    print(f"✅ 完成！共处理 {len(PRODUCTS)} 个产品")
    print(f"   - 成功修复 logo: {fixed_count} 个")
    print(f"   - logo 缺失: {failed_count} 个")
    print(f"   - 输出目录: {XHS_DIR}")

if __name__ == "__main__":
    main()
