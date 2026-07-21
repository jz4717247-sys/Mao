# jiang-writer

美剧 Writers' Room 编剧工作流，装进 Claude Code。一个 Skill（写稿）+ 两个 subagent（诊断、导演稿），核心目标是去掉剧本里的 AI 腔。

## 装什么

| 文件 | 作用 |
|---|---|
| `skills/jiang-writer/SKILL.md` | 主 Skill，写稿时自动触发 |
| `skills/jiang-writer/references/banned-patterns.md` | 禁用句式，长期资产，持续追加 |
| `skills/jiang-writer/references/dialogue-rules.md` | 对话规则 + 正反样例 |
| `skills/jiang-writer/references/structure.md` | 场景 / Act / 主题结构 |
| `skills/jiang-writer/templates/` | bible / outline / scene-card 模板 |
| `agents/room-critic.md` | 只诊断不改稿的批评者 |
| `agents/director-pass.md` | 从 AI 视频可拍性反推剧本 |

`install.sh` 是以上全部内容的自包含副本，供直接粘贴终端。仓库里的 `skills/`、`agents/` 目录是同样内容的可读版本——用手机在 GitHub App 里读、改都行，改完再同步进 `install.sh`。

## 装到电脑

前提：先装了 Claude Code（`npm install -g @anthropic-ai/claude-code`）。

```bash
bash install.sh
```

会写入 `~/.claude/skills/jiang-writer/` 和 `~/.claude/agents/`。装完重启 Claude Code。

## 用法

- 写稿：直接说"帮我写这集的 cold open"，Skill 自动触发
- 批稿：`用 room-critic 看一下这版`
- 导演稿：`跑一遍 director-pass`

第一次跑完，把它写坏的句子追加进 `references/banned-patterns.md`。那个文件才是长期资产。

## 手机上的替代方案（没有电脑时）

Claude Code 是命令行工具，手机装不了。临时方案：

1. Claude App 里新建 Project，把 `SKILL.md` 内容贴进 Project Instructions。
2. `banned-patterns.md`、`dialogue-rules.md` 等当文件上传到 Project 知识库。
3. 需要诊断时，在对话里说"切到 room-critic 模式，只诊断不改"，把 `agents/room-critic.md` 内容贴进去。

局限：没有真正的 subagent 隔离（Critic 和 Writer 共享上下文），样例库不能自动增长。基本工作流能跑，隔离性弱一些。
