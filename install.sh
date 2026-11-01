#!/bin/bash
# 安装脚本：把 skills/ 下的 Skill 复制到 ~/.claude/skills/
# 用法：先 clone 本仓库，在仓库根目录执行
#   bash install.sh                    # 安装全部（jiang-writer + ultimate-creative）
#   bash install.sh jiang-writer       # 只装指定的
set -e

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ "$#" -gt 0 ]; then
  SKILLS=("$@")
else
  SKILLS=()
  for d in "$REPO_DIR"/skills/*/; do SKILLS+=("$(basename "$d")"); done
fi

mkdir -p "$HOME/.claude/skills"

for name in "${SKILLS[@]}"; do
  SRC="$REPO_DIR/skills/$name"
  DEST="$HOME/.claude/skills/$name"
  if [ ! -f "$SRC/SKILL.md" ]; then
    echo "找不到 $SRC/SKILL.md —— 请在 clone 下来的仓库根目录运行本脚本。" >&2
    exit 1
  fi
  rm -rf "$DEST"
  cp -r "$SRC" "$DEST"
  find "$DEST" -name '__pycache__' -type d -prune -exec rm -rf {} +
  echo "已安装 $name → ${DEST/#$HOME/~}（$(find "$DEST" -type f | wc -l) 个文件）"
done

echo ""
echo "重启 Claude Code 后生效。"
