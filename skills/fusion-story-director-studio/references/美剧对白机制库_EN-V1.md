# 美剧对白机制库 EN-V1

用途：治 AI 写英文对白的七大病——**回合太整齐**（每句完整回应上一句，没有抢话、答非所问、拖半拍）、**人人一个声音**（全员中性受教育美音，去掉人名听不出谁在说）、**把潜台词说出来**（角色宣布自己的情绪，on-the-nose）、**信息倾倒**（用完整段落向已知情的人解释设定）、**没有地位游戏**（人人客气平等，看不出谁能命令谁）、**笑点飘**（有梗但没有 setup／runner／callback 结构）、**行话像百科**（专业语言写成维基词条而不是从业者的口头禅）。

**与中文机制库 V4 的分工**：中文那份治的是称谓、面子、台阶、含蓄——英文没有这套装置。本库治的是 status transaction（地位交易）、turn-taking（回合争夺）、deflection（回避）、register（语域）、comedy architecture（喜剧结构）。两份不重叠，按创作语言选用；写中文但想借美剧手艺时，看每部分末尾的【中文转译】。

**来源与可靠性边界（重要，先读）**：本库**不是语料蒸馏产物**。中文机制库 V4 的每条锚点来自逐集听打台词本并注明出处；本库没有这个条件——所有"情境锚点"是**技法与情境的描述性复述，不含逐字引文**，用于说明机制长什么样，不可当引用使用。可靠性押在机制层：机制说明、生效原理、适用场景与 ❌→✅ 对照均为原创，可直接检验。凡涉及具体作品，只在该技法被公开讨论到近乎常识的程度时提及，且只描述做法不复述台词。要逐字引用请自行核对剧本原文。

**使用方法**：写对白前先查第九部分【场景速查索引】按场景反查机制编号；改稿时先定位缺哪个机制再动笔，不凭感觉润色。学的是机制不是句子。

机制编号：1–10 回合与反应／11–20 地位与权力／21–30 潜台词与回避／31–40 节奏与句法／41–50 声音差异化／51–60 喜剧机制／61–68 类型语域／69–76 结构性台词。

==================================================
一、回合与反应类（治"回合太整齐"）
==================================================

英文对白的真实感有一半在 turn-taking 上。AI 的默认是"问—答—问—答"的完整回合，而真人对话里回合是被抢的、被拖的、被拐走的。

### 1. Answer with a question（不答反问）
- 说明：不回答问题，用一个反问把回答义务推回去。反问本身就暴露了立场和防御姿态。
- 情境锚点：审讯与家庭争吵里最常见的一拍——被问"你去哪了"，回一句"为什么问这个"，问的人立刻变成被审的人。
- 原理：回合的所有权是权力。每一次把问题推回去，都是拒绝进入对方设定的框架。
- 适用：审讯、夫妻争执、下属被上级质询、任何一方有隐瞒的对话。
- ❌ "I was at the office until eight, then I drove home." → ✅ "Why, where were you?"

### 2. Overlap（抢话重叠）
- 说明：不等对方说完就切进去。剧本里用破折号标注被切断处，或用 (overlapping) 提示。
- 情境锚点：Sorkin 式高速对白与 Altman 式群戏的共同底层——重叠不是混乱，是把"谁急、谁强、谁不耐烦"写进节奏。
- 原理：完整让对方说完是礼貌，礼貌是地位表态。抢话把关系温度写进结构，不用形容词。
- 适用：编辑室、手术室、竞选团队、法庭外走廊、家庭饭桌。
- ❌ A: "I think we should consider—" B: "I disagree with that approach." → ✅ A: "I think we should consid—" B: "No."

### 3. The delayed beat（迟半拍）
- 说明：该立刻回答的地方停一拍再答。停顿写进剧本（(beat) 或空行动作），不靠演员自由发挥。
- 情境锚点：Pinter 传统进入电视的产物——Mad Men 一类剧把沉默当台词用，停顿的长度就是答案的重量。
- 原理：立刻回答＝准备好的答案＝可能是假的。迟疑本身携带信息，观众自己读出"他在算"。
- 适用：说谎前、被求婚、被问及死者、被要求表态站队。
- ❌ "No, I never met him." → ✅ (beat) "...No." / (He picks up the glass. Puts it down without drinking.) "I don't think so."

### 4. Answering the question they didn't ask（答错问题）
- 说明：回答一个更容易的、相邻的问题，绕开真正被问的那个。听者听得出被绕，但没有把柄。
- 情境锚点：政治剧与幕僚戏的基本功——记者问"你知不知情"，答"我们已经启动了内部审查"。
- 原理：技术上没撒谎，实质上没回答。观众同时看见回避和回避的技巧，人物的能力和心虚一起立住。
- 适用：新闻发布会、董事会、被配偶盘问、律师会见当事人。
- ❌ "Yes, I knew about it in March." → ✅ "We've opened a full internal review. It'll be thorough."

### 5. Latching onto the last clause（只接后半句）
- 说明：对方说了一整段，只接住最后半句或某个词，前面全部装作没听见。
- 情境锚点：喜剧与拆台角色的常规武器，也是冷漠上司的写法。
- 原理：选择性接收即表态。被忽略的那部分变成房间里的大象，观众替说话的人尴尬。
- 适用：汇报被打断、示弱被无视、告白被轻描淡写接过。
- ❌ "I hear that you're upset, and I want to address your concerns." → ✅ A: "...and I've been here eleven years, I've never missed a deadline, and frankly I think I deserve—" B: "Eleven years. Huh."

### 6. Silence as a turn（沉默当一个回合）
- 说明：把"不说话"写成一个完整回合，配一个可见动作。对方被迫再说一次或改口。
- 情境锚点：审讯室战术的戏剧化——警探不接话，嫌疑人自己往下填。
- 原理：真空必须被填满。沉默把说话的负担压给对方，说得越多漏得越多。
- 适用：审讯、谈判、父母面对撒谎的孩子、老板面对找借口的下属。
- ❌ "I don't believe you. Tell me the truth." → ✅ (He says nothing. Slides the folder an inch closer.) / SUSPECT: "...Okay, look. It wasn't like that."

### 7. Third-party hijack（第三人劫走回合）
- 说明：两人对话里第三人插进来，把话题拐到自己的利益上，原话题当场散架。
- 情境锚点：群戏的生命线——办公室、家庭、编辑部里没有人真的在听主线。
- 原理：真实的多人对话不围绕主题运行，围绕各自利益运行。逻辑上"跑题"，反应上人人精准。
- 适用：三人以上的任何场面，尤其是会议和饭桌。
- ❌ Everyone responds on-topic in turn. → ✅ A: "So the merger closes Friday—" C: (not looking up) "Is anyone taking the car? Because I need the car."

### 8. Echo as challenge（复读当质疑）
- 说明：把对方刚说的一个词原样重复一遍，不加评论。重复即质疑。
- 情境锚点：法庭交叉询问与夫妻争吵共用的一招，重音落在被重复的词上。
- 原理：不反驳，只把词摆出来让它自己听起来荒唐。比说"我不信"更狠，也不给对方反击的把手。
- 适用：交叉询问、揭穿谎言、上级敲打下级。
- ❌ "That's a ridiculous excuse and we both know it." → ✅ "Traffic." (beat) "Traffic."

### 9. Answering before the question lands（提前回答）
- 说明：对方问题还没问完就答，说明他早就知道会被问什么——排练过，或者心虚。
- 情境锚点：被反复质询的角色出现的破绽，也可以写成极度熟悉彼此的两个人。
- 原理：一句抢答同时交代"他预演过这场对话"和"他们有多熟"，不用旁白。
- 适用：说谎、老夫老妻、长期搭档、被同一个问题追问过很多次的人。
- ❌ A: "Where were you last night?" B: "I was home." → ✅ A: "Where were—" B: "Home. I was home. Ask Mrs. Alvarez, she saw me."

### 10. Environmental interrupt（环境打断）
- 说明：关键情绪话被环境事件截断——电话、门铃、孩子哭、微波炉、广播。话永远没说完。
- 情境锚点：情景喜剧与家庭剧共用的节奏器，也是拒绝给观众满足感的手段。
- 原理：生活不给人把话说完的机会。被截断的半句比说完的整句更响，观众自己补完。
- 适用：告白、坦白、道歉、坏消息、任何"终于要说了"的时刻。
- ❌ "I need to tell you something. I've been seeing someone else for the past year." → ✅ "I need to tell you something. I've been—" (The kettle screams. She turns to it. Doesn't turn back.)

**【中文转译】** 1／3／6／8／10 直接可用，中文语境同样成立。2 抢话重叠在中文里要配合语气词（"不是，我意思是——"），否则读起来像排版错误。4 答错问题在中文里常与"官腔"合流，参见中文库机制 37 官腔错位。7 第三人劫走回合对应中文库机制 7 群戏各算各账，两者同源。

==================================================
二、地位与权力类（治"人人客气平等"）
==================================================

英文没有称谓敬语系统，地位靠**交易**表达：谁能打断谁、谁能结束场面、谁把请求说成命令、谁的时间更值钱。Keith Johnstone 的 status 概念进入电视后成为编剧室通用语。

### 11. Name as weapon（直呼其名压人）
- 说明：英文里连名带姓叫人、或在一句话中间插入对方的名字，是施压不是亲昵。
- 情境锚点：老板叫全名、警察叫全名、母亲叫孩子的中间名——都是坏消息的前奏。
- 原理：正常对话不需要一直叫名字。多出来的那个名字就是多出来的压力，观众听得出气压变了。
- 适用：训话、警告、揭穿、母亲发怒。
- ❌ "I'm very disappointed in your behavior." → ✅ "Sit down, Michael." / "Michael James Doherty."

### 12. The order disguised as a question（假征询真命令）
- 说明：用疑问句式下命令。对方没有拒绝的余地，但表面上被"征求"了意见。
- 情境锚点：所有职场剧的权力语法——"Do you want to grab that for me?" 不是问句。
- 原理：地位越高越不用命令句。礼貌形式与强制内容之间的落差，就是权力本身。
- 适用：上下级、医生对护士、资深对新人、丈夫对妻子（写婚姻不平等时）。
- ❌ "Get me the Hollis file immediately." → ✅ "You want to pull the Hollis file for me? Great."

### 13. Weaponized courtesy（谢字当刀）
- 说明：用过度的礼貌表达攻击。"Thank you so much" 说得越完整越冷。
- 情境锚点：职场与上流家庭的常规武器，礼貌的完整度与敌意成正比。
- 原理：熟人之间不用完整礼貌。突然的正式化＝关系降级，等于当众划线。
- 适用：办公室政治、离婚谈判、豪门家庭、同事翻脸。
- ❌ "I'm furious with you and I want you to know it." → ✅ "No, it's fine. Really. Thank you for letting me know. I appreciate it. Truly."

### 14. Who ends the scene（谁结束场面）
- 说明：谁先起身、先挂电话、先走出画面，谁地位高。把"离场权"写进动作里。
- 情境锚点：谈判戏的胜负经常不在台词而在谁先站起来。
- 原理：留下来的人是被留下的。不用一句台词就完成权力宣告。
- 适用：谈判、分手、辞退、审讯结束、董事会。
- ❌ "This meeting is over and I'm in charge here." → ✅ (She stands mid-sentence, while he's still talking, and walks out. He keeps talking for two more words, then stops.)

### 15. Interruption rights（打断权分配）
- 说明：在一场戏里明确谁可以打断谁、谁被打断后只能接受。打断权的分布就是权力地图。
- 情境锚点：群体场面（急诊室、编辑部、内阁会议）的地位结构，全部写在谁敢切谁的话上。
- 原理：观众不需要被告知谁说了算，他们从谁被切断中直接读到。
- 适用：任何三人以上、存在等级的场面。
- ❌ 每个人依次完整发言。 → ✅ 主治医打断所有人；住院医只打断实习医；实习医谁也不敢打断，只在所有人说完后补一句，还被无视。

### 16. Diminutive downgrade（降级称呼）
- 说明：用昵称、缩写、"kid""sport""champ"称呼对方，把成年人降级成孩子。
- 情境锚点：黑帮片与职场剧共用——越亲昵的称呼越是威胁。
- 原理：命名权即定义权。被叫 kid 的人如果接受这个称呼，就接受了这个位置。
- 适用：黑帮、老派上司、家族企业、教练与球员。
- ❌ "You're inexperienced and you should defer to me." → ✅ "Relax, kid." / "You did good, sport. Now sit down."

### 17. Silence as dominance（沉默施压）
- 说明：地位高的一方不解释、不辩护、不填空白，让对方自己说个不停。
- 情境锚点：与机制 6 同源但功能不同——6 是战术，17 是地位常态。
- 原理：需要解释的人是弱势的。不解释本身就是"我不需要你理解"。
- 适用：老板面对辩解、老钱面对新贵、法官面对律师。
- ❌ "I don't need to explain myself to you." → ✅ (Says nothing. Looks at him until he keeps going.)

### 18. "Say that again"（让对方重复）
- 说明：要求对方把刚说的话重复一遍。重复的过程就是对方自我审查和退缩的过程。
- 情境锚点：冲突升级前的最后一格，也常用于父亲对儿子。
- 原理：把说过的话再说一遍，需要比第一次更多的勇气。多数人会在重复时软化——软化即认输。
- 适用：挑衅、家法、黑帮、军队、任何一触即发的时刻。
- ❌ "How dare you speak to me like that." → ✅ "Say it again." (beat) "Go on. Say it exactly like you just said it."

### 19. Answering for someone present（替在场的人回答）
- 说明：有人被问话，另一个人替他答了。被替的人在场、有嘴、但没有说话权。
- 情境锚点：控制型关系的经典外化——丈夫替妻子点菜、母亲替孩子回答医生。
- 原理：不用一句解释就写清了谁被剥夺了什么。被替答的人的沉默（或迟疑）是第二层信息。
- 适用：控制型婚姻、亲子、经纪人与艺人、律师与当事人。
- ❌ "He controls everything she does." → ✅ DOCTOR: "And how have you been sleeping?" (She opens her mouth.) HUSBAND: "She's been fine."

### 20. The false choice（给出选择实为通牒）
- 说明：给两个选项，其中一个明显不可能，形式上是选择，实质上是命令。
- 情境锚点：谈判与勒索的标准语法，也是家长的常用手段。
- 原理：保留对方的"自愿"外壳，让对方自己说出投降的话——比强迫更羞辱。
- 适用：勒索、解雇、离婚协议、黑帮收编。
- ❌ "You have to sign this. You have no choice." → ✅ "You can sign it here, or you can sign it in front of the board on Thursday. Up to you."

**【中文转译】** 12 假征询真命令、14 谁结束场面、15 打断权、17 沉默施压、19 替人回答、20 假选择在中文里完全成立且高频。11 直呼其名在中文对应"从职务称呼切换到全名"，参见中文库机制 9 称谓换挡。13 谢字当刀对应中文的"越客气越生分"，参见中文库机制 60 同话异价。16 降级称呼在中文里走"小张""孩子""你还年轻"这条路。

==================================================
三、潜台词与回避类（治"把心里话说出来"）
==================================================

on-the-nose 是英文编剧室骂人的话：角色说出了自己的感受。规则是——**角色可以知道自己的感受，但不能说出来；观众必须自己看出来。**

### 21. Displacement onto object（转移到物）
- 说明：情绪不落在情绪上，落在手边一个不相干的具体物件上。
- 情境锚点：厨房戏的通用解法——争吵的真正内容是婚姻，说出口的内容是洗碗机。
- 原理：真人在情绪最大时抓最近的东西挡枪。物越小越不重要，压着的情绪越大。
- 适用：婚姻、丧亲、父子、任何不能直说的场合。
- ❌ "I feel like you've stopped caring about this family." → ✅ "You put the pan in the dishwasher again." (beat) "I've asked you. I've asked you so many times."

### 22. Talking about a third party（谈第三方谈自己）
- 说明：借评论一个不在场的人，说自己不敢说的话。双方都知道在说谁。
- 情境锚点：家庭剧与办公室剧共用——"Dave's wife left him because he never asked her anything."
- 原理：第三方是安全距离。听的人可以选择接住或装没听见，两种反应都是信息。
- 适用：婚姻、友谊、同事、亲子。
- ❌ "You never ask me about my day." → ✅ "You know why Dave's marriage ended? Fifteen years and he never once asked her a question. Not one."

### 23. The joke that isn't（说笑话说真话）
- 说明：把真话包在玩笑里说出来，留一条"我开玩笑的"退路。对方笑不笑决定下一拍。
- 情境锚点：英美对白最常用的防御装置，尤其在男性角色之间。
- 原理：幽默是可撤回的告白。观众同时收到内容和说话人的怯懦。
- 适用：告白、辞职威胁、揭穿、兄弟之间。
- ❌ "I'm in love with you and I have been for years." → ✅ "You know, if you'd married me instead, you'd be much happier and only slightly poorer." (She doesn't laugh. He does, too late.)

### 24. Over-specification as avoidance（过度具体）
- 说明：被问到痛处时，答一堆极其精确但完全不相干的细节。
- 情境锚点：创伤叙述的常见写法——问"那天发生了什么"，答的是天气、路线、几点几分。
- 原理：细节是掩体。人在回避核心时会本能地供出周边，观众从"没说的那一块"读到全部。
- 适用：创伤、丧亲、犯罪、被审问。
- ❌ "I don't want to talk about the accident." → ✅ "It was a Tuesday. It had rained earlier, so the road was — I remember the wipers were on intermittent. I'd stopped for gas at the Shell on Route 9, the one with the broken—" (stops)

### 25. Refusing the word（拒绝命名）
- 说明：全程用 it / that / the thing / what happened 指代，从不说出那个词（死、癌症、离婚、他的名字）。
- 情境锚点：丧亲戏与病房戏的核心机制，说出那个词就是承认。
- 原理：命名即接受。回避命名把角色的否认写进语法，一旦终于说出口，那一拍就是转折。
- 适用：丧亲、绝症、离婚、成瘾、失踪的孩子。
- ❌ "Since my son died, I haven't been able to work." → ✅ "Since — since it happened. I haven't really been back." (Later, at the climax:) "Since Danny died."

### 26. Pre-emptive absolution（提前原谅）
- 说明：在对方道歉之前先说"没关系"，用宽恕堵住对话，实际是拒绝谈。
- 情境锚点：礼貌文化里的攻击性写法，说"It's fine"的人从不是 fine。
- 原理：抢先赦免剥夺了对方赎罪的机会，是比指责更彻底的惩罚。
- 适用：婚姻、亲子、朋友背叛之后。
- ❌ "I'm still angry about what you did." → ✅ "Don't. Honestly. It's done, it's fine, I'd rather not." (turns back to the sink)

### 27. Professional register for personal content（借专业语言说私事）
- 说明：用职业语言处理私人情感——医生用诊断说爱，律师用条款说恨。
- 情境锚点：职业剧的高级写法，角色只有一套语言可用，那套语言就是他的牢房。
- 原理：语域错位即人物履历。观众同时看见他想说什么和他为什么说不出来。
- 适用：医生、律师、军人、警察、工程师、任何职业剧。
- ❌ "I love you but I'm afraid of losing you." → ✅ "Statistically you'll outlive me by nine years. I've run it. I've run it more than once."

### 28. Future tense as avoidance（谈未来避现在）
- 说明：现在无法面对，就谈以后——计划、旅行、退休、等孩子长大。计划越具体，现在越糟。
- 情境锚点：绝症戏与破裂婚姻共用，两个人一起假装有未来。
- 原理：未来时是最柔软的谎言。观众知道那个未来不会到来，角色也知道，但谁都不说破。
- 适用：绝症、破裂婚姻、即将被捕、即将分别。
- ❌ "We both know you're dying." → ✅ "When you're through this we'll do the Cape. The house with the porch. You always said the porch."

### 29. The "I'm fine" family（我很好家族）
- 说明：I'm fine / It's nothing / Don't worry about it — 必须配一个拆穿它的可见动作。
- 情境锚点：这是最容易写坏的一句台词：单独出现是废话，配上动作才是机制。
- 原理："I'm fine" 本身不携带信息，它的功能是提供一个让身体去反驳的机会。
- 适用：任何强撑的时刻。
- ❌ "I'm fine." （无动作） → ✅ "I'm fine." (She's been holding the same cup of coffee for eleven minutes. It's cold. She drinks it anyway.)

### 30. The unfinished sentence（说不完的句子）
- 说明：句子起了头就停住，让对方（和观众）自己补完。补什么由观众决定，比写死更狠。
- 情境锚点：离婚、告别、临终戏的收尾常用。
- 原理：观众补的那半句永远比编剧写的更贴他自己。参与即代入。
- 适用：告别、临终、无法道歉、无法挽留。
- ❌ "I should have been a better father to you and I regret it every day." → ✅ "I should have—" (He shakes his head. Picks up his keys.) "Drive safe."

**【中文转译】** 21 转移到物、22 谈第三方、24 过度具体、25 拒绝命名、28 谈未来、30 说不完的句子在中文里全部成立，且与中文库机制 5 答非所问、13 留半句、25 借孩子骂人同源。23 说笑话说真话在中文里更常走"自嘲"而非"俏皮话"。27 借专业语言说私事在中文里对应"用工作话说家事"，参见中文库机制 37 官腔错位。26 提前原谅在中文里常写成"算了，都过去了"，杀伤力相同。

==================================================
四、节奏与句法类（治"死板"）
==================================================

AI 写的英文对白最大的可识别特征是**句子都一样长、都语法完整**。真人说话的句长方差极大，且大量不完整。

### 31. Fragments（碎句）
- 说明：删掉主语、系动词、冠词。"You okay?" 不是 "Are you okay?"。
- 情境锚点：所有当代美剧的默认口语层。
- 原理：完整语法是书面的。删掉的成分越多，关系越近或情况越急。
- 适用：熟人、紧急、疲惫、专业人士之间。
- ❌ "Are you doing all right? You look as though you might be unwell." → ✅ "You okay?" "Mm." "You don't look okay."

### 32. Run-on under pressure（压力下一句到底）
- 说明：紧张、撒谎或恳求时，句子失控地长，靠 and / but / because 串起来，中间不换气。
- 情境锚点：与碎句相反的一极——两者在同一场戏里交替出现才有节奏。
- 原理：话多是心虚的生理表现。长句不是文采，是失控。
- 适用：撒谎、辩解、恳求、崩溃、推销。
- ❌ "I was delayed by traffic. I apologize for my tardiness." → ✅ "Okay so the thing is there was traffic but also I got a call from my sister and she's — it doesn't matter, it's not — I should have called, I know, I know I should have called."

### 33. Rule of three（三拍律）
- 说明：列举、升级、笑点都用三。两个不够成立，四个开始拖。
- 情境锚点：英文修辞的底层节奏，喜剧与演讲共用。
- 原理：三是"形成模式"的最小数量，第三项落地时观众已经在预期它了——所以第三项可以顺势也可以打破。
- 适用：列举、威胁、笑点、演讲、自我介绍。
- ❌ "He's unreliable and dishonest." → ✅ "He's late, he's loud, and he's the best I've got."

### 34. One-word turns（单词回合）
- 说明：整个回合只有一个词。Yeah. No. Sure. Fine. Okay. 用在关系最紧或最松的两端。
- 情境锚点：熟到不用说话，或者冷到不愿说话——同一个 "Fine." 两种意思。
- 原理：单词回合把重量全部推给上下文和动作，是最省也最险的写法。
- 适用：老夫老妻、审讯、决裂后、长期搭档。
- ❌ "Yes, I agree with your assessment of the situation." → ✅ "Yeah."

### 35. Self-interruption（自我打断）
- 说明：说到一半自己改口，用破折号标注。改口的方向暴露他真正在意什么。
- 情境锚点：所有活人都会做的事，AI 从来不做。
- 原理：改口是思维过程的外化。观众看见他先想说什么、又为什么咽回去。
- 适用：撒谎、临时收敛、避免伤人、心虚。
- ❌ "Your mother would have been proud of you." → ✅ "Your mother would've — she'd have had something to say about it, that's for sure."

### 36. Repetition with escalation（重复升级）
- 说明：同一个词或句式重复三次，每次加重。重复不是啰嗦，是压力表。
- 情境锚点：崩溃前的最后一段，也用于逼供。
- 原理：语言在极端情绪下会退化成重复。词汇量下降本身就是情绪指标。
- 适用：崩溃、暴怒、恳求、逼问。
- ❌ "I'm asking you to be honest with me right now." → ✅ "Look at me. Look at me. Look at me."

### 37. The list that runs away（列举失控）
- 说明：开始列举时是理性的，列到后面开始加入不该出现的私人条目，暴露真正在意的东西。
- 情境锚点：争吵中段的经典写法——从事实清单滑向旧账清单。
- 原理：列举的顺序即优先级。最后蹦出来的那一项才是真的。
- 适用：夫妻争吵、辞职、控诉、遗嘱。
- ❌ "You've let me down in many ways over the years." → ✅ "The car, the money, the thing with my mother, the — you didn't come. To the hospital. You didn't come."

### 38. Tag questions（反问句尾）
- 说明：句尾挂 right? / you know? / isn't it? / okay? 索取确认。索取得越频繁，越不确定。
- 情境锚点：不安角色的语音指纹，也是操纵者的诱导手法。
- 原理：一个附加疑问句就把"我需要你同意"写进句法，不用写心理。
- 适用：不安、讨好、推销、操纵、审讯诱导。
- ❌ "This is the correct decision." → ✅ "This is the right call. Right? This is — tell me this is the right call."

### 39. The written pause（把停顿写进剧本）
- 说明：用 (beat) / (a pause) / 独立动作行标注停顿，不指望演员自己找。长停顿必须配动作。
- 情境锚点：Pinter 传统的电视化，停顿的长短是编剧的权力不是演员的。
- 原理：停顿是台词的一部分。写不写停顿，决定同一段台词是紧张还是平淡。
- 适用：所有关键场面。
- ❌ 连续六句对白无停顿标注。 → ✅ "So." (beat) "That's that, then." (He doesn't move. Neither does she. Somewhere a dog barks.) "Yeah."

### 40. Profanity as meter（咒骂当节拍）
- 说明：脏话在英文对白里承担节奏和亲密度功能，不只是攻击。谁对谁说脏话＝关系地图。
- 情境锚点：Deadwood、Succession 一类剧把咒骂密度当语域来用——高频脏话可以是亲密，也可以是阶级标记。
- 原理：脏话是重音符号。它落在哪个词前面，哪个词就被抬高。同时它划分圈内圈外。
- 适用：黑帮、军队、厨房、交易大厅、家族企业。注意目标平台尺度。
- ❌ "That's an extremely bad idea." → ✅ "That is a spectacularly bad idea." （不用脏话时，用意外的修饰语顶替它的节奏功能）

**【中文转译】** 31 碎句、34 单词回合、35 自我打断、36 重复升级、37 列举失控、39 写进停顿在中文里同样成立，参见中文库机制 29 短句点火、33 复读壮胆。32 压力下一句到底对应中文的"急了就絮叨、找补、翻旧账"。33 三拍律在中文里是"三番"，参见骨架 B。38 反问句尾对应中文的"是吧？""你说呢？""对不对"。40 咒骂在中文里的等价物是"骂式亲密"，参见中文库《亮剑》语域机制。

==================================================
五、声音差异化类（治"人人一个声音"）
==================================================

检验标准：**遮住人名，能否听出谁在说话。**做不到就是没有声纹。声纹不是口头禅，是下面六个维度的稳定偏移。

### 41. Sentence-length fingerprint（句长指纹）
- 说明：给每个主要角色定一个默认句长区间，并规定他在压力下是变长还是变短。
- 原理：句长是最容易被观众无意识识别的指纹，也是最容易在改稿中丢失的。
- 适用：所有主要角色，写作前先定。
- ❌ 全员平均 12–15 词。 → ✅ A 默认 3–6 词，压力下更短；B 默认 20+ 词，压力下更长、开始用从句。

### 42. The abstract/concrete axis（抽象具体轴）
- 说明：有的角色只说具体的东西（名词、数字、物件），有的只说抽象的（概念、感受、原则）。
- 原理：这条轴同时携带阶级、教育、职业和世界观信息，一句话就能定位一个人。
- 适用：跨阶级对手戏、专业人士对外行、代际冲突。
- ❌ 两人都说"we need to consider the implications"。 → ✅ A: "It has implications for the entire department." B: "It means Ray loses his truck."

### 43. Avoidance fingerprint（回避方式指纹）
- 说明：每个角色被逼到墙角时的默认反应必须不同：开玩笑／攻击／沉默／过度解释／离开房间／转移到物。
- 原理：人在压力下才露出真正的语言人格。舒适时人人相似，受压时必须分开。
- 适用：写作前为每个主要角色指定一种，全剧不漂移。
- ❌ 全员被逼问时都沉默三秒然后坦白。 → ✅ A 开玩笑；B 反问；C 站起来去倒水；D 攻击提问者的动机。

### 44. Filler-word fingerprint（填充词指纹）
- 说明：Look / Listen / So / I mean / Okay so / Right — 每个角色只用一到两个，不共享。
- 原理：填充词是最廉价也最有效的识别标记，但共享即失效。
- 适用：所有角色，但每人限一到两个，且不能是当下流行语（会过时）。
- ❌ 全员都说 "Look,"。 → ✅ A 只用 "Look,"；B 只用 "So—"；C 从不用填充词（这本身就是指纹）。

### 45. Address habits（称呼习惯）
- 说明：谁叫全名、谁叫姓、谁用昵称、谁从不称呼对方——固定下来，变化时即事件。
- 原理：英文没有敬语，称呼选择就承担了全部关系标定功能。
- 适用：所有关系，尤其是关系变化的临界点。
- ❌ 所有人互相直呼其名。 → ✅ 她全程叫他 "Detective"；第九集叫了一次 "Ray"；第十集又回到 "Detective"。

### 46. Humor type（幽默类型）
- 说明：每个会开玩笑的角色，幽默类型必须不同：自嘲／刻薄／荒诞／双关／不合时宜／冷面。
- 原理：幽默类型是人格的直接投射，也是观众最容易记住的角色标签。
- 适用：群像剧必做。
- ❌ 全员刻薄机智。 → ✅ A 自嘲；B 刻薄；C 完全不好笑但自己觉得好笑；D 只在最不该笑的时候笑。

### 47. Code-switching（语域切换能力）
- 说明：角色能否在不同场合切换语域，本身就是人物信息。能切＝有社会流动性；不能切＝被困住。
- 原理：切换的时机和方向暴露角色认为自己属于哪里、想让谁看见哪个自己。
- 适用：阶级流动、移民、职场新人、双重生活。
- ❌ 角色在家和在法庭说话方式一样。 → ✅ 在法庭上句法完整、用拉丁词根；回到母亲的厨房，句子塌下来，动词开始省略。

### 48. The absent word（缺席的词）
- 说明：为每个主要角色规定一个他从不说的词——"sorry"、"love"、"please"、对方的名字、某个人的名字。
- 原理：缺席比在场更有力。一旦他终于说了那个词，那一拍不需要任何铺垫就是高潮。
- 适用：所有有弧光的角色，尤其是硬汉、控制型父母、创伤角色。
- ❌ 角色随口道歉。 → ✅ 他全季没说过一次 "sorry"；第十集他说了；不需要任何配乐。

### 49. Professional grammar residue（职业语法残留）
- 说明：职业训练会永久改变句法——军人用被动语态卸责、医生用否定式确认、律师限定每一句、警察用时间戳开头。
- 原理：职业不是靠行话表现的，是靠句法表现的。行话可以查，句法骗不了人。
- 适用：所有职业角色，尤其是已经离职的角色（残留最能说明问题）。
- ❌ 前军人角色说话和平民一样。 → ✅ "Weapon was discharged." （不说 "I fired"）

### 50. Regional syntax, not phonetic spelling（地域句法而非口音拼写）
- 说明：地域感靠句法和习语，不靠拼写变形（不写 gonna、ain't 堆砌，不写方言注音）。
- 原理：注音拼写让演员反感、让读者出戏，且经常带侮辱性。句法层的地域感更准也更安全。
- 适用：所有有地域设定的角色。
- ❌ "Ah reckon we oughta git movin'." → ✅ "We might could head out now." （句法层的南方，不动拼写）

**【中文转译】** 41／43／46／48 直接可用，是通用声纹方法。42 抽象具体轴在中文里同样是阶级与教育的分水岭。44 填充词对应中文的"我跟你说啊""不是""哎"。45 称呼习惯在中文里威力更大，直接参见中文库机制 9–11 称谓三条。47 语域切换对应中文的"普通话／方言／职场腔"切换。49 职业语法残留在中文里表现为"公文腔残留""医嘱腔残留"。50 在中文里对应"只提炼句法和语气，方言词只点味不堆砌"。

==================================================
六、喜剧机制类（治"笑点飘、没有结构"）
==================================================

美剧喜剧的笑点不是零散的俏皮话，是**建筑**：setup 在前，runner 贯穿，callback 收束，button 结束场面。

### 51. Setup / Runner / Callback（三段结构）
- 说明：Setup 埋一次（不好笑）；Runner 中段重复两到三次（渐好笑）；Callback 结尾一次（最好笑，且带情感）。
- 原理：笑点的力量来自累积和预期，不来自单句机智。最后一次出现时观众自己完成了笑点。
- 适用：所有喜剧，正剧中的喜剧支线同样适用。
- ❌ 三个不相干的笑话。 → ✅ 第 2 分钟有人提到"他从不喝无咖啡因"；第 12 分钟他坚持要无咖啡因；第 26 分钟葬礼上有人递给他咖啡，他看了一眼，说 "Decaf?"

### 52. The act-out（演出来）
- 说明：笑点用动作和场面完成，不用台词点破。台词只负责点火。
- 原理：可见的荒唐比被描述的荒唐好笑一个数量级，也更容易传播成片段。
- 适用：所有喜剧。与引擎 4"好点子先场面化"同源。
- ❌ "He's terrible at parking." → ✅ (Eleven-point turn. Two of the points are on the curb. He gets out, looks at it, and nods, satisfied.)

### 53. Specific nouns are funnier（具体名词更好笑）
- 说明：把泛称换成具体品牌、型号、地名、数字。具体度和笑点强度正相关。
- 原理：具体名词携带阶级、年代和品味信息，观众在半秒内完成整套判断——判断本身就是笑点。
- 适用：所有喜剧，也适用于正剧的人物塑造。
- ❌ "He drives an old car." → ✅ "He drives a 2003 Sebring. Convertible. The top doesn't go down."

### 54. Escalation in threes（升级三番）
- 说明：同类事件三次，一次比一次过分，第三次必须越过合理边界。
- 原理：与机制 33 同源但用于场面而非句子。前两番建立规则，第三番打破规则。
- 适用：喜剧段落、闹剧、误会戏。参见骨架 B。
- ❌ 同一个笑点重复三次强度相同。 → ✅ 第一次他撒了个小谎；第二次为圆谎伪造了一封邮件；第三次他雇了一个演员冒充自己的哥哥。

### 55. Playing it straight（认真对待荒唐）
- 说明：角色对荒唐处境的反应必须完全认真。谁笑场谁毁戏。
- 原理：观众替角色觉得荒唐。角色一旦自己指出荒唐，观众的发现权被剥夺，笑点消失。
- 适用：所有喜剧，尤其是高概念设定。
- ❌ "This is insane. Do you hear how insane this sounds?" → ✅ (He nods gravely, takes out a notepad.) "Okay. And when did the horse start attending the meetings?"

### 56. The un-cleared misunderstanding（误会不解释）
- 说明：误会一旦成立，禁止任何角色用一句话澄清。必须让每个角色都有不澄清的合理理由。
- 原理：观众能看出误会而角色不能，这个信息差就是喜剧引擎。澄清＝关掉引擎。
- 适用：情景喜剧、浪漫喜剧、身份错位。
- ❌ 第二场就有人说清楚了。 → ✅ A 不澄清因为他享受被高看；B 不澄清因为她以为在帮 A；C 没听懂但不肯承认没听懂。

### 57. The cringe hold（尴尬停留）
- 说明：尴尬发生后不切走，停在那里，比舒适时长多三秒。
- 原理：喜剧的痛感来自时长。切得太早是礼貌，礼貌不好笑。
- 适用：cringe comedy、办公室喜剧、社交灾难。
- ❌ 尴尬后立刻切下一场。 → ✅ (Nobody says anything. He's still holding the cake. Someone's chair creaks. He's still holding the cake.)

### 58. Register mismatch（语域错位）
- 说明：用极正式的语言说极琐碎的事，或用极粗俗的语言说极庄严的事。
- 原理：语域与内容的落差本身就是笑点，且同时交代人物履历。
- 适用：官僚喜剧、家庭喜剧、职场喜剧。
- ❌ "We need to decide who takes out the trash." → ✅ "I'd like to table a motion regarding the ongoing failure of this household's waste-removal protocol."
- 中文同源：见中文库机制 36 大词小用、37 官腔错位。

### 59. Yes-and to absurdity（顺杆归谬）
- 说明：不反驳对方的荒唐前提，顺着它推到底，让它自己崩塌。
- 原理：反驳是辩论，顺着推是喜剧。观众看着一个荒唐前提被认真执行到毁灭。
- 适用：拆台角色、双人喜剧、辩论戏。
- ❌ "That's ridiculous, that would never work." → ✅ "Right. So we steal the ambulance. Then — and I want to make sure I follow — we drive the ambulance to the hospital. Where the ambulances are."

### 60. The button（收尾一击）
- 说明：每场喜剧戏用一个短句或一个动作收尾，收完立刻切。不解释、不升华。
- 原理：切的时机决定笑点是否落地。多一句就是解释笑点，解释即死亡。
- 适用：所有喜剧场面的最后一拍。
- ❌ 笑点后再补两句对话收场。 → ✅ (Long silence.) "...I'll get my coat." CUT TO:

**【中文转译】** 51 三段结构、54 升级三番、55 认真对待荒唐、56 误会不解释、58 语域错位、60 button 在中文里全部成立，且与骨架 B（铺垫→三番→包袱）和引擎 4 第 5 条"笑点来自关系"直接对应。53 具体名词更好笑在中文里同样有效，换成具体品牌车型小区名。57 尴尬停留在竖屏短剧里要压缩时长，否则伤完播。

==================================================
七、类型语域类（治"行话像百科"）
==================================================

规则：**行话不解释。**角色对彼此说行话，观众从上下文和反应里推断。一旦有人解释术语，观众立刻知道这句是说给他们听的。

### 61. Procedural shorthand（程序剧速记）
- 说明：从业者之间用缩写、代号、省略。观众听不懂具体词，但看得懂谁着急、谁在推卸。
- 原理：听不懂反而增加真实感和信任感。观众买的是"我在偷看专业人士工作"。
- 适用：警察、消防、急救、军事、航空。
- ❌ "We need to perform an intubation, which means inserting a tube into his airway." → ✅ "Tube him." "I can't get a view." "Bougie. Now."

### 62. Legal hedging（法律限定）
- 说明：律师的句法特征是给每一句加限定：to my knowledge / at this time / as I understand it。
- 原理：限定语是职业训练的残留，也是免责本能。密度上升＝他在防守。
- 适用：律政剧、公司剧、任何有律师在场的场面。
- ❌ "He didn't do it." → ✅ "My client has not been charged with anything at this time, and I'd caution against characterizing him in any way."

### 63. Clinical understatement（医疗低调陈述）
- 说明：医护对严重情况用极平的措辞，情绪被压进技术语言里。
- 原理：低调陈述与内容严重性的落差，比任何形容词都重。观众自己完成翻译。
- 适用：医疗剧、战争、灾难。
- ❌ "He's going to die, this is a catastrophe." → ✅ "We're not going to be able to fix this." (beat) "Somebody get his daughter."

### 64. Criminal euphemism（犯罪委婉语）
- 说明：黑帮和犯罪角色从不说出行为本身，用日常词替代（take care of / handle / go see him / the thing）。
- 原理：委婉语既是自我保护（怕窃听），也是自我欺骗。两层功能同时成立。
- 适用：黑帮、犯罪、政治阴谋。
- ❌ "I want you to kill him." → ✅ "Go see him." (beat) "Don't come back and tell me about it."

### 65. Political non-answer（政治不回答）
- 说明：幕僚与政客的语言核心是"说满一分钟不承诺任何事"，配合机制 4 答错问题。
- 原理：观众看见的是技巧本身。技巧越娴熟，角色越可怕或越可悲。
- 适用：政治剧、公司公关、危机管理。
- ❌ "Yes, we made a mistake." → ✅ "What I'd say is that the process worked exactly as the process is designed to work, and where it didn't, we'll look at that."

### 66. Military passive（军事被动语态）
- 说明：军事语言用被动语态和名词化卸除个人责任：mistakes were made / the target was serviced。
- 原理：语法本身就是伦理。被动语态里没有主语，也就没有人负责。
- 适用：军事、警察、官僚、任何体制性伤害的题材。
- ❌ "I ordered the strike and civilians died." → ✅ "The package was delivered. There was collateral."

### 67. Tech-optimist register（科技乐观语域）
- 说明：硅谷语言把一切转成使命、规模和动词化名词（we're onboarding、let's socialize this、impact）。
- 原理：这套语言的荒诞不需要点破，直接引用就是讽刺。但要给一个不说这套话的角色作对照。
- 适用：科技剧、创业剧、现代职场讽刺。
- ❌ "We're going to sell more units." → ✅ "We're not selling a product. We're building a movement. At scale."

### 68. Newsroom compression（新闻编辑室压缩）
- 说明：编辑室语言极度压缩，用行话＋时间压力＋否定：no / kill it / we don't have it / two sources or it doesn't run。
- 原理：时间压力写进句法，观众感到 deadline 而不需要看表。
- 适用：新闻剧、直播、任何有硬截止的行业。
- ❌ "I don't think we have enough verification to publish this story yet." → ✅ "Who's your second?" "I'm working on it." "Then you don't have it. Next."

**【中文转译】** 61 行话不解释是通用原则，中文同样适用且同样常被违反。62／65／66 在中文里分别对应"法务限定语""官方表态腔""公文被动"，中文的官僚语法用"有关方面""相关工作已经开展"完成同样的卸责功能。64 犯罪委婉语在中文里走"办了""处理一下""让他消停"。67 科技语域对应中文互联网黑话（对齐、抓手、赋能、闭环），讽刺效果相同。

==================================================
八、结构性台词类（美剧特有的位置功能）
==================================================

美剧的对白承担结构功能：某些句子的作用不是内容，而是它站的位置。

### 69. Cold open hook（冷开场钩子）
- 说明：第一句台词必须制造问题而不是交代情况。不建置、不问候、不铺垫。
- 原理：观众在前 20 秒决定是否继续。第一句的功能是提问，不是回答。
- 适用：每一集的第一场。
- ❌ "Good morning. It's going to be a busy day at the precinct." → ✅ "Whose blood is that?"

### 70. The act break（幕间出点）
- 说明：广告前最后一句必须是新问题、新威胁或认知翻转，不能是情绪落地。
- 原理：幕间是观众流失点。出点的功能是让人不敢走。
- 适用：每个幕末（美剧通常 4–6 幕）。
- ❌ "...and that's why I forgave him." → ✅ "There's just one thing." (beat) "He was already dead when you called me."

### 71. The button（场面收尾）
- 说明：与机制 60 同源，但正剧的 button 是情绪刀不是笑点：一个短句或动作，收完立刻切。
- 原理：场面的最后一拍决定观众带走什么。多说一句就是解释。
- 适用：每场戏的最后一拍。
- ❌ 场面在对话自然结束后又聊了两句。 → ✅ "You knew." (She doesn't deny it. He picks up his coat.) CUT TO:

### 72. The runner（贯穿线）
- 说明：一句台词、一个物件或一个问题在全集重复出现三次以上，每次意义变化。
- 原理：重复建立预期，变化兑现预期。这是单集的隐形结构骨架。
- 适用：单集、单季，尤其群像剧。
- ❌ 无重复元素。 → ✅ 全集有三个人问同一个人 "You eat today?"——第一次是关心，第二次是试探，第三次是他自己问别人。

### 73. The tag（片尾小戏）
- 说明：主线结束后的一小段收尾戏，通常轻、私密、与主线情绪反向。
- 原理：观众需要一个下车的缓冲。tag 的功能是把这一集变成"一段经历"而不是"一个事件"。
- 适用：单元剧、程序剧、喜剧。
- ❌ 高潮结束直接片尾。 → ✅ 两个警探在车里吃三明治，谁也不提刚才发生的事，其中一个说 "You want the pickle?"

### 74. Walk-and-talk delivery（移动中投送信息）
- 说明：需要交代大量信息时，让角色边走边说，并让第三方在途中打断、插话、递文件。
- 原理：移动＋打断把说明性内容变成有压力的动作。观众感到的是节奏，不是讲课。
- 适用：政治剧、医疗剧、任何信息密度高的题材。
- ❌ 两人坐在办公室交代设定三分钟。 → ✅ 穿过三个门、被两个人截住、说到一半有人塞进来一份文件，信息量相同但没有一句像解释。

### 75. "Previously on" selection（前情提要的选择）
- 说明：前情提要选什么，就等于告诉观众本集要考什么。选错等于剧透，选漏等于观众看不懂。
- 原理：这是编剧对观众注意力的直接分配，属于结构决策不属于剪辑。
- 适用：所有连续剧。
- ❌ 把上集所有大事都放进去。 → ✅ 只放三件，其中一件是观众以为不重要的细节——本集它会变成关键。

### 76. Late in, early out（晚进早出）
- 说明：场面从冲突已经开始的地方进入，在结论落地前离开。删掉打招呼和道别。
- 原理：这是美剧场面写作的第一原则。进得晚＝观众要追赶＝注意力被抓住；出得早＝观众自己补完。
- 适用：所有场面。
- ❌ "Hi." "Hey, come in, sit down." "Thanks." "So, what did you want to talk about?" → ✅ "—then why did you call him?" （直接从争吵中段进入）

**【中文转译】** 69 冷开场钩子对应竖屏"前三秒"与横屏"开场白式 hook"，见轨道 T2／T4。70 幕间出点在竖屏里对应"付费点卡点"，在网文里对应"章末尾钩"。71 button 与引擎 7 第 7 条"结尾双收"同源。72 runner 对应中文的"重复一个专属行为"，见引擎 13 第八节。76 晚进早出是通用原则，中文剧本同样适用且同样常被违反。

==================================================
九、场景速查索引（写戏前先按场景反查）
==================================================

- **审讯／盘问**：1 不答反问、3 迟半拍、6 沉默当回合、8 复读当质疑、17 沉默施压、18 让对方重复、24 过度具体、61 程序剧速记
- **夫妻争吵**：1、8、21 转移到物、22 谈第三方、26 提前原谅、36 重复升级、37 列举失控、48 缺席的词
- **上下级／职场**：11 直呼其名、12 假征询真命令、13 谢字当刀、14 谁结束场面、15 打断权、20 假选择、67 科技语域
- **谈判**：14、17、20、59 顺杆归谬、68 新闻编辑室压缩（时间压力写法通用）
- **告白／示爱**：3、10 环境打断、23 说笑话说真话、27 借专业语言说私事、30 说不完的句子
- **告别／临终**：25 拒绝命名、28 谈未来避现在、30、39 写进停顿、73 片尾小戏
- **丧亲／创伤**：21、24、25、29 我很好家族、39
- **群戏／会议／饭桌**：2 抢话重叠、7 第三人劫走回合、15 打断权、37
- **说谎／被揭穿**：3、4 答错问题、9 提前回答、32 压力下一句到底、35 自我打断、38 反问句尾
- **控制型关系**：12、16 降级称呼、19 替人回答、20
- **喜剧场面**：51 三段结构、52 演出来、53 具体名词、54 升级三番、55 认真对待荒唐、56 误会不解释、57 尴尬停留、58 语域错位、59、60 button
- **专业场面（医／警／法／军／新闻）**：61、62 法律限定、63 医疗低调、65 政治不回答、66 军事被动、68
- **犯罪／黑帮**：16、18、40 咒骂当节拍、64 犯罪委婉语
- **阶级／代际冲突**：42 抽象具体轴、47 语域切换、50 地域句法
- **单集结构位**：69 冷开场、70 幕间出点、71 button、72 runner、73 tag、74 walk-and-talk、75 前情提要、76 晚进早出

==================================================
十、声纹建立流程（配合引擎 6 台词自然度四层）
==================================================

写任何主要角色的第一句台词之前，先填这张卡。**没填完，不开写。**

    【EN 声纹卡｜角色ID】
    句长默认区间（41）：
    压力下句长变化方向（41）：
    抽象／具体轴位置（42）：
    受压时的回避方式（43，全剧唯一，不与其他角色重复）：
    填充词（44，限 1–2 个，不与其他角色共享）：
    称呼习惯（45）：对每个主要角色分别怎么叫
    幽默类型（46，如果他会开玩笑）：
    能否语域切换（47）：能／不能，切换时机
    缺席的词（48）：他全剧不说的那个词，以及它在第几集第一次出现
    职业语法残留（49，如适用）：
    地域句法特征（50，如适用；不写注音）：

**四维检验**：任取两个主要角色，比对句长（41）、抽象具体（42）、回避方式（43）、幽默类型（46）。**四维全撞＝人物化不足，重写。** 至少要有两维明显分开。

**遮名测试**：随机抽一页对白，遮住所有角色名，让第三方指认谁在说。指认不出即声纹失败。

==================================================
附：来源、方法与使用边界
==================================================

**建库方法**：本库整理自美剧编剧室通行的手艺共识——场面写作原则（late in / early out、act break、button、runner）、status transaction 传统（源自 Keith Johnstone 的即兴戏剧理论，后成为编剧室通用语）、subtext 与 on-the-nose 的判定惯例、职业语域的句法特征，以及公开剧本格式惯例。机制的抽象与编号、生效原理、适用场景判断、全部 ❌→✅ 对照均为原创。

**与中文机制库 V4 的可靠性差异（务必知悉）**：中文库每条机制附"≤2 句原文＋出处"的逐字锚点，来自逐集听打台词本；**本库没有逐字锚点**。所谓"情境锚点"是技法与情境的**描述性复述，不含任何逐字引文**，仅用于说明该机制在成品中长什么样子。凡提及具体作品，只在该技法已被公开讨论到近乎行业常识的程度时提及，且只描述做法。

**因此**：本库可用于设计与改稿，**不可用作引用来源**。需要逐字例证时，请自行核对剧本原文（IMSDB、Daily Script 等站有公开剧本 PDF，注意其版权状态）。

**版权边界**：不整段复制任何剧集对白进正文；不复制标志性台词组合；机制是通用手艺，不受版权保护，具体台词受保护——学的是前者。

**已知缺口（下一版补）**：本版偏当代美剧（约 2000 年后），对时代剧语域、英式对白（英美差异不小）、单机位与多机位喜剧的语法差异、以及非白人角色群体的语域多样性覆盖不足。第七部分类型语域只覆盖 8 类，尚缺教育、宗教、体育、金融交易、军法等。声纹原型库（中文库有 132 条）本版未建，只给了建立流程。

**版本**：EN-V1，76 个机制／8 类场景语域／10 类场景速查／1 张声纹卡。
