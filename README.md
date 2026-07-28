# jiang-writer v2.4

美剧 Writers' Room 编剧工作流，装进 Claude Code。**在美剧底座上补了竖屏微短剧模块**——既能开发/诊断/修订美剧规格的剧集，也能写抖音/快手的竖屏投流爽剧（重生、逆袭、打脸、甜宠、马甲）。v2.2 补上运营侧：全剧节奏波形、爽感配比、付费卡点、内容合规。v2.3 补上防重复引擎：冲突装置账本、R0-R3 分级、冷却配额、变奏升级、同质化红线——治多集剧最大的弃剧原因「换皮重复」。v2.4 补上两件长期缺的：**去 AI 味独立 Pass**（分档改动半径 + 命中密度分流）与**跨会话断点续写**（canon lock 落盘，不再随对话上下文丢失）。

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
    anti-repetition.md         ★ v2.3：防重复——冲突装置账本/冷却配额/变奏升级
    humanize-pass.md           ★ v2.4：去 AI 味执行层——L1/L2/L3 分档、命中密度分流
    project-state.md           ★ v2.4：跨会话状态——canon 落盘/pass 状态/陈旧传播
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
    project-state.json         ★ v2.4 新增：跨会话状态文件骨架
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

## 去 AI 味 Pass（v2.4 新增）

原本 `ai-patterns.md` 只管**识别**（哪些句子有风险），缺一份**执行**契约——结果要么扫出一堆问题然后全剧重写，要么按感觉润色、改完所有人变成同一张嘴。`humanize-pass.md` 补上这层：

**先测命中密度，再决定改不改。** 抽样算风险句占比：<10% 走 L1；10–30% 是本 Pass 主场；**>30% 停手**——病因不在措辞，在场景没有真实冲突或信息全靠对白搬运，转 `critic-pass.md`。逐句润色只会把空洞句子换成好听的空洞句子。

**三档按改动半径分，不按用力程度分：**

| 档 | 可动范围 | 硬约束 |
|---|---|---|
| L1 句内 | 只动被标记的句子 | 不增删台词条数、不改说话人 |
| L2 场内（默认） | 单场内重分配信息、合并删改、换人说 | 场景目标/阻力/结局状态/因果推动不变 |
| L3 结构 | 删场、挪 payoff、拆合场景 | **须用户明确许可**，执行后标下游 stale |

**改写三验**：更具体了吗 / 还是这个角色吗 / 场景功能还在吗——任一条不过就回退原句。改不动的留着并进"未改清单"，不凑修改量。

另外两条边界：**过度去味也是一种 AI 味**（到处撒口语碎片、全员答非所问、故意留错别字——只是把一种同质化换成另一种）；**竖屏项目自动降档**，内心 OS 和打脸金句是付费理由，不当风险句扫掉。

竖屏另走一套阈值（`<20%` L1 ／ `20–45%` 照改但功能层单列 ／ `>45%` 停手），且**钩子层不计入改动半径**——开篇钩与集尾钩是形态硬约束，修废钩不需要 L3 许可，否则会卡成"把废钩润色成更好听的废钩"。这两条是 v2.4 首次实测跑出来的缺口，回归锚见 `evaluation-cases.md`。

**本 Skill 不做反检测**——目标是让句子承担人物和场景功能，不是让文本在检测器上得分变低。

## 断点续写（v2.4 新增）

canon lock 原先只活在对话上下文里，换个会话就丢；丢 canon 的代价不是重写一段，是新集和已定稿的集对不上。`project-state.md` + `.jiang-state.json` 把形态约束、canon lock、产物路径、逐集 pass 状态、Showrunner 裁决落盘。

**状态不是流程。** 参考项目用的是线性阶段机（`/start→/plan→…`），本 Skill 是模式路由，所以只搬状态持久化、不搬强制流程：状态文件记录**已经发生了什么**，不规定**接下来必须做什么**。显示 Bible 缺失也照写你要的那场戏，不要求补前置文档。

**陈旧传播**：pass 状态取 `none/draft/done/stale` 四值。改 canon → 全项目标 stale 并先报影响范围；改大纲 → 该集及受影响集的正文与 pass 标 stale；改声纹卡 → 全集 `voice` 标 stale。stale 只是"这里没被复核过"，不等于强制返工。状态与实际文件冲突时**以文件为准**。

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
- 批量去 AI 味：`用 jiang-writer 把这五集润一遍，只改句子别动结构` → L1 档，先抽样报密度
- 竖屏爽剧：`用 jiang-writer 写一集竖屏重生打脸短剧，95 秒` → 自动加载竖屏模块
- Showrunner 拍板：`把这些 notes 交给 showrunner pass 定取舍`
- 断点续写：`用 jiang-writer 接着上次，这个项目做到哪了` → 读 `.jiang-state.json` 汇报进度与 canon

## 手机上的替代方案

Claude Code 是命令行工具，手机装不了。临时方案：在 Claude App 新建 Project，把 `SKILL.md` 贴进 Project Instructions，把需要的 reference 当文件上传。局限：没有真正的模式隔离，reference 需手动挑着贴。
