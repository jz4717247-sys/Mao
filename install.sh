#!/bin/bash
# jiang-writer v2.4 安装脚本
# 用法：先 clone 本仓库，在仓库根目录执行  bash install.sh
set -e

# 定位仓库根（脚本所在目录）
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$REPO_DIR/skills/jiang-writer"
DEST="$HOME/.claude/skills/jiang-writer"

if [ ! -f "$SRC/SKILL.md" ]; then
  echo "找不到 $SRC/SKILL.md —— 请在 clone 下来的仓库根目录运行本脚本。" >&2
  exit 1
fi

mkdir -p "$HOME/.claude/skills"
rm -rf "$DEST"
cp -r "$SRC" "$DEST"

echo "jiang-writer v2.4 安装完成。"
echo ""
echo "Skill: $DEST"
echo ""
find "$DEST" -type f | sed "s|$HOME|~|" | sort
echo ""
echo "重启 Claude Code 后生效。写竖屏微短剧时，Skill 会加载 references/vertical-microdrama.md。"
