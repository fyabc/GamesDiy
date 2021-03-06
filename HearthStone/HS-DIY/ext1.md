# 自制扩展1

* 扩展类型：纯卡牌扩展
* 对应标准版本：狗头人与女巫森林之间（猛犸年结束）

|MyExtension|Basic  |Common |Rare   |Epic   |Legend |Total  |
|:---------:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|Total      |       |50     |36     |27     |21     |134    |
|Neutral    |       |23     |9      |9      |12     |53     |
|Class      |       |3      |3      |2      |1      |9      |

## 说明

1. 部分卡牌内容或创意（以*标示）来自之前看到的其他DIY设计，但现在找不到出处了。
2. _表示未定的名称，XXX表示未定的效果，self表示该卡牌自身。
3. “永久”牌指“瑟拉金之种”等类似的牌。

## 规定

1. 非传说**任务**牌没有*一定出现在起始手牌*中的限制。
2. 你不能同时挂两个相同的**任务**，类似**奥秘**。
3. “抽牌”默认指从牌库抽牌。

## 版本关键词及机制

* 扩展的揭示
* 非传说**任务**牌
* 法力值与法力水晶相关
* 对面的敌人（卡拉赞象棋机制）

## 卡牌

### 卡牌表示

格式：name \[职业\] \[类型\] \[稀有度\] (\[种族\]) \[数值\] - 描述  // 注释
    > 注释

例子：铁鬃灰熊 中立 随从 基本 野兽 3 3 3 - **嘲讽**  // 基本卡牌
    > 基本卡牌

### 中立

1. 迅猛龙蛋 中立 随从 普通 1 0 2 - **亡语**：若你的法力水晶数不小于3，则召唤两个1/1的迅猛龙。
1. _ 中立 随从 普通 1 1 1 - **战吼**：揭示你的对手牌库中的一张牌，若其法力值消耗不小于5，则获得+2攻击力。
1. _ 中立 随从 普通 2 1 1 - **战吼**：揭示你的对手手牌中的一张随从牌，然后召唤该随从的一个1/1复制。
1. _ 中立 随从 普通 2 1 2 - **亡语**：为你的对手召唤一个0/1的_。
    1. _ 中立 随从 衍生物 1 0 1 - 你每回合使用的第一张随从牌的法力值消耗增加(1)点。
1. _ 中立 随从 普通 2 2 2 - **战吼**：揭示你的牌库中的一张随从牌，使其法力值消耗减少(1)点。
1. _ 中立 随从 普通 2 3 2 - 在你的回合结束时，若你有任何未使用的法力水晶，则获得+1/+1。
1. 卑劣的偷窥者 中立 随从 普通 2 3 2 - **战吼**：揭示你的对手的一张手牌。
1. 水晶窃贼 中立 随从 普通 2 3 2 - **战吼**：若你的对手的法力水晶数比你多，则获得一个空的法力水晶。
1. 蓝腮骑士 中立 随从 普通 鱼人 3 2 1 - **亡语**：召唤一个蓝腮战士。
1. _ 中立 随从 普通 恶魔 3 2 2 - 每当你使用一张随从牌后，召唤一个1/1的小鬼。
1. 食人魔法师学徒 中立 随从 普通 3 2 3 - 在你的对手的回合结束时，将该随从变形成为食人魔法师。
1. _ 中立 随从 普通 3 2 4 - 每当该随从对其他随从造成伤害时，若目标随从的攻击力大于该随从的攻击力，此伤害翻倍。
1. 目标锁定器 中立 随从 普通 机械 3 3 4 - **战吼**：使一个敌方随从获得**嘲讽**。
1. 木制禁卫 中立 随从 普通 4 1 6 - 在你的回合结束时，对该随从对面的敌人造成1点伤害。
    > 与卡拉赞象棋类似的机制
1. _ 中立 随从 普通 4 3 3 - 当你揭示该牌时，获得+2/+2。
1. _ 中立 随从 普通 4 4 3 - **战吼**：为你的英雄恢复等同于你的剩余法力值的生命值。
1. 失控的收割机 中立 随从 普通 机械 4 5 5 - 在每个回合结束时，随机攻击一个随从。
    > 不分敌我
1. _ 中立 随从 普通 5 4 5 - **亡语**：恢复你的两个法力水晶。
1. _ 中立 随从 普通 5 5 5 - **战吼**：揭示双方牌库里的一张法术牌。如果你的法术牌法力值消耗较大，将一个幸运币置入你的手牌。
1. _ 中立 随从 普通 6 6 6 - **战吼**：揭示双方牌库里的一张随从牌。如果你的随从牌法力值消耗较大，则获得**进化**。
1. _ 中立 随从 普通 7 6 6 - **战吼**：对一个随从造成等同于其生命值一半（向下取整）的伤害。
1. _ 中立 随从 普通 龙 8 7 9 - 当你揭示该牌时，恢复你的一个法力水晶。
1. _ 中立 随从 普通 9 9 7 - **亡语**：在本回合中，使一个随机友方随从获得**免疫**。

------

1. _ 中立 随从 稀有 2 1 1 - **战吼**：若你的法力水晶数不小于4，则获得+2/+2。
1. _ 中立 随从 稀有 2 3 2 - 该随从对面的随从获得-1攻击力。
1. _ 中立 随从 稀有 4 3 6 - 所有英雄牌的法力值消耗增加（5）点。
1. _ 中立 随从 稀有 4 5 3 - 在你的回合结束时，揭示你的对手的一张手牌。
1. _ 中立 随从 稀有 5 0 7 - **战吼**：获得等同于该随从对面的随从攻击力之和的攻击力。
1. 铁铸城堡 中立 随从 稀有 5 2 6 - 在你的回合结束时，对该随从对面的敌人造成2点伤害。
1. _ 中立 随从 稀有 5 3 5 - **战吼**：揭示你的牌库中的一张武器牌，使其获得+1耐久度。
1. _ 中立 随从 稀有 6 5 4 - **战吼**：对所有随从造成等同于你的剩余法力值的伤害。
1. _ 中立 随从 稀有 7 6 6 - 在你的回合结束时，若你的剩余法力值大于0，则对所有随从造成2点伤害。

------

1. _ 中立 随从 史诗 1 1 1 - **亡语**：若此时是你对手的回合，则召唤一个_(self)。
1. _ 中立 随从 史诗 2 1 2 - **战吼**：揭示你的牌库中的一张法力值消耗为(7)点的牌，若为法术牌，则抽这张牌。
1. _ 中立 随从 史诗 3 3 3 - **战吼**：若你控制至少一个**任务**，则对一个随从造成3点伤害。
1. _ 中立 随从 史诗 4 2 3 - **战吼**：在你的下回合开始时，对所有角色造成2点伤害。
1. _ 中立 随从 史诗 5 3 5 - **亡语**，将一张1/1的小精灵置于你的对手的牌库顶。
1. _ 中立 随从 史诗 野兽 5 4 3 - **亡语**：**招募**一个_(self)。
1. 战场清扫者 中立 随从 史诗 7 6 4 - 每当一个随从死亡，有50%的几率获得一个随机的战利品。
    > 战利品：

    1. 劣质的胸甲 中立 法术 衍生物 1 - 获得10点护甲值。在你的下回合开始时，摧毁你的所有护甲。
    1. 失灵的助手 中立 随从 衍生物 机械 3 2 5 - 在你控制该随从攻击后，若目标仍存活，则会再自动攻击一次相同目标。
    1. 破旧的手斧 中立 武器 衍生物 4 3 1 - **亡语**：若该武器至少攻击并消灭了一个随从，则将该武器移回你的手牌。
    1. 黯淡的灵符 中立 法术 衍生物 0 - 在本回合中，获得5个法力水晶。随机弃两张牌。
1. 钻石皇后 中立 随从 史诗 8 4 6 - 在你的回合结束时，对该随从对面的敌人造成4点伤害。
1. 水晶巨人 中立 随从 史诗 元素 12 8 8 - 本局对战中，在你的每个回合结束时，你每有一个未使用的法力水晶，该牌的法力值消耗便减少(1)点。

------

1. _ 中立 随从 传说 2 3 2 - **战吼**：将你的牌库中的牌按法力值消耗递增排序。
    > 说明：法力值相同的牌顺序随机
2. _ 中立 随从 传说 3 2 2 - **战吼**：将你手牌中任意数量的牌与牌库中等量的牌交换。
    > 过程与对战开始时的换牌完全一致，即进行一次换牌
3. “探索者”布莱恩 中立 随从 传说 4 4 4 - 每当你**发现**一张牌后，将该次**发现**的另一个随机选项置入你的手牌。
4. _ 中立 随从 传说 4 3 5 - 当你抽牌时，优先抽法力值消耗等同于你当前剩余法力值的牌。
    > 在牌库有符合条件的牌的情况下才生效，否则正常抽牌
5. 侏儒大师_ 中立 随从 传说 5 3 5 - 每当有玩家使用一张**史诗**或**传说**随从牌时，使该随从变形成为1/1的小鸡。
6. _ 中立 随从 传说 6 5 6 - 每当你揭示你的牌库里的一张随从牌时，召唤一个该随从的1/1复制。
1. _ 中立 随从 传说 6 6 3 - **战吼**：抽数量等同于你的剩余法力值的牌（至多五张）。
1. _ 中立 随从 传说 7 4 6 - 每当你的其他随从死亡时，若该随从具有种族，随机将一张与该随从种族相同的随从置入你的手牌。
2. _ 中立 随从 传说 7 6 6 - **战吼**：**冻结**所有随从。若有随从已被**冻结**，则改为将其消灭。
3. _ 中立 随从 传说 8 6 7 - 所有敌方随从受到的所有伤害翻倍。
4. 骸骨奈法利安 中立 随从 传说 龙 9 8 8 - **战吼**：对所有其他随从造成2点伤害。当你揭示该牌时，触发其**战吼**效果。
5. 猛犸之王 中立 随从 传说 野兽 10 6 6 - **嘲讽**，**战吼**：**发现**一张**任务**牌、死亡骑士英雄牌或**传说**武器牌。
    > 猛犸年的总结？

### 德鲁伊

1. _ 德鲁伊 随从 普通 2 2 1 - **战吼**：若你的法力水晶数不小于3，则获得一个空的法力水晶。
1. 树人施法者 德鲁伊 随从 普通 5 4 4 - **战吼**：将一张“激活”置入你的手牌。
1. 根须缠绕 德鲁伊 法术 普通 1 - 使一个随从获得**嘲讽**和“无法攻击”。

------

1. _ 德鲁伊 随从 稀有 3 2 4 - 你的英雄在你的回合获得+2攻击力。
1. 丛林德鲁伊 德鲁伊 随从 稀有 6 6 5 - **嘲讽**，**战吼**：使一个随从获得**嘲讽**和“无法攻击”。
1. _ 德鲁伊 法术 稀有 4 - **沉默**一个随从。然后如果你有十个法力水晶，消灭该随从。

------

1. _ 德鲁伊 法术 史诗 3 - 抽四张牌。在本回合结束时，随机将两张手牌洗回你的牌库。
1. _ 德鲁伊 法术 史诗 9 - **招募**一个随从。在你的回合开始时，该牌的法力值消耗减少(1)点。

------

1. _ 德鲁伊 随从 传说 7 6 7 - **战吼**：你的对手在其下个回合使用一张牌后，使你的对手的剩余法力值变为(0)点。

### 法师

1. _ 法师 随从 普通 1 1 2 - **亡语**：揭示双方牌库中法力值消耗最高的一张法术牌。
1. 烈焰药水 法师 法术 普通 4 - 造成3点伤害，将一张“烈焰喷涌”置入你的手牌。
1. _ 法师 法术 普通 6 - 造成4点伤害。在你的回合开始时，该牌的法力值消耗减少(1)点。

------

1. _ 法师 随从 稀有 4 4 3 - **战吼**：揭示你的对手牌库中的一张法术牌，将其变为“冰封秘典”。
1. 法力幻影 法师 随从 稀有 5 5 5 - **战吼**：将一张_洗入你的牌库。
    1. _ 法师 法术 衍生物 7 - 召唤两个法力幻影。当你揭示该牌时，召唤一个法力幻影。
1. 法术复制 法师 法术 稀有 3 - **任务**：施放两个法术。**奖励**：将这两张法术牌的复制置入你的手牌。

------

1. _ 法师 随从 史诗 5 4 4 - **战吼**：为你的对手召唤一个寒冰元素。
    1. 寒冰元素 法师 随从 衍生物 元素 3 0 3 - 在你的回合开始时，随机**冻结**一个友方角色。
1. _ 法师 法术 史诗 6 - 将所有友方元素的攻击力和生命值变为5。

------

1. _ 法师 武器 传说 3 0 3 - 当你的英雄受到致命伤害时，防止此伤害，该武器失去1点耐久度。

### 圣骑士

1. _ 圣骑士 随从 普通 1 1 1 - **亡语**：随机将一张棋子牌置入你的手牌。
    > 所有棋子牌：
    > 木制禁卫
    > 铁铸城堡
    > 玛瑙主教
    > 象牙骑士
    > 钻石皇后
2. 水晶充能 圣骑士 法术 普通 1 - **奥秘**：在你的对手的回合结束时，若其有未用完的法力水晶，则召唤一个2/2并具有**圣盾**的护盾机器人。
3. 缩小术 圣骑士 法术 普通 2 - 使一个随从获得-2/-2。

------

1. _ 圣骑士 随从 稀有 2 2 2 - **战吼**：选择一个随从，若该随从的法力值消耗小于你的剩余法力值，则将其消灭。
1. _ 圣骑士 随从 稀有 6 1 3 - **冲锋**，**战吼**：揭示你的牌库中的一张牌，获得等同于该牌法力值消耗的攻击力。
1. _ 圣骑士 法术 稀有 1 - 揭示你的手牌中的一张随从牌，并使其获得**圣盾**。

------

1. _ 圣骑士 法术 史诗 5 - 消灭场上所有攻击力最高的随从。
2. 命令之锤 圣骑士 武器 史诗 5 2 3 - 在你的英雄攻击一个敌方随从后，使所有友方随从攻击相同的目标。*（不占用这些随从的攻击次数）*

------

1. _ 圣骑士 随从 传说 4 3 3 - **战吼**：将你手牌中一张随机随从牌的攻击力、生命值和法力值消耗变为原来的一半（*向上取整*）。

### 猎人

1. _ 猎人 随从 普通 野兽 4 4 4 - **战吼**，**亡语**：当前回合角色抽一张牌。
1. _ 猎人 随从 普通 野兽 5 5 3 - **亡语**：抽一张牌，对敌方英雄造成等同于该牌法力值消耗的伤害。
1. _ 猎人 法术 普通 1 - **任务**：**招募**三个野兽。**奖励**：_。
    > 奖励牌：

    1. _ 猎人 武器 衍生物 2 1 4 - 每当你**招募**一个随从，使其获得+2/+2，该武器失去1点耐久度。

------

1. _ 猎人 随从 稀有 7 6 6 - **亡语**：使一个随机友方野兽获得+2/+2。当你揭示该牌时，触发其**亡语**效果。
1. 狂犬注射 猎人 法术 稀有 3 - 选择一个友方随从，使其获得+4生命值。然后该随从攻击一个随机敌方随从，重复攻击三次。
    > 三次攻击的目标可以不一样
1. _ 猎人 武器 稀有 3 3 2 - **战吼**：揭示你的牌库中法力值消耗最高的随从牌。若该随从的法力值消耗不小于10，获得+1耐久度。

------

1. _ 猎人 法术 史诗 3 - **任务**：使用两张具有**亡语**的随从牌。**奖励**：对所有敌方随从造成2点伤害。
1. _ 猎人 武器 史诗 3 2 2 - **战吼**：选择一个随从，该随从受到的所有伤害翻倍。

------

1. _ 猎人 随从 传说 6 5 7 - 每当该随从受到伤害后，该随从获得**免疫**直到当前回合结束。

### 术士

1. _ 术士 随从 普通 3 3 2 - 当你弃掉一张牌或受到来自你的卡牌的伤害后，将该随从从你的手牌置入战场。
1. _ 术士 随从 普通 恶魔 6 5 7 - **嘲讽**，**战吼**：发现你的牌库中的一张随从牌，抽这张牌，然后弃掉它。
1. _ 术士 法术 普通 3 - 在本回合中，使你使用的下一张法术牌具有**吸血**。
    > 过强？

------

1. 游荡的灵魂 术士 随从 稀有 2 2 1 - **亡语**：使一个随机友方随从获得“**亡语**：召唤一个游荡的灵魂。”。
1. _ 术士 随从 史诗 3 2 2 - **战吼**：**发现**一张你在本局对战中弃掉的牌。
1. 狂热药水 术士 法术 稀有 0 - 摧毁你的一个法力水晶，然后仅在本回合中，获得三个法力水晶。

------

1. _ 术士 随从 史诗 4 2 6 - 防止你施放的法术对友方角色造成的所有伤害。
1. _ 术士 法术 史诗 5 - 选择一个随从，消灭所有与该随从同名的随从。

------

1. _ 术士 随从 传说 8 4 8 - **嘲讽**，**亡语**：揭示你的对手牌库里的一张牌，若为随从牌，则将其移除。重复三次。

### 战士

1. _ 战士 随从 普通 4 3 5 - **嘲讽**，当该随从受到伤害时，揭示你的手牌中的一张随从牌，并使其获得+1/+1。
    > 获得+1/+1的是被揭示的随从牌
1. _ 战士 随从 普通 7 5 5 - 你每有1点护甲值，该随从的法力值消耗减少(1)点。
1. 专注打击 战士 法术 普通 2 - 对一个随从造成3点伤害。若该随从仍然存活，则恢复你的一个法力水晶。

------

1. _ 战士 随从 稀有 2 3 2 - **战吼**：选择一个友方随从，摧毁你所有的护甲，使该随从获得等量的生命值。
1. _ 战士 法术 稀有 4 - 揭示你的手牌中的一张龙牌，对一个随从造成等同于该牌法力值消耗的伤害。
1. _ 战士 武器 稀有 3 1 2 - 每当你召唤一个攻击力不大于5的随从，将该武器的攻击力变为该随从的攻击力。

------

1. _ 战士 法术 史诗 6 - 消灭一个随从，然后对所有其他随从造成等同于你的剩余法力值的伤害。
1. _ 战士 武器 史诗 5 2 2 - 在你的英雄攻击后，施放一张“命令怒吼”。

------

1. _ 战士 随从 传说 10 5 5 - **战吼**：**招募**一个随从。若你的对手拥有的随从更多，则重复此战吼效果。

### 潜行者

1. _ 潜行者 随从 普通 5 4 4 - 在本回合中，你每使用一张牌，该牌的法力值消耗减少(1)点。
1. _ 潜行者 法术 普通 2 - **奥秘**：当你的对手抽到一张法术牌时，揭示此牌，并使其法力值消耗增加(2)点。
1. _ 潜行者 法术 普通 2 - 选择一个友方随从，对与该随从相对的敌人造成等同于该随从攻击力的伤害。

------

1. _ 潜行者 随从 稀有 海盗 3 3 3 - **战吼**：在本回合中，获得等同于你上回合未使用的法力水晶数的法力水晶。
1. _ 潜行者 随从 稀有 5 5 4 - **亡语**：将一张你在本局对战中施放过的法力值消耗为(1)点的法术置入你的手牌。
1. _ 潜行者 法术 稀有 2 - **发现**一张具有**连击**的牌。**连击**：使该牌的法力值消耗减少(1)点。

------

1. _ 潜行者 法术 史诗 3 - 抽若干张牌，直到你抽到的牌的法力值消耗之和大于(5)点。
1. _ 潜行者 武器 史诗 4 3 2 - 每当该武器消灭一个随从，抽一张法力值消耗等同于该随从法力值消耗的牌。

------

1. 新的冒险 潜行者 法术 传说 1 - **任务**：**发现**七张牌。**奖励**：探险者归来。
    1. 探险者归来 法术 衍生物 5 - 将雷诺·杰克逊、布莱恩·铜须、芬利·莫格顿爵士、伊莉斯·逐星置入你的手牌，这些牌的法力值消耗减少(2)点。

### 牧师

1. _ 牧师 随从 普通 元素 3 2 5 - **沉默**所有受到该随从伤害的随从。
1. _ 牧师 随从 普通 7 3 5 - **亡语**：**招募**一条龙。
1. _ 牧师 法术 普通 5 - 揭示你的牌库里的一张随从牌，触发其亡语效果，重复两次。

------

1. _ 牧师 随从 稀有 2 2 2 - **战吼**：揭示你的对手牌库中的一张牌，复制该牌并置入你的手牌。
1. _ 牧师 随从 稀有 龙 4 5 3 - 在你的回合结束时，若你有任何未用完的法力水晶，则获得+3生命值。
1. 净化药水 牧师 法术 稀有 5 - **沉默**所有敌方随从，然后对所有敌方随从造成2点伤害。

------

1. _ 牧师 随从 史诗 7 4 4 - **战吼**：随机召唤两个本局对战中被移除的随从。
    > 指的是因爆牌、魔能机甲等被移除的随从牌（直接从牌库移除）。
1. _ 牧师 法术 史诗 8 - 将一个随从移回你的手牌。

------

1. _ 牧师 法术 传说 1 - **任务**：使用来自五个不同系列的卡牌。**奖励**：_。
    > 说明：例如使用基础、标准、安戈洛、冰封王座、狗头人卡牌各一张
    > 奖励牌：

    1. _ 牧师 法术 衍生物 5 - 本局对战中，你的所有与你使用的上一张牌系列不同的牌的法力值消耗减少(1)点。
    > 奖励牌说明：
    > 若你使用的上一张牌为基础牌，则你手牌中的基础牌费用不变，其余牌法力值消耗均减少(1)点。
    > 其余类推。

### 萨满

> TODO: 以2/3嘲讽幽灵狼和2/2风怒元素为泛用衍生物，类似贼的刀瓣，德的1/5嘲讽和1/2剧毒，中立的烈焰元素

1. _ 萨满 随从 普通 元素 2 2 2 - **风怒**，**战吼**：将一张2/2且具有**风怒**的XX置入你的手牌。  
    > XX 萨满 随从 衍生物 元素 2 2 2 - **风怒**
1. _ 萨满 随从 普通 7 4 8 - 每当你使用一张具有**过载**的牌，便召唤一个2/3并具有**嘲讽**的幽灵狼。
1. _ 萨满 法术 普通 2 - 选择一个随从，在该随从的两边各召唤一个虚弱图腾。
    1. 虚弱图腾：萨满 随从 衍生物 图腾 2 0 3 - 相邻的随从获得-1攻击力。

------

1. _ 萨满 随从 稀有 2 2 3 - **战吼**：本回合中，使一个友方图腾获得+3攻击力。**过载**：(1)。
1. _ 萨满 法术 稀有 7 - 随机召唤一个法力值消耗为(7)点的随从。当你揭示这张牌时，随机召唤一个法力值消耗为(3)点的随从。
1. _ 萨满 武器 稀有 4 4 2 - 在你的英雄攻击后，在本回合中，具有**法术伤害+1**。

------

1. _ 萨满 随从 史诗 6 4 5 - **战吼**：使一个友方随从变形成为法力值消耗增加(1)点的随机随从。本局对战中，你每揭示过一张牌，便重复一次。
1. _ 萨满 法术 史诗 1 - 消耗你所有的法力值，使你的对手**过载**等量的法力水晶。

------

1. 石母瑟拉塞恩 萨满 随从 传说 元素 7 6 6 - **嘲讽**，**亡语**：进入大地状态。
    1. 大地状态 萨满 永久 衍生物 - 在你的第三个回合开始时苏醒，变为石母瑟拉塞恩。
    > 说明：“大地状态”类似于“瑟拉金之种”。
    > “大地状态”在经历三个“你的回合开始”事件后苏醒。
