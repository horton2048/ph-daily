#!/usr/bin/env python3
"""
渲染小红书信息卡片 HTML → PNG
确保 logo 等网络资源完全加载后再截图
"""
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

def render_html_to_png(html_path: Path, png_path: Path, wait_for_images: bool = True):
    """使用 Playwright 渲染 HTML 为 PNG"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(
            viewport={'width': 375, 'height': 500},
            device_scale_factor=4
        )

        # 加载 HTML
        page.goto(f"file://{html_path.absolute()}")

        # 等待图片加载
        if wait_for_images:
            page.wait_for_load_state("networkidle", timeout=10000)
            time.sleep(0.5)  # 额外缓冲

        # 截图
        page.screenshot(path=str(png_path), full_page=True)
        browser.close()
        print(f"✓ {html_path.name} → {png_path.name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: render_cards.py <html_dir>")
        sys.exit(1)

    html_dir = Path(sys.argv[1])
    if not html_dir.exists():
        print(f"Error: {html_dir} not found")
        sys.exit(1)

    # 渲染所有 HTML
    for html_file in sorted(html_dir.glob("*.html")):
        png_file = html_file.parent.parent / f"{html_file.stem}.png"
        try:
            render_html_to_png(html_file, png_file)
        except Exception as e:
            print(f"✗ {html_file.name}: {e}")
