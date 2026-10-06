#!/usr/bin/env python3
"""
修复 2026-08-05 榜单 #9 Capacity Desktop 和 #10 X Money 的信息图 logo
"""
import os
import requests
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

# 配置
CONTEXT_DIR = Path.home() / "Projects/ph-daily/context"
XHS_DIR = Path.home() / "Projects/ph-daily/xhs/2026-08-05"
DATE = "2026-08-05"

# 信息图尺寸
WIDTH = 1500
HEIGHT = 2000
BG_COLOR = "#FFFFFF"
PRIMARY_COLOR = "#FF6154"  # PH 橙色
TEXT_COLOR = "#333333"

# 需要修复的产品
PRODUCTS = [
    (9, "capacity-desktop"),
    (10, "x-money-2")
]

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
        'logo_url': ''
    }

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

    # logo
    match = re.search(r'\| logo \| ([^\n]+) \|', content)
    if match:
        info['logo_url'] = match.group(1).strip()

    return info

def create_infographic(rank, product_info, logo_img):
    """创建信息图"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # 加载字体
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

    # 英文 tagline（换行处理）
    y_offset += 100
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

    for line in lines[:3]:
        draw.text((80, y_offset), line, fill="#666666", font=font_small)
        y_offset += 50

    # 中文 tagline（换行处理）
    y_offset += 80
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
    print(f"🎨 修复 {DATE} 的 #9 和 #10 信息图 logo...")
    print()

    XHS_DIR.mkdir(parents=True, exist_ok=True)

    for rank, product_slug in PRODUCTS:
        print(f"[#{rank}] {product_slug}")

        # 提取产品信息
        info = extract_info_from_context(product_slug)
        if not info:
            print(f"  ❌ 无法提取产品信息")
            continue

        print(f"  产品名: {info['product']}")
        print(f"  Logo URL: {info['logo_url'][:60]}...")

        # 下载 logo
        logo_img = None
        if info['logo_url'] and info['logo_url'].startswith('http'):
            print(f"  📥 下载 logo...")
            logo_img = download_logo(info['logo_url'])

        if not logo_img:
            print(f"  ❌ 无法获取 logo")
            continue

        # 生成信息图
        print(f"  🎨 生成信息图...")
        img = create_infographic(rank, info, logo_img)

        # 保存（覆盖现有文件）
        output_path = XHS_DIR / f"{rank:02d}-{product_slug}.png"
        img.save(output_path, 'PNG', optimize=True)
        print(f"  ✅ 已保存: {output_path}")
        print()

    print("="*60)
    print(f"✅ 完成！已更新 {len(PRODUCTS)} 个信息图")

if __name__ == "__main__":
    main()
