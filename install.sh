#!/bin/bash
# 安装脚本：把本仓库的 skills 复制到 ~/.claude/skills/
# 用法：先 clone 本仓库，在仓库根目录执行  bash install.sh
set -e

# 定位仓库根（脚本所在目录）
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST_ROOT="$HOME/.claude/skills"

# 要安装的 skill 列表
SKILLS=(jiang-writer screenwriting-master director-master)

mkdir -p "$DEST_ROOT"

for name in "${SKILLS[@]}"; do
  SRC="$REPO_DIR/skills/$name"
  DEST="$DEST_ROOT/$name"
  if [ ! -f "$SRC/SKILL.md" ]; then
    echo "找不到 $SRC/SKILL.md —— 请在 clone 下来的仓库根目录运行本脚本。" >&2
    exit 1
  fi
  rm -rf "$DEST"
  cp -r "$SRC" "$DEST"
  echo "已安装 Skill: $DEST"
done

echo ""
echo "已安装的文件："
for name in "${SKILLS[@]}"; do
  find "$DEST_ROOT/$name" -type f | sed "s|$HOME|~|" | sort
done
echo ""
echo "重启 Claude Code 后生效。"
echo "  - jiang-writer：美剧 Writers' Room + 竖屏微短剧工作流"
echo "  - screenwriting-master：全格式编剧（概念超短片 / 短片 / 90 分钟长片 / 多集剧集）"
echo "  - director-master：导演视听（定调 / 节奏 / 分镜拆解 → 九列分镜表 xlsx）"
