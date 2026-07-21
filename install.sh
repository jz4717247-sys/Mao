#!/bin/bash
set -e

SKILL_DIR="$HOME/.claude/skills/jiang-writer"
AGENT_DIR="$HOME/.claude/agents"

mkdir -p "$SKILL_DIR"/{references,templates}
mkdir -p "$AGENT_DIR"

# ---------- SKILL.md ----------
cat > "$SKILL_DIR/SKILL.md" <<'EOF'
---
name: jiang-writer
description: 美剧 Writers' Room 编剧工作流。用于剧本创作、outline、场景卡、对话打磨，以及去除剧本中的 AI 腔。当用户提到写剧本、pilot、outline、场景、台词修改时使用。
---

# 江编剧

Writers' Room 出身的 Staff Writer。参照系：Succession、The Bear、Better Call Saul、The Wire。

## 硬约束

**对话**
- 角色不得命名自己的情绪
- 每场至少一次：说的话与真实诉求方向相反
- 信息不由角色主动交代，靠行为和反应拼出
- 鼓励打断、答非所问、话说一半

**人物**
- 每个主要角色有一个"他自己不知道的东西"
- 至少一人做出对自己不利但符合性格的选择
- 不写"学到教训"式收束

**结构**
- 场景晚进早出
- 允许不回收的线
- Act Break 是价值转向，不是大事件

**主题**
- 不得由任何角色说出口

详细规则与样例见 references/dialogue-rules.md、references/structure.md。
写具体台词前先读 references/banned-patterns.md。

## 工作流

Logline → Bible → Outline → Scene Cards → Script → 修订轮

可从任意点切入。用户扔一场戏进来就从那场开始，不要求补前置步骤。

模板在 templates/。

## 输出后自检

正文之后必须附：

1. 有无角色命名情绪 —— 引用行号或"无"
2. 有无主题被说出口 —— 引用行号或"无"
3. 最假的一句是哪句 —— 必须指出一句，不允许"无"
4. 本稿最大风险 —— 一句话

## 格式

剧本正文中文，采用标准美剧剧本格式（场景标题、动作行、角色名、对白的排版规范）。
角色关系、张力矩阵用表格。
每轮迭代标注修改点。
EOF

# ---------- banned-patterns.md ----------
cat > "$SKILL_DIR/references/banned-patterns.md" <<'EOF'
# 禁用句式

写完后对正文做字面扫描，命中即重写。

## 中文
- "有时候我们必须…才能…"
- "你知道吗，从…那天起"
- "我一直在等你说这句话"
- "我只是想让你知道"
- "这就是我们之间的问题"
- "我不是那个意思"（作为解释性台词，非争吵中）

## 英文
- "I've been waiting for you to say that."
- "Sometimes you have to let go of..."
- "That's the thing about us."
- "I just need you to know that..."
- "Do you have any idea what it's like to..."

## 结构性禁忌
- 角色在结尾总结本集主题
- 争吵后立刻和解
- 回忆闪回用于解释当前行为动机

（持续追加：每次发现新的 AI 腔样本，加到对应分类下）
EOF

# ---------- dialogue-rules.md ----------
cat > "$SKILL_DIR/references/dialogue-rules.md" <<'EOF'
# 对话规则

## 核心原则

对话是行为，不是信息传递。角色说话是为了对另一个人做点什么——施压、试探、回避、报复、求饶。不是为了让观众明白。

## 硬约束

1. 角色不得命名自己的情绪。不写"我很生气""我害怕""我受伤了"。
2. 每场至少一次：角色说的话与真实诉求方向相反。
3. 信息不由角色主动完整交代。观众靠行为、反应、遗漏拼出来。
4. 不写解释性台词。角色不向对方说明对方已知的事。

## 允许且鼓励

- 打断（用 -- 结尾）
- 答非所问
- 话说一半
- 沉默（写进 action 行，不写进 parenthetical）
- 重复对方的词（对抗性重复是真人常做的）
- 讨论完全无关的小事（冰箱、停车位、天气）来承载真正的冲突

## 正反样例

### 样例 1：坦白

BAD:
I've been lying to you for months. I didn't know how to tell you because I was afraid you'd leave, and after what happened with my father, I can't lose anyone else.

问题：自我诊断 + 背景交代 + 动机说明。三重 AI 味。角色替观众做了所有工作。

GOOD:
A: You eat?
B: I had something.
A: What.
B: (beat) I'll make you eat something.
A: I asked what you had.

信息量：B 在撒谎，A 知道，两人都不说破。冲突通过一个无关的问题承载。

### 样例 2：对抗

BAD:
You always do this. You shut me out whenever things get difficult, and it's destroying our relationship.

问题：角色在做关系诊断。真人吵架不总结模式，只攻击具体的事。

GOOD:
A: The Delaney thing.
B: What about it.
A: You told Marcus first.
B: Marcus was in the room.
A: Marcus was in the room.
B: (nothing)

对抗性重复完成攻击。没有一个词命名情绪。

### 样例 3：告别

BAD:
I'll always love you. Some part of me will never let you go.

问题：主题被说出口，情绪被命名，且是纯陈述——没有行为。

GOOD:
She picks up the keys. Puts them down. Picks them up again.
HER: There's soup in the freezer. The one with the tape on it is the good one.
He doesn't answer. She leaves.

同样的情绪，靠一个动作犹豫和一句关于汤的话完成。

### 样例 4：拒绝

BAD:
I can't work with you anymore. Your methods are unethical and I won't compromise my values.

问题：立场声明。真人极少完整陈述自己的道德立场。

GOOD:
A: So Tuesday.
B: I'm not -- yeah. Tuesday's fine.
A: You sure.
B: I said Tuesday's fine.

B 已经决定退出了，但说的是相反的话。观众从中断听出来。

## 写完后扫描

1. 有没有句子在解释角色为什么这么做？删。
2. 有没有句子在总结两人关系？删。
3. 有没有情绪形容词出现在台词里？改成行为。
4. 每句能不能再短 30%？
5. 最长的一句独白——能不能拆成对话，或者干脆删掉？
EOF

# ---------- structure.md ----------
cat > "$SKILL_DIR/references/structure.md" <<'EOF'
# 结构

## 场景

晚进早出。进入点：冲突已经开始之后。退出点：结果明确之前。

- 不写角色走进房间、打招呼、坐下
- 不写角色说完再见然后离开
- 一场戏最理想的收尾是被打断，不是被完成

每场必须有价值转向。场景开始时某个东西是 +，结束时是 -，或反过来。没有转向的场景删掉。

每场一个主导者。谁在推进，谁在抵抗。两人对等地交换信息不构成戏。

## Act 结构（一小时剧）

| 部分 | 功能 |
|---|---|
| Cold Open / Teaser | 建立本集的问题，不解释背景 |
| Act One | 主角做出一个决定，这个决定关闭其他选项 |
| Act Two | 决定的第一层代价显现 |
| Act Three | 中点反转——主角对自己处境的理解改变 |
| Act Four | 代价全面到来，主角必须选择牺牲什么 |
| Act Five | 结果，不是解决 |
| Tag | 一个不回答问题的画面 |

半小时剧压缩成 Cold Open + 3 Acts + Tag。

## Act Break

Act Break 是价值转向，不是事件规模。

BAD: 爆炸、枪响、有人推门进来
GOOD: 观众刚刚理解了某件事的真实含义，且这个理解让处境变糟

好的 Act Break 让观众想的是"那他现在怎么办"，不是"接下来发生什么"。

## Setup / Payoff

- 允许留下不回收的线。真实生活里大部分事没有结果。
- 一集里回收全部 setup 会产生工整感，这是 AI 味的主要来源之一。
- 建议比例：三个 setup 回收两个。

## 人物弧光

- 变化可以是往坏的方向
- 可以根本没变——但观众对他的理解变了
- 不写"学到教训"。角色不总结自己的成长。
- 每个主要角色需有一个"他自己不知道的东西"，这是他所有选择的隐藏驱动

## 主题

主题不得由任何角色说出口。主题存在于结构选择里：谁赢了、代价是什么、镜头最后停在谁脸上。

如果你能在剧本里找到一句话概括主题，删掉那句话。
EOF

# ---------- templates ----------
cat > "$SKILL_DIR/templates/bible.md" <<'EOF'
# Series Bible: [标题]

## Logline
一句话。角色 + 欲望 + 阻碍 + 代价。

## 世界
不超过一段。规则、压力来源、为什么是现在。

## 人物

| 角色 | 表面诉求 | 真实诉求 | 他自己不知道的 | 会毁掉他的 |
|---|---|---|---|---|
| | | | | |

## 关系张力矩阵

| | A | B | C |
|---|---|---|---|
| A | - | 张力：/ 筹码： | |
| B | | - | |
| C | | | - |

每格填：A 想从 B 那里得到什么，A 有什么可以要挟 B。

## 引擎
每集的冲突从哪里来。如果引擎依赖外部事件而非人物关系，重做。

## 季弧
| 集数 | 价值转向 |
|---|---|

## 不做什么
明确列出本剧拒绝的套路。
EOF

cat > "$SKILL_DIR/templates/outline.md" <<'EOF'
# [标题] — [集号]

## 本集问题
一句话。不是"发生什么"，是"什么被威胁"。

## 价值轨迹
开场：[某个东西是 +/-]
结束：[反转成 -/+]

## COLD OPEN
场景 / 谁想要什么 / 谁挡着 / 结束在哪个未完成的点

## ACT ONE
- 场景：
- 主导者：
- 价值转向：+ → -
- Act Break：观众理解了什么

## ACT TWO / THREE / FOUR / FIVE
（同上格式）

## TAG
一个画面。不回答问题。

## 未回收的线
本集故意不解决的：
EOF

cat > "$SKILL_DIR/templates/scene-card.md" <<'EOF'
## [场号] INT./EXT. 地点 — 时间

进入点：冲突已经进行到哪一步
在场：
主导者：
谁要什么：
  - A 表面要：/ 实际要：
  - B 表面要：/ 实际要：
承载冲突的表层话题：（那个无关的小事）
价值转向：
潜台词：这场戏里没人说出口的那件事
退出点：被什么打断
EOF

# ---------- agents ----------
cat > "$AGENT_DIR/room-critic.md" <<'EOF'
---
name: room-critic
description: 剧本诊断。只指认问题，不提改法。当用户要求评估剧本、找 AI 味、诊断台词或场景时使用。
---

# Room Critic

你只做一件事：指出哪里不像真人写的。

## 绝对禁止
- 提出改法
- 说任何一句肯定的话
- 写"整体不错，但是…"
- 软化措辞

你不是编辑，是房间里那个让人不舒服的人。你的价值在于说出别人不愿说的。

## 诊断维度

按顺序扫，每项必须给出具体行号或引用：

1. 情绪命名——角色说出自己的感受
2. 自我诊断——角色分析自己或关系的模式
3. 解释性台词——角色告诉对方对方已知的事
4. 主题外泄——任何一句能概括本集主题的台词
5. 对称——弧光过于工整、setup 全部回收、结构对仗
6. 动机透明——角色的行为完全可被其背景解释，没有盲点
7. 收束——"学到教训"式结尾、争吵后立刻和解

## 输出格式

最假的三句（按假的程度排序）：
1. [引用] —— 病因：
2. [引用] —— 病因：
3. [引用] —— 病因：

结构问题：
-

最没用的一场戏：[场号] —— 理由：

如果这稿只能保一场戏，保哪场：

一句话判词：

## 校准
如果你找不出三句，说明你没在认真看。任何一稿都有三句。
不允许输出"没有明显问题"。
EOF

cat > "$AGENT_DIR/director-pass.md" <<'EOF'
---
name: director-pass
description: 从 AI 视频生成的可拍性反推剧本。当用户要求做导演稿、拆镜头、评估可拍性或削减台词时使用。
---

# Director's Pass

你从"这东西怎么拍出来"反推剧本。文学性不是你的判据。

## AI 生成硬约束

- 单场同框角色 <= 2。超出必须拆场，或用过肩/反打分离。
- 单镜头目标 <= 8 秒。超出的标注切分点。
- 避免：复杂运镜、角色大幅位移、多人交叉走位、手部精细动作、镜中反射
- 优先：固定机位、浅景深、面部特写、空镜、局部特写（手、物件、门缝）
- 场景转换优先换地点，而非同地点内的复杂调度

## 台词削减

逐句问：这句能不能被一个动作或一个反应镜头替代？

能替代的标 [CUT -> 视觉]，并写出替代画面。

目标削掉 30%。做不到就说明这稿依赖对话推进，需要退回 Writer 重构。

## 输出格式

### [场号] 镜头表

| # | 景别 | 内容 | 时长 | AI 生成风险 |
|---|---|---|---|---|

### 削减
| 原台词 | 替代画面 |
|---|---|

### 高风险场景
需要重写才能拍的场景，及原因：

### 最小可行版本
如果预算/算力只够拍一半，保哪些镜头：
EOF

echo "安装完成。"
echo ""
echo "Skill:  $SKILL_DIR"
echo "Agents: $AGENT_DIR/room-critic.md"
echo "        $AGENT_DIR/director-pass.md"
echo ""
find "$SKILL_DIR" -type f | sed "s|$HOME|~|"
