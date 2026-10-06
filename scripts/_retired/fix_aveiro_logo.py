#!/usr/bin/env python3
"""
修复 Aveiro 的 logo（使用 imgix 转换）
"""
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
PRIMARY_COLOR = "#FF6154"
TEXT_COLOR = "#333333"

def download_logo(logo_url):
    """下载 logo 图片（支持 imgix SVG 转换）"""
    try:
        # 如果是 SVG，使用 imgix 参数转换为 PNG
        if logo_url.endswith('.svg'):
            logo_url = logo_url + '?fm=png&w=200'

        response = requests.get(logo_url, timeout=15)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        return img.convert('RGBA')
    except Exception as e:
        print(f"      ⚠️  下载失败: {e}")
        return None

def extract_info_from_context(product_slug):
    """从 context 文件提取产品信息"""
    context_file = CONTEXT_DIR / f"{DATE}-{product_slug}.md"
    content = context_file.read_text(encoding='utf-8')

    info = {'product': '', 'tagline_en': '', 'tagline_zh': ''}

    import re
    match = re.search(r'\| 产品名 \| ([^\n]+) \|', content)
    if match:
        info['product'] = match.group(1).strip()

    match = re.search(r'\| 英文 tagline \| ([^\n]+) \|', content)
    if match:
        info['tagline_en'] = match.group(1).strip()

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
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

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
    draw.text((80, y_offset), f"#{rank}", fill=PRIMARY_COLOR, font=font_large)

    if logo_img:
        logo_size = 120
        logo_img = logo_img.copy()
        logo_img.thumbnail((logo_size, logo_size), Image.Resampling.LANCZOS)
        logo_x = WIDTH - logo_size - 80
        logo_y = y_offset
        img.paste(logo_img, (logo_x, logo_y), logo_img if logo_img.mode == 'RGBA' else None)

    y_offset += 180
    draw.text((80, y_offset), product_info['product'], fill=TEXT_COLOR, font=font_large)

    y_offset += 100
    lines = wrap_text(draw, product_info['tagline_en'], font_small, WIDTH - 160)
    for line in lines[:3]:
        draw.text((80, y_offset), line, fill="#666666", font=font_small)
        y_offset += 50

    y_offset += 80
    zh_lines = wrap_text_cjk(draw, product_info['tagline_zh'], font_medium, WIDTH - 160)
    for line in zh_lines[:3]:
        draw.text((80, y_offset), line, fill=TEXT_COLOR, font=font_medium)
        y_offset += 60

    y_offset = HEIGHT - 200
    draw.text((80, y_offset), f"Product Hunt · {DATE}", fill="#999999", font=font_tiny)
    y_offset += 60
    draw.text((80, y_offset), "#ProductHunt #AI工具 #产品观察", fill="#999999", font=font_tiny)

    return img

def main():
    print(f"🔧 修复 Aveiro 的 SVG logo...\n")

    rank = 9
    product_slug = "aveiro"
    logo_url = "https://ph-files.imgix.net/0b9f6d6b-4980-42fc-af75-acb55e53d825.svg"

    print(f"[{rank}/10] {product_slug}")

    info = extract_info_from_context(product_slug)

    print(f"    📥 下载 logo（使用 imgix 转换）...")
    logo_img = download_logo(logo_url)

    if not logo_img:
        print(f"    ❌ logo 下载失败")
    else:
        print(f"    ✅ logo 下载成功")

    print(f"    🎨 生成信息图...")
    img = create_infographic(rank, info, logo_img)

    output_path = XHS_DIR / f"{rank:02d}-{product_slug}.png"
    img.save(output_path, 'PNG', optimize=True)
    print(f"    ✅ 已保存: {output_path.name}\n")

    print("="*60)
    if logo_img:
        print(f"✅ Aveiro logo 修复成功！")
    else:
        print(f"❌ Aveiro logo 仍然缺失")

if __name__ == "__main__":
    main()
