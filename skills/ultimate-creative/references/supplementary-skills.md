# 补充方法的使用边界

原解析库是核心；以下是旧版构建时实际读取并提炼的方法来源。终极创意只保留适用于选题、角色与大纲的部分，不调用这些 Skill 的正文生成或生产流程。

| 来源 | 在创意开发中保留 | 本版退出的内容 |
|---|---|---|
| baokuan-juben-skills | 具体目标、人物介绍、主支线、连续性、阶段回报与钩子回收、按严重程度修复 | 正式场号/动作/对白合同、固定60集/场数/秒数、正文导出 |
| wanwusheng-cinematic-drama | 命题通过选择落地、生活入口、道具表现规则、欲望—阻力—选择—结果、高潮代价 | 固定美术与时长、成片工作流、分镜与资产、API调用 |
| screenplay-humanizer-cn | 目标与筹码、知情边界、关系中的说话策略、潜台词、特色的可见载体、先因果后措辞 | 分场修订、整段对白教学戏、固定节拍与评分档位、扫描器与AI作者判定 |

用户重复提及 wanwusheng-cinematic-drama 按同一来源处理，不臆造第三套参考。发生冲突时先满足当前用户与项目锁定项，再取适用的解析事实与明确标注的创作推导。不要求其它参考 Skill 已安装，不替用户自动启动后续写作。

## 历史读取记录

2026-10-03旧版读取：
- `/Users/yubowen/.codex/skills/baokuan-juben-skills/SKILL.md` 与其 `episode-engine.md`、`dialogue-revision.md`、`formal-word-template.md`、`script-review-rubric.md`。
- `/Users/yubowen/.codex/skills/wanwusheng-cinematic-drama/SKILL.md` 与其 `story-and-screenplay.md`。

2026-10-09旧版集成时读取 `/Users/yubowen/.codex/skills/screenplay-humanizer-cn/SKILL.md` 与 `humanization-rubric.md`、`revision-workflow.md`。本次重构在已集成方法上改为 [人物创意设计](humanization.md)，删除正文教学戏；原参考 Skill 不改。这里只记录既有来源，不声称本轮重新执行所有来源 Skill，也不把补充编辑方法算作解析库新增统计。
