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
find "$SKILLS_DEST" -type f -name '*.md' | sed "s|$HOME|~|" | sort
echo ""
echo "重启 Claude Code 后生效。"
echo "  · ai-us-drama-writer          直接开工：概念 → 可生成的 AI 美剧单集"
echo "  · fusion-story-director-studio 全链路：创意策划 / 深度开发 / 诊断 / 改编 / 其他媒介"
