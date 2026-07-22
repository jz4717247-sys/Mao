# jiang-writer v2.2

美剧 Writers' Room 编剧工作流，装进 Claude Code。**在美剧底座上补了竖屏微短剧模块**——既能开发/诊断/修订美剧规格的剧集，也能写抖音/快手的竖屏投流爽剧（重生、逆袭、打脸、甜宠、马甲）。v2.2 补上运营侧：全剧节奏波形、爽感配比、付费卡点、内容合规。

## 结构

```
skills/jiang-writer/
  SKILL.md                     主控：任务模式路由、canon lock、流程、质量门槛
  agents/openai.yaml           OpenAI 界面配置（非 Claude Code）
  references/                  按需加载的规则库
    format-selection.md        剧集形态选择（含竖屏微短剧一行）
    vertical-microdrama.md     ★ 竖屏投流爽剧：单集钩子/爽点手艺
    vertical-season-and-monetization.md  ★ v2.2：全剧节奏波形/爽感配比/付费卡点
    vertical-compliance.md     ★ v2.2：内容合规红线（七维度/P0-P2/出海）
    structure.md / series-engine.md / dialogue-and-subtext.md
    character-voice.md / ai-patterns.md / continuity-and-story-ledger.md
    critic-pass.md / voice-pass.md / showrunner-pass.md / director-pass.md
    revision-room.md / quality-rubric.md / evaluation-cases.md
    voice-card-example.md
  assets/templates/            按需复制的模板
    series-bible / season-board / episode-outline / beat-sheet
    scene-card / teleplay-format / character-voice-card
    continuity-ledger / script-notes
    vertical-episode.md        ★ v2.1 新增：竖屏单集卡（钩子链/爽点节拍）
```

设计取向：**模式路由**（只跑用户要的那一档，不强制走完整编剧室）、**上下文扫描而非字面黑名单**（`ai-patterns.md` 判断句子功能再决定改不改）、**证据化诊断**（`critic-pass.md` 不强凑问题，没问题就说没问题）、**三层声纹**（指纹/关系语态/压力变体，不降格成口头禅清单）。

## 竖屏微短剧模块（v2.1 新增）

美剧的"风险信号"，在竖屏投流爽剧里多是**类型承诺**。该模块反转了这些默认值：

| 手法 | 美剧判断 | 竖屏微短剧判断 |
|---|---|---|
| 内心 OS / 情绪直给 | 作者替角色解释，风险 | 刚需，承担重生记忆与身份反差 |
| 打脸金句 / 主题直给 | 万能句、作者腔 | 类型核心买点（但要落在具体人和事） |
| setup 全回收 | 工整过度 | 资产，留存靠钩子兑现 |
| 扁平配角 | 冲突同质化 | 配角可功能化，主角需一个钩人反差 |

外加：钩子系统（开篇钩/集内钩/集尾钩/付费点钩）、打脸"憋—爆"节拍、名词控制、单集微结构、投流剧七种死法、竖屏 AI 视频制作约束（单场≤2人、单镜头≤8秒、中英对照）。SKILL.md 检测到项目是竖屏投流剧时自动指向 `vertical-microdrama.md`。

**v2.2 运营侧**（消化自研究开源短剧生态的通用方法论，按本 Skill「数值当基线不当硬配额」的分寸重写）：
- `vertical-season-and-monetization.md`：四段式节奏波形（起势15%/攀升30%/风暴35%/决战20%，带爽点强度与加减速比例）、五类爽感与按段密度、题材配比、付费卡点集数基线（首卡8-12集…）与卡点选择三原则。
- `vertical-compliance.md`：七个合规维度、P0红线/P1-P2灰区分级、逐集与全剧自检、题材高发踩坑、出海补充。

## 安装（电脑端）

前提：已装 Claude Code（`npm install -g @anthropic-ai/claude-code`）。

```bash
git clone <本仓库> && cd Mao
bash install.sh          # 复制 skills/jiang-writer 到 ~/.claude/skills/
```

装完重启 Claude Code。（v2.1 文件数较多，安装脚本改为从 clone 的仓库复制，不再是可粘贴的自包含脚本。）

## 用法

Skill 按 SKILL.md 的模式路由自动判断该跑哪档：

- 写稿：`用 jiang-writer 帮我写这集的 cold open`
- 诊断：`用 jiang-writer 只审查这版，别改`
- 检查并去 AI 味：`用 jiang-writer 检查并修，声纹和 AI 腔一起看`
- 竖屏爽剧：`用 jiang-writer 写一集竖屏重生打脸短剧，95 秒` → 自动加载竖屏模块
- Showrunner 拍板：`把这些 notes 交给 showrunner pass 定取舍`

## 手机上的替代方案

Claude Code 是命令行工具，手机装不了。临时方案：在 Claude App 新建 Project，把 `SKILL.md` 贴进 Project Instructions，把需要的 reference 当文件上传。局限：没有真正的模式隔离，reference 需手动挑着贴。
