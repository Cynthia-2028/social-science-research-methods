#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Skill 包自检：结构、frontmatter、交叉引用、禁词、深度、体量。

用法：
    python scripts/audit.py [skill_root]

退出码 0 表示通过（可能带警告），1 表示有硬错误。
"""
import os
import re
import sys

REQUIRED_FILES = ["SKILL.md", "README.md", "LICENSE", "CHANGELOG.md"]
REQUIRED_DIRS = ["references"]
FRONTMATTER_KEYS = [
    "name", "version", "display_name", "display_name_en",
    "description", "description_zh", "description_en",
]

# 禁词：书名、作者名、期刊名、册数表述
BANNED = [
    # 册数表述
    "多少本书", "这本书", "本书共", "三本书", "两本书",
    # 常见教材作者姓氏（防止把材料名写进 skill）
    "Neuman", "Babbie", "Grønmo", "Gronmo", "Creswell", "Hernán", "Hernan",
    "Mahoney", "Treiman", "Stockemer", "Haslwanter", "Castellani",
    "Hooley", "Lepkowski", "Silverman", "Cohen's", "James, Witten",
    "ISLR", "What If", "SAGE", "Springer", "Wiley", "Pearson",
    # 期刊名
    "American Sociological Review", "American Journal of Sociology",
]

# 允许出现的例外（语境词，不是书名）
WHITELIST_CONTEXT = ["Cohen's d", "Silverman 法则", "Silverman法则"]


def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def strip_whitelist(text):
    for w in WHITELIST_CONTEXT:
        text = text.replace(w, "")
    return text


def main(root):
    errors, warns, info = [], [], []

    # 1. 结构
    for f in REQUIRED_FILES:
        p = os.path.join(root, f)
        if not os.path.isfile(p):
            errors.append(f"缺少必需文件：{f}")
    for d in REQUIRED_DIRS:
        p = os.path.join(root, d)
        if not os.path.isdir(p):
            errors.append(f"缺少必需目录：{d}/")

    # 2. 深度（skill 包最多两级）
    for dirpath, dirnames, filenames in os.walk(root):
        rel = os.path.relpath(dirpath, root)
        depth = 0 if rel == "." else len(rel.replace("\\", "/").split("/"))
        if depth > 1:
            errors.append(f"目录层级超过两级：{rel}")
        for fn in filenames:
            if fn.startswith("."):
                warns.append(f"隐藏文件：{os.path.join(rel, fn)}")

    # 3. frontmatter
    skill_md = os.path.join(root, "SKILL.md")
    if os.path.isfile(skill_md):
        txt = read(skill_md)
        m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
        if not m:
            errors.append("SKILL.md 缺少 YAML frontmatter")
        else:
            fm = m.group(1)
            for k in FRONTMATTER_KEYS:
                if not re.search(rf"^{k}\s*:", fm, re.M):
                    errors.append(f"frontmatter 缺少字段：{k}")
            name = re.search(r"^name\s*:\s*(.+)$", fm, re.M)
            if name and name.group(1).strip().strip('"').strip("'") != os.path.basename(root):
                warns.append(
                    f"frontmatter name（{name.group(1).strip()}）与目录名（{os.path.basename(root)}）不一致"
                )

    # 4. 交叉引用
    refs_dir = os.path.join(root, "references")
    existing = set()
    if os.path.isdir(refs_dir):
        existing = {f for f in os.listdir(refs_dir) if f.endswith(".md")}
    md_files = []
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if fn.endswith(".md"):
                md_files.append(os.path.join(dirpath, fn))

    for p in md_files:
        txt = read(p)
        for ref in re.findall(r"`(?:\.\./)?references/([\w\-.]+\.md)`", txt):
            if ref not in existing:
                errors.append(f"{os.path.relpath(p, root)} 引用了不存在的文件：references/{ref}")
        for ref in re.findall(r"`(?:\.\./)?assets/([\w\-.]+\.md)`", txt):
            if not os.path.isfile(os.path.join(root, "assets", ref)):
                errors.append(f"{os.path.relpath(p, root)} 引用了不存在的文件：assets/{ref}")

    # 5. 禁词
    for p in md_files:
        txt = strip_whitelist(read(p))
        for w in BANNED:
            if w in txt:
                errors.append(f"{os.path.relpath(p, root)} 出现禁词：{w}")

    # 6. 体量统计
    total_chars, total_lines = 0, 0
    for p in md_files:
        txt = read(p)
        total_chars += len(txt)
        total_lines += txt.count("\n") + 1
    info.append(f"文件数：{len(md_files)} 个 markdown")
    info.append(f"总字符：{total_chars:,}")
    info.append(f"总行数：{total_lines:,}")
    info.append(f"references：{len(existing)} 个")
    for f in sorted(existing):
        c = len(read(os.path.join(refs_dir, f)))
        info.append(f"  - {f}: {c:,} 字符")

    print("=" * 60)
    for i in info:
        print(i)
    print("=" * 60)
    if warns:
        print(f"\n警告 {len(warns)} 条：")
        for w in warns:
            print("  ! " + w)
    if errors:
        print(f"\n错误 {len(errors)} 条：")
        for e in errors:
            print("  x " + e)
        return 1
    print("\n通过：结构与内容检查无误。")
    return 0


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.exit(main(os.path.abspath(root)))
