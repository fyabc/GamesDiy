# Simulation Guide — sgssim 集成指南

## 前置条件

sgssim 已安装在 `sgssim/` 目录下，通过 pip editable 模式安装。

CLI 入口：
- `sgs-run` — 启动完整游戏（含 UI）
- `sgs-sim` — 批量模拟

## 快速模拟

```bash
sgs-sim -n 1000 -s 42
```

参数说明：
- `-n <数量>`：模拟局数，默认 1
- `-s <种子>`：随机种子，第 N 局使用 `seed + N`
- `-c <配置>`：指定配置文件路径
- `-l <级别>`：日志级别（debug/info/warning/error/critical）

## 添加新武将到模拟器

### 方法一：修改标准扩展

编辑 `sgssim/src/sgssim/extensions/standard/heroes.py`，按现有格式添加武将定义。

编辑 `sgssim/src/sgssim/extensions/standard/cards.py` 添加专属卡牌。

### 方法二：新建扩展

在 `sgssim/src/sgssim/extensions/` 下新建扩展目录，参考 `standard/` 的结构：

```
extensions/<ext_name>/
├── __init__.py
├── heroes.py
├── cards.py
└── card_list.json  # 可选
```

### 武将定义格式（Python）

参考 `sgssim/src/sgssim/core/hero.py` 中的 `Hero` 类定义，以及 `extensions/standard/heroes.py` 中的实例。

基本结构：
```python
from ...core.hero import Hero
from ...core.skill import Skill

hero_name = Hero(
    name="武将名",
    force="势力",
    gender="男/女",
    max_hp=体力值,
    skills=[skill1, skill2],
)
```

### 技能定义格式

参考 `sgssim/src/sgssim/core/skill.py`。

## 解析模拟结果

`sgs-sim` 的输出包含统计信息。关注以下指标：

1. **各阵营胜率** — 主/忠/反/内 各方胜率
2. **武将使用率** — 被选中的频率
3. **武将胜率** — 该局中存活的概率

### 强度评估

将模拟结果与理论值对比：

| 指标 | 理论值 | 偏差处理 |
|------|--------|----------|
| 三血武将收益 | 1.5~2.5 | 超出则偏强，需削弱 |
| 四血武将收益 | 0.75~1.25 | 同上 |

如果武将过强/过弱，提出具体修改建议：
- 过强：减少摸牌量、增加限制条件、降低伤害
- 过弱：增加可选触发、扩大目标范围、提高收益

## 常见模拟配置

### 标准 8 人局

```bash
sgs-sim -n 100 -s 42 -c <config_with_8_players>
```

### 对比测试（两个版本）

分别用不同配置运行，对比胜率差异。

### 压力测试

```bash
sgs-sim -n 10000 -s 12345
```

大量模拟以获取稳定的统计结果。
