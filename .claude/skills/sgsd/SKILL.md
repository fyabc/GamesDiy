---
name: sgsd
description: Design SanGuoSha (三国杀) heroes, cards, and scenes interactively. Use when the user mentions "sgsd", wants to design or edit 三国杀武将、武将技能、卡牌、锦囊、装备、场景牌、扩展包，或需要验证设计格式、运行 sgssim 模拟测试武将强度。也适用于用户讨论三国杀重置计划、提出新机制/新武将想法时主动推荐使用。
---

# SanGuoSha Designer (sgsd)

交互式三国杀武将/卡牌/场景设计工具，集成 sgssim 模拟器进行强度验证。

## Workflow

### 1. 确定设计类型

根据用户需求选择模式：
- **武将设计** — 创建或修改武将（势力、体力、技能）
- **卡牌设计** — 创建或修改游戏牌（锦囊、装备、基本牌）
- **场景设计** — 创建或修改场景牌（全局规则变更）

### 2. 收集设计信息

使用引导式提问收集必要信息。如果用户已提供大部分信息，直接进入下一步。

#### 武将设计引导

| 项目 | 说明 | 必填 |
|------|------|------|
| 武将名 | 武将名称 | 是 |
| 称号 | 如"黄巾天公将军" | 否 |
| 势力 | 汉/魏/蜀/吴/群/晋，可带次势力 | 是 |
| 体力 | 通常 3~5 | 是 |
| 性别 | 男/女 | 否 |
| 技能名及描述 | 1~3 个技能 | 是 |
| 所属扩展 | ext1~ext5 / standard / scene1 等 | 是 |
| SP/神武将 | 是否为 SP 或神武将 | 否 |

#### 卡牌设计引导

| 项目 | 说明 | 必填 |
|------|------|------|
| 牌名 | 卡牌名称 | 是 |
| 类别 | 基本牌/锦囊牌（普通/延时）/装备（武器/防具/坐骑/宝物） | 是 |
| 花色/点数 | ♠/♥/♣/♦，A~K | 是 |
| 效果描述 | 使用/打出时机及效果 | 是 |
| 所属扩展 | 同上 | 是 |

### 3. 生成设计草案

根据收集的信息生成完整的设计草案。

**武将输出格式**（参考 `references/design-rules.md`）：

```markdown
## <武将名> <称号>
<势力> <性别> <体力>体力

【<技能名1>】：<技能描述1>
【<技能名2>】：<技能描述2>
```

**卡牌输出格式**：

```markdown
| 花色\点数 | A | 2 | ... | K |
|-----------|---|---|-----|---|
| ♠ | ... | **<牌名>** | ... | ... |

【<牌名>】：<类别>，<效果描述>
```

### 4. 格式校验

自动检查设计是否符合格式规范：

- 单技能描述 ≤ 70 字（含标点，不含技能名）
- 所有技能描述总和 ≤ 120 字
- 所有技能描述行数 ≤ 6
- 避免复杂多步骤操作和跨回合长时记忆
- 三血武将平均轮收益目标 1.5~2.5，四血 0.75~1.25（参考 `references/design-rules.md`）

如有违规，明确标注并提出修改建议。

### 5. 保存设计

根据用户确认，将设计保存至目标文件：

| 设计类型 | 目标路径 |
|----------|----------|
| 标准版武将 | `SanGuoSha/SGS-RebirthProject/standard.md` |
| 扩展武将 | `SanGuoSha/SGS-RebirthProject/ext-main/ext<N>.md` |
| 扩展卡牌 | `SanGuoSha/SGS-RebirthProject/ext-main/ext<N>.md` |
| 场景牌 | `SanGuoSha/SGS-RebirthProject/scenes/scene<N>.md` |
| 仓库创意 | `SanGuoSha/Warehouse/` 对应文件 |
| 新机制 | `SanGuoSha/Warehouse/warehouse.md` |

### 6. 可选：sgssim 模拟测试

当用户要求或设计为武将时主动提议。详见 `references/simulation.md`。

基本流程：
1. 将武将定义写入 sgssim 扩展（`sgssim/src/sgssim/extensions/standard/heroes.py` 或新建扩展）
2. 配置模拟参数（局数、随机种子、AI 代理类型）
3. 运行 `sgs-sim -n <局数>` 
4. 解析输出，统计胜率、平均轮收益
5. 生成简要报告，与理论值对比

## 设计原则速查

核心原则（详细内容见 `references/design-rules.md`）：

1. **简洁优先** — 技能描述尽量简短，避免冗长操作
2. **面向面杀** — 避免长时记忆、复杂多步骤
3. **强度可控** — 三血 1.5~2.5 收益，四血 0.75~1.25
4. **牌堆比例** — 杀 25%、闪 12.5%、桃 7%、酒 2.7%
5. **扩展独立** — 每个扩展包自带专属武将和特制标准武将

## Reference Files

设计时按需读取以下参考文件：

- `references/design-rules.md` — 完整设计原则、格式规范、编号规则
- `references/card-format.md` — 卡牌格式模板、牌堆统计参考
- `references/simulation.md` — sgssim 集成指南、模拟命令

## 知识库

设计过程中，以下文件作为权威参考，应按需读取：

- `SanGuoSha/SGS-RebirthProject/main.md` — 重置计划总纲
- `SanGuoSha/SGS-RebirthProject/standard.md` — 标准版牌表
- `SanGuoSha/Warehouse/warehouse.md` — 机制/场景仓库
- `SanGuoSha/SGS-Theory/BenifitTheory.ipynb` — 收益理论模型
