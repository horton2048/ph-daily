#!/usr/bin/env python3
"""
修复剩余 3 个产品的 logo（Shieldstral, Aveiro, Ododok）
"""
import requests
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import ssl
import urllib3

# 禁用 SSL 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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

# 需要修复的产品
PRODUCTS_TO_FIX = [
    (6, "shieldstral", "https://ph-files.imgix.net/296959f2-f1f5-408c-803c-58b33e049208.png"),
    (9, "aveiro", "https://ph-files.imgix.net/0b9f6d6b-4980-42fc-af75-acb55e53d825.svg"),
    (10, "ododok", "https://ph-files.imgix.net/0e15f596-110a-4c86-9c64-51b8faa72ec2.png"),
]

def download_logo(logo_url, verify_ssl=True):
    """下载 logo 图片"""
    try:
        response = requests.get(logo_url, timeout=15, verify=verify_ssl)
        response.raise_for_status()

        # 处理 SVG
        if logo_url.endswith('.svg'):
            try:
                import cairosvg
                png_data = cairosvg.svg2png(bytestring=response.content, output_width=200)
                img = Image.open(BytesIO(png_data))
                return img.convert('RGBA')
            except ImportError:
                print(f"      ⚠️  需要安装 cairosvg 来处理 SVG")
                # 尝试直接获取 PNG 版本
                png_url = logo_url.replace('.svg', '.png')
                try:
                    response = requests.get(png_url, timeout=15, verify=verify_ssl)
                    response.raise_for_status()
                    img = Image.open(BytesIO(response.content))
                    return img.convert('RGBA')
                except:
                    return None

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
    print(f"🔧 修复剩余 3 个产品的 logo...\n")

    fixed = []
    failed = []

    for rank, product_slug, logo_url in PRODUCTS_TO_FIX:
        print(f"[{rank}/10] {product_slug}")

        info = extract_info_from_context(product_slug)

        # 先尝试正常下载
        print(f"    📥 下载 logo...")
        logo_img = download_logo(logo_url, verify_ssl=True)

        # 如果失败，尝试不验证 SSL
        if not logo_img:
            print(f"    🔄 重试（跳过 SSL 验证）...")
            logo_img = download_logo(logo_url, verify_ssl=False)

        if not logo_img:
            print(f"    ❌ logo 下载失败")
            failed.append(product_slug)
        else:
            print(f"    ✅ logo 下载成功")
            fixed.append(product_slug)

        print(f"    🎨 生成信息图...")
        img = create_infographic(rank, info, logo_img)

        output_path = XHS_DIR / f"{rank:02d}-{product_slug}.png"
        img.save(output_path, 'PNG', optimize=True)
        print(f"    ✅ 已保存: {output_path.name}\n")

    print("="*60)
    print(f"✅ 修复完成！")
    print(f"   - 成功添加 logo: {len(fixed)} 个 - {', '.join(fixed)}")
    print(f"   - 仍然缺失: {len(failed)} 个 - {', '.join(failed)}")

if __name__ == "__main__":
    main()
