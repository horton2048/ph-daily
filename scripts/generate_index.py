#!/usr/bin/env python3
"""
Context 知识库索引生成器

读取 context/*.md 档案的 frontmatter，生成：
- INDEX.md（主索引）
- by-category/*.md（品类索引）
- by-tech/*.md（技术索引）
- by-business/*.md（商业模式索引）
- timeline/YYYY-MM.md（月度时间轴）
"""

import os
import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime
import yaml

# 配置
CONTEXT_DIR = Path.home() / "Projects/ph-daily/context"
INDEX_FILE = CONTEXT_DIR / "INDEX.md"
CATEGORY_DIR = CONTEXT_DIR / "by-category"
TECH_DIR = CONTEXT_DIR / "by-tech"
BUSINESS_DIR = CONTEXT_DIR / "by-business"
TIMELINE_DIR = CONTEXT_DIR / "timeline"


def extract_frontmatter(content):
    """提取 frontmatter（YAML）"""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None


def parse_context_file(filepath):
    """解析单个 context 档案"""
    try:
        content = filepath.read_text(encoding='utf-8')
        meta = extract_frontmatter(content)
        if not meta:
            return None

        # 补充文件名和相对路径
        meta['filename'] = filepath.name
        meta['relpath'] = filepath.relative_to(CONTEXT_DIR)

        return meta
    except Exception as e:
        print(f"⚠️  解析失败: {filepath.name} - {e}")
        return None


def load_all_contexts():
    """加载所有 context 档案"""
    contexts = []
    for filepath in CONTEXT_DIR.glob("20*.md"):  # 匹配 2026-08-05-*.md
        meta = parse_context_file(filepath)
        if meta:
            contexts.append(meta)

    # 按日期倒序排序
    contexts.sort(key=lambda x: (x.get('date', ''), -x.get('rank', 999)), reverse=True)
    return contexts


def generate_index(contexts):
    """生成主索引 INDEX.md"""
    lines = [
        "# Product Hunt Context 档案索引",
        "",
        f"> 共 {len(contexts)} 个产品 · 最后更新 {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "## 最近更新（按日期倒序）",
        ""
    ]

    # 按日期分组
    by_date = defaultdict(list)
    for ctx in contexts:
        date = ctx.get('date', 'unknown')
        by_date[date].append(ctx)

    for date in sorted(by_date.keys(), reverse=True):
        products = by_date[date]
        lines.append(f"### {date}（{len(products)} 个产品）")
        lines.append("")

        for ctx in sorted(products, key=lambda x: x.get('rank', 999)):
            product = ctx.get('product', 'Unknown')
            filename = ctx.get('filename', '')
            category = ctx.get('category', '')
            subcategory = ctx.get('subcategory', '')
            cat_display = f"{category} / {subcategory}" if subcategory else category

            # 从原档案读取一句话定位（如果有的话）
            tagline = ctx.get('中文tagline', ctx.get('subcategory', ''))

            lines.append(f"{ctx.get('rank', '?')}. [{product}]({filename}) · {cat_display}")
            signals = ctx.get('key_signals') or []
            if signals:
                lines.append(f"   - {' · '.join(signals)}")

        lines.append("")

    lines.extend([
        "## 快速导航",
        "",
        "- [按品类浏览](by-category/) · [按技术栈浏览](by-tech/) · [按商业模式浏览](by-business/)",
        "- [时间轴趋势](timeline/)",
        "",
        "## 统计",
        ""
    ])

    # 统计
    categories = defaultdict(int)
    tags_count = defaultdict(int)
    open_source_count = sum(1 for c in contexts if c.get('open_source'))

    for ctx in contexts:
        cat = ctx.get('category', 'Unknown')
        categories[cat] += 1
        for tag in ctx.get('tags', []):
            tags_count[tag] += 1

    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        lines.append(f"- {cat}: {count} 个")

    lines.append(f"- 开源产品: {open_source_count} 个")
    lines.append("")

    if tags_count:
        lines.append("## 热门标签")
        lines.append("")
        for tag, count in sorted(tags_count.items(), key=lambda x: -x[1])[:10]:
            lines.append(f"- #{tag}: {count} 个")
        lines.append("")

    return "\n".join(lines)


def generate_category_indexes(contexts):
    """生成品类索引 by-category/*.md"""
    CATEGORY_DIR.mkdir(exist_ok=True)

    by_category = defaultdict(list)
    for ctx in contexts:
        cat = ctx.get('category', 'Unknown')
        by_category[cat].append(ctx)

    for category, products in by_category.items():
        slug = category.lower().replace(' ', '-').replace('/', '-')
        filepath = CATEGORY_DIR / f"{slug}.md"

        lines = [
            f"# {category} 产品档案",
            "",
            f"> 共 {len(products)} 个 · 最后更新 {datetime.now().strftime('%Y-%m-%d')}",
            "",
            "## 产品列表（按日期倒序）",
            ""
        ]

        for ctx in sorted(products, key=lambda x: x.get('date', ''), reverse=True):
            product = ctx.get('product', 'Unknown')
            date = ctx.get('date', '')
            subcategory = ctx.get('subcategory', '')
            filename = ctx.get('filename', '')

            lines.append(f"- [{product}](../{filename}) · {subcategory} · {date}")

        lines.append("")
        filepath.write_text("\n".join(lines), encoding='utf-8')
        print(f"✓ 生成品类索引: {filepath.name}")


def generate_tech_indexes(contexts):
    """生成技术栈索引 by-tech/*.md"""
    TECH_DIR.mkdir(exist_ok=True)

    by_tech = defaultdict(list)
    for ctx in contexts:
        for tag in ctx.get('tags', []):
            by_tech[tag].append(ctx)
        for tech in ctx.get('tech_stack', []):
            by_tech[tech].append(ctx)

    for tech, products in by_tech.items():
        slug = re.sub(r'[^\w一-鿿-]+', '-', tech.lower().replace(' ', '-').replace('.', '')).strip('-')
        filepath = TECH_DIR / f"{slug}.md"

        lines = [
            f"# {tech} 相关产品",
            "",
            f"> 共 {len(products)} 个 · 最后更新 {datetime.now().strftime('%Y-%m-%d')}",
            "",
            "## 产品列表（按日期倒序）",
            ""
        ]

        for ctx in sorted(products, key=lambda x: x.get('date', ''), reverse=True):
            product = ctx.get('product', 'Unknown')
            date = ctx.get('date', '')
            subcategory = ctx.get('subcategory', '')
            filename = ctx.get('filename', '')

            lines.append(f"- [{product}](../{filename}) · {subcategory} · {date}")

        lines.append("")
        filepath.write_text("\n".join(lines), encoding='utf-8')
        print(f"✓ 生成技术索引: {filepath.name}")


def generate_business_indexes(contexts):
    """生成商业模式索引 by-business/*.md"""
    BUSINESS_DIR.mkdir(exist_ok=True)

    by_business = defaultdict(list)
    for ctx in contexts:
        model = ctx.get('business_model', 'Unknown')
        by_business[model].append(ctx)

    for model, products in by_business.items():
        slug = model.lower().replace(' ', '-').replace('/', '-')
        filepath = BUSINESS_DIR / f"{slug}.md"

        lines = [
            f"# {model} 产品",
            "",
            f"> 共 {len(products)} 个 · 最后更新 {datetime.now().strftime('%Y-%m-%d')}",
            "",
            "## 产品列表（按日期倒序）",
            ""
        ]

        for ctx in sorted(products, key=lambda x: x.get('date', ''), reverse=True):
            product = ctx.get('product', 'Unknown')
            date = ctx.get('date', '')
            pricing = ctx.get('pricing_start', '')
            filename = ctx.get('filename', '')

            price_display = f" · {pricing}" if pricing else ""
            lines.append(f"- [{product}](../{filename}) · {date}{price_display}")

        lines.append("")
        filepath.write_text("\n".join(lines), encoding='utf-8')
        print(f"✓ 生成商业模式索引: {filepath.name}")


def generate_timeline_indexes(contexts):
    """生成时间轴索引 timeline/*.md"""
    TIMELINE_DIR.mkdir(exist_ok=True)

    by_month = defaultdict(list)
    for ctx in contexts:
        date = ctx.get('date', '')
        if date:
            month = date[:7]  # YYYY-MM
            by_month[month].append(ctx)

    for month, products in by_month.items():
        filepath = TIMELINE_DIR / f"{month}.md"

        lines = [
            f"# {month} Product Hunt 产品时间轴",
            "",
            f"> 共 {len(products)} 个产品 · 更新至 {datetime.now().strftime('%Y-%m-%d')}",
            "",
            "## 按日产品",
            ""
        ]

        by_date = defaultdict(list)
        for ctx in products:
            by_date[ctx.get('date', '')].append(ctx)

        for date in sorted(by_date.keys(), reverse=True):
            day_products = by_date[date]
            lines.append(f"### {date}（{len(day_products)} 个）")
            lines.append("")

            for ctx in sorted(day_products, key=lambda x: x.get('rank', 999)):
                product = ctx.get('product', 'Unknown')
                subcategory = ctx.get('subcategory', '')
                filename = ctx.get('filename', '')

                lines.append(f"{ctx.get('rank', '?')}. [{product}](../{filename}) · {subcategory}")

            lines.append("")

        lines.append("## 按品类统计")
        lines.append("")

        categories = defaultdict(int)
        for ctx in products:
            categories[ctx.get('category', 'Unknown')] += 1

        for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
            lines.append(f"- {cat}: {count} 个")

        lines.append("")
        filepath.write_text("\n".join(lines), encoding='utf-8')
        print(f"✓ 生成时间轴索引: {filepath.name}")


def main():
    print("🔍 扫描 context 档案...")
    contexts = load_all_contexts()

    if not contexts:
        print("❌ 未找到任何带 frontmatter 的档案")
        return

    print(f"✓ 找到 {len(contexts)} 个档案\n")

    print("📝 生成主索引...")
    index_content = generate_index(contexts)
    INDEX_FILE.write_text(index_content, encoding='utf-8')
    print(f"✓ {INDEX_FILE}\n")

    print("📂 生成品类索引...")
    generate_category_indexes(contexts)
    print()

    print("🔧 生成技术索引...")
    generate_tech_indexes(contexts)
    print()

    print("💰 生成商业模式索引...")
    generate_business_indexes(contexts)
    print()

    print("📅 生成时间轴索引...")
    generate_timeline_indexes(contexts)
    print()

    print("✅ 索引生成完成")


if __name__ == "__main__":
    main()
