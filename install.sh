#!/bin/bash
# fusion-story-director-studio v7.0 安装脚本
# 用法：先 clone 本仓库，在仓库根目录执行  bash install.sh
set -e

# 定位仓库根（脚本所在目录）
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$REPO_DIR/skills/fusion-story-director-studio"
DEST="$HOME/.claude/skills/fusion-story-director-studio"

if [ ! -f "$SRC/SKILL.md" ]; then
  echo "找不到 $SRC/SKILL.md —— 请在 clone 下来的仓库根目录运行本脚本。" >&2
  exit 1
fi

mkdir -p "$HOME/.claude/skills"
rm -rf "$DEST"
cp -r "$SRC" "$DEST"

echo "fusion-story-director-studio v7.0 安装完成。"
echo ""
echo "Skill: $DEST"
echo ""
find "$DEST" -type f | sed "s|$HOME|~|" | sort
echo ""
echo "重启 Claude Code 后生效。该 Skill 为自包含单文件（SKILL.md），无需额外 reference。"
