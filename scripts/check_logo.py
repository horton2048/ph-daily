#!/usr/bin/env python3
"""检查 PNG 中 logo 区域是否为空白"""
from PIL import Image
import sys

def check_logo_area(png_path):
    """检查 logo 区域（左上角 hero 部分的 logo 位置）"""
    img = Image.open(png_path).convert('RGBA')
    # logo 在 1500x2000 图中的位置（scale 4x 后）
    # 原始位置大约是 20px, 30px 附近，28x28 大小
    # 4x 后是 80px, 120px 附近，112x112 大小
    logo_region = img.crop((80, 100, 192, 212))

    # 检查是否全是单一颜色（表示 logo 没加载）
    colors = logo_region.getcolors(maxcolors=1000000)
    if colors and len(colors) < 5:
        print(f"✗ {png_path.name}: logo 区域颜色单一 ({len(colors)} 种颜色)")
        return False
    else:
        print(f"✓ {png_path.name}: logo 区域有内容 ({len(colors) if colors else '很多'} 种颜色)")
        return True

if __name__ == "__main__":
    from pathlib import Path

    png_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    for png in sorted(png_dir.glob("*.png")):
        check_logo_area(png)
