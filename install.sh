#!/bin/bash
# 安装脚本：把本仓库的 skills 复制到 ~/.claude/skills/
# 用法：先 clone 本仓库，在仓库根目录执行  bash install.sh
set -e

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_SRC="$REPO_DIR/skills"
SKILLS_DEST="$HOME/.claude/skills"

if [ ! -d "$SKILLS_SRC" ]; then
  echo "找不到 $SKILLS_SRC —— 请在 clone 下来的仓库根目录运行本脚本。" >&2
  exit 1
fi

mkdir -p "$SKILLS_DEST"

installed=0
for src in "$SKILLS_SRC"/*/; do
  name="$(basename "$src")"
  if [ ! -f "$src/SKILL.md" ]; then
    echo "跳过 $name（没有 SKILL.md）" >&2
    continue
  fi
  rm -rf "${SKILLS_DEST:?}/$name"
  cp -r "$src" "$SKILLS_DEST/$name"
  echo "已安装：$name"
  installed=$((installed + 1))
done

if [ "$installed" -eq 0 ]; then
  echo "没有安装任何 skill —— skills/ 下没有找到含 SKILL.md 的目录。" >&2
  exit 1
fi

echo ""
echo "共安装 $installed 个 skill 到 $SKILLS_DEST"
echo ""
echo "重启 Claude Code 后生效。已安装的 skill："
for src in "$SKILLS_SRC"/*/; do
  name="$(basename "$src")"
  [ -f "$src/SKILL.md" ] || continue
  # description 可能写在同一行，也可能是 YAML 块标量（> 或 |）跟在下一行
  desc="$(awk '/^description:/{
      sub(/^description:[ ]*/,"");
      if ($0 ~ /^[>|]/ || $0 == "") { getline; sub(/^[ ]+/,"") }
      print; exit
    }' "$src/SKILL.md")"
  files="$(find "$SKILLS_DEST/$name" -type f | wc -l | tr -d ' ')"
  printf "  · %-30s (%s 个文件) %s\n" "$name" "$files" "$(echo "$desc" | cut -c1-52)"
done
