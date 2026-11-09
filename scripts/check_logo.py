#!/usr/bin/env python3
"""检查 PNG 中 logo 区域是否为空白；并列出每张卡 logo 来源（render_xhs.py 写的 .tmp/logos/sources.json）

来源: official = PH 官方 logo（Post.thumbnail）；manual = data.json 人工指定；
      site = 官网品牌标识兜底；letter = 色块首字母兜底。
"""
from PIL import Image
import json
import sys

_SOURCE_ZH = {"official": "PH 官方", "manual": "人工指定", "site": "官网兜底", "letter": "首字母兜底"}


def load_sources(png_dir):
    path = png_dir / ".tmp" / "logos" / "sources.json"
    try:
        return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    except Exception:
        return {}


def source_label(png_path, sources):
    """01-some-slug.png -> sources['some-slug']"""
    slug = png_path.stem.split("-", 1)[-1]
    for suffix in ("-mono", "-cal"):
        slug = slug.removesuffix(suffix)
    rec = sources.get(slug)
    if not rec:
        return ""
    extra = f"；未用官方: {'; '.join(rec['notes'])}" if rec.get("notes") and rec["source"] != "official" else ""
    return f"  [{_SOURCE_ZH.get(rec['source'], rec['source'])}] {rec.get('url') or ''}{extra}"

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
    sources = load_sources(png_dir)
    for png in sorted(png_dir.glob("*.png")):
        check_logo_area(png)
        label = source_label(png, sources)
        if label:
            print(label)
