# 三国杀重置计划

## 基本思路

1. 面向面杀，而不是面向网杀。
2. 由目前的“武将扩展”为主改为“卡牌扩展”为主。
3. 仿照“炉石传说”，将三国杀的游戏牌分为两部分：标准版和游戏牌扩展包。
   1. 标准版（约两副扑克牌）固定不变，类似炉石传说中永不退环境的基本和经典卡牌。
   2. 游戏牌扩展包（约一副扑克牌）各自独立，在游戏时，玩家可自由选择任意个扩展包（一般推荐0~2个）添加到标准版中进行游戏，类似炉石传说中会退环境的各个扩展包。
        - 例：“军争篇”即为一个游戏牌扩展包的例子。
   3. 一个游戏牌扩展包可以附带若干*专属武将*以及若干*特制版标准武将*，当将该扩展包加入游戏时，可以使用相应的专属武将牌，并且使用特制版武将替换标准版中的相应武将牌。
        - 例：假设有一个以游戏牌扩展包，名为“极武”，该扩展包可以附带一个特制版关羽：

        > 势力、性别、体力等不变
        >
        > 【武圣】：你可以将一张红色牌当【杀】使用或打出。
        >
        > 【忠义】：当你使用“极武”扩展包的牌发动【武圣】时，你可以摸一张牌。
   4. 游戏牌扩展包以三国历史上的著名事件为主题，配合相关的游戏牌和武将牌。
        - 例：“官渡之战”扩展包，包含袁绍、特制版曹操以及游戏牌“声东击西”、“奇袭乌巢”等。
4. 使用“场景牌”改变一些游戏规则，场景牌可以在游戏开始时指定。
5. 好处
   1. 不同的游戏牌扩展包可以包含不同的机制，当有新手玩家不熟悉该机制时，可以不添加该扩展包，降低新手入门门槛。
        - 类似炉石传说的退环境机制，保证了环境的不断更新，并且避免武将池无限增大。
   2. 武将牌相对稳定，可以减少玩家记忆武将的开销；由于在多局游戏中，一张特定游戏牌的出现频率远高于一张特定武将牌的出现频率，对游戏牌的熟悉速度会快得多。
   3. 武将牌相对稳定，可以减少“不知名武将完爆关羽张飞”的现象出现。
   4. 游戏牌扩展包对游戏环境的影响远大于武将牌扩展包，可以更好控制游戏环境，并可能导致不同的游戏体验。
        - 例：假设现有5个游戏牌扩展包，若选择任意个加入标准版，则共有32种不同的牌堆；若选择0~2个加入标准版，则共有16种不同的牌堆。
        - 不同的游戏牌扩展包的风格可以差距极大，例如“军争篇”攻击性极强，也可以设计出偏向主忠方的慢速扩展包或极端的“全【闪】”扩展包等。
   5. 游戏牌目前的设计空间比武将牌更大。
        - 可以将“三十六计”中的剩余计谋以及三国中的著名事件做成卡牌。

## 设计原则

1. 尽可能保持技能简洁（可以为此适当牺牲武将强度平衡）
   1. 每个技能描述的字数尽量不超过70（包含标点，不包含技能名）
   2. 所有技能描述的字数总和尽量不超过120（包含标点，不包含技能名）
   3. 所有技能描述的行数总和不超过6（该标准from @紫髯的小乔）
   4. 如果上述两条难以满足，尽量使得该技能可以有一个粗略的“简洁”描述。
      1. 例：初版周泰的【不屈】描述较长，但并不难理解。
   5. 避免复杂的多步骤操作。
   6. 避免长时记忆，尤其避免跨回合记忆。
   7. 非神/仙（左慈、于吉等）/鬼（秦广王蒋歆等）/妖不标。
2. 控制武将整体强度的上限和下限。
   1. 暂定目标：三血武将的平均轮收益为1.5 \~ 2.5，四血武将的平均轮收益为0.75 \~ 1.25（规定1体力的收益为2）
3. 对于知名武将，可以用多张武将牌表现其不同事迹（分布在不同扩展包中）。其中一个为主武将，其余为SP武将。
4. 武将编号规则：**TODO**
   1. 普通武将和神武将按`<势力编码><武将序号>`编号
   2. SP武将按`SP-<该SP武将对应的原始武将编号>`编号
5. 在标准版中，用少量武将代表一个特定的机制，以便于新手熟悉这些机制。
   1. 例：使用曹仁和曹丕代表“翻面”机制。
6. 控制【铁索连环】、【酒】、属性伤害及其他高输出牌的比例，以调控游戏速度（4\~5张铁索连环、3\~5张酒可能是合适的？）。
7. 牌堆设计细节上可以尽量遵循官方牌堆的特征，例如：
   1. 黑桃主要为攻击性锦囊，草花主要为【杀】，红桃主要为增益性锦囊，方片主要为【闪】
   2. 【乐不思蜀】点数为6，【兵粮寸断】点数为4和10，【酒】的点数为3和9（谐音）
   3. 除【南蛮入侵】点数为7和K之外，AOE的点数均为A
   4. 【无懈可击】的点数为A、Q、K
   5. 装备牌的点数为A、2、5、6、Q、K，其中防具牌点数为A和2

## 扩展包计划

### 主线系列

- 总计36扩展（暗合三十六天罡）。
- 第12扩为官渡之战，第24扩为夷陵之战，将三国分为前-中-后三个时期。

1. 黄巾之乱（184 - 185）
    1. 武将：张宝、张梁、张燕、黄巾雷使、刘宏、张让、皇甫嵩、卢植
    2. SP武将：刘宏2、刘备2
    3. 已在标准版或其他扩展中出现的武将：张角
    4. 神武将：张角
2. 董卓入京（189 - 192）
    1. 武将：董卓、李儒、何进、何太后、刘辩、唐姬、王允、蔡邕
    2. SP武将：貂蝉2
    3. 已在标准版或其他扩展中出现的武将：暂无
    4. 神武将：貂蝉
3. 诸侯讨董（190 - 191）
    1. 武将：华雄、徐荣、李肃、牛辅、孔融、韩馥、鲍信、臧洪
    2. SP武将：袁绍2、孙坚2、（诸葛亮2）
    3. 已在标准版或其他扩展中出现的武将：吕布
    4. 神武将：吕布
4. 文和乱武（192 - 195）
    1. 武将：李傕、郭汜、樊稠、张济、杨奉、杨彪、段煨、马腾
    2. SP武将：刘协2、徐晃2
    3. 已在标准版或其他扩展中出现的武将：贾诩
    4. 神武将：贾诩
5. 江东定基（194 - 200）
    1. 武将：太史慈、大乔、小乔、吴景、黄祖、刘繇、严白虎、许贡
    2. SP武将：王朗2
    3. 已在标准版或其他扩展中出现的武将：孙策、周瑜、甘宁
    4. 神武将：孙策
6. 绍平河北（191 - 199）
    1. 武将：麴义、刘虞、TODO
    2. SP武将：TODO
    3. 已在标准版或其他扩展中出现的武将：袁绍、公孙瓒、TODO
    4. 神武将：TODO
7. 迎驾许都（196）
    1. 武将：毛玠、董昭、徐晃、TODO
    2. SP武将：TODO
    3. 已在标准版或其他扩展中出现的武将：荀彧、TODO
    4. 神武将：TODO
8. 宛城之战（197）
    1. 武将：张绣、胡车儿、典韦、曹昂、TODO
    2. SP武将：TODO
    3. 已在标准版或其他扩展中出现的武将：贾诩、TODO
    4. 神武将：TODO
9.  代汉涂高（197 - 199）
    1. 武将：阎象、纪灵、TODO
    2. SP武将：TODO
    3. 已在标准版或其他扩展中出现的武将：袁术、TODO
    4. 神武将：TODO
10. 徐州风云（194 - 198）
    1. 武将：陶谦、曹嵩、张闿、陈宫、高顺、陈登、TODO
    2. SP武将：张辽、TODO
    3. 已在标准版或其他扩展中出现的武将：TODO
    4. 神武将：TODO
11. 衣带诏（199 - 200）
    1. 武将：董承、王子服、伏完、灵雎、吉平、穆顺、TODO
    2. SP武将：TODO
    3. 已在标准版或其他扩展中出现的武将：曹操、刘协、伏皇后
    4. 神武将：无
12. 官渡之战（199 - 200）
    1. 武将：颜良&文丑、沮授、田丰、郭图、于禁、陈琳、许攸、TODO
    2. SP武将：关羽2、张郃2、TODO
    3. 已在标准版或其他扩展中出现的武将：TODO
    4. 神武将：曹操
13. 统一北方（202 - 207）
    1. 武将：程昱、曹彰、袁谭、袁尚、袁熙、审配、蹋顿、公孙康
    2. SP武将：TODO
    3. 已在标准版或其他扩展中出现的武将：张辽、TODO
    4. 神武将：郭嘉
14. 三顾茅庐 & 荆州之战（208）
    1. 武将：蔡夫人、蒯良&蒯越、刘琦、徐庶、TODO
    2. SP武将：诸葛亮3、庞统2
    3. 已在标准版或其他扩展中出现的武将：刘表、TODO
    4. 神武将：张飞、赵云
15. 赤壁之战（208）
    1. 武将：庞统、黄盖、蒋干、蔡瑁&张允、TODO
    2. SP武将：TODO
    3. 已在标准版或其他扩展中出现的武将：TODO
    4. 神武将：周瑜、诸葛亮
16. 南郡之战（208 - 209）
    1. 武将：韩当、文聘、陈矫、牛金、TODO
    2. SP武将：TODO
    3. 已在标准版或其他扩展中出现的武将：周瑜、TODO
    4. 神武将：TODO
17. 借荆州（210 - 217）
    1. 武将：诸葛瑾、TODO
    2. SP武将：孙尚香2、TODO
    3. 已在标准版或其他扩展中出现的武将：鲁肃、TODO
    4. 神武将：TODO
18. 平定关西（211 - 212）
    1. 武将：夏侯渊、韩遂、TODO
    2. SP武将：TODO
    3. 已在标准版或其他扩展中出现的武将：许褚、马超、TODO
    4. 神武将：马超
19. 刘备取蜀（212 - 214）
    1. 武将：张松、简雍、刘璋、张任、TODO
    2. SP武将：法正2、TODO
    3. 已在标准版或其他扩展中出现的武将：刘备、TODO
    4. 神武将：TODO
20. 逍遥津之战（215）
    1. 武将：乐进、李典、凌统、TODO
    2. SP武将：暂无
    3. 已在标准版或其他扩展中出现的武将：TODO
    4. 神武将：张辽
21. 汉中之战（215 - 219）
    1. 武将：法正、张郃、杨修、TODO
    2. SP武将：TODO
    3. 已在标准版或其他扩展中出现的武将：黄忠、张飞、TODO
    4. 神武将：黄忠
22. 襄樊之战（219）
    1. 武将：庞德、糜芳&傅士仁、TODO
    2. SP武将：TODO
    3. 已在标准版或其他扩展中出现的武将：曹仁、吕蒙、TODO
    4. 神武将：关羽
23. 夺嫡之争 & 代汉自立（220）
    1. 武将：曹植、曹节、曹宪&曹华、华歆、崔琰、TODO
    2. SP武将：贾诩2、TODO
    3. 已在标准版或其他扩展中出现的武将：曹丕、TODO
    4. 神武将：曹丕
24. 夷陵之战（221 - 222）
    1. 武将：朱然、孙桓、马良、沙摩柯、傅肜、向宠、黄权、孟达
    2. SP武将：刘备3
    3. 已在标准版或其他扩展中出现的武将：TODO
    4. 神武将：陆逊
25. 七擒孟获（225）
    1. 武将：马谡、马岱、关索、孟获、祝融、鲍三娘、木鹿大王、朵思大王
    2. SP武将：TODO
    3. 已在标准版或其他扩展中出现的武将：诸葛亮、TODO
    4. 神武将：暂无
26. 六出祁山（228 - 234）
    1. 武将：刘禅、魏延、吴懿、杨仪、曹真、郭淮、王朗、郝昭
    2. SP武将：姜维2、马谡2、司马懿2
    3. 已在标准版或其他扩展中出现的武将：诸葛亮、TODO
    4. 神武将：暂无
27. 石亭之战（228）
    1. 武将：周鲂、朱桓、全琮、曹休、贾逵、满宠、TODO
    2. SP武将：陆逊2
    3. 已在标准版或其他扩展中出现的武将：TODO
    4. 神武将：暂无
28. 南鲁党争（242 - 250）
    1. 武将：孙和、孙霸、孙鲁班、孙鲁育、孙登、TODO
    2. SP武将：孙权2
    3. 已在标准版或其他扩展中出现的武将：TODO
    4. 神武将：TODO
29. 高平陵（249）
    1. 武将：曹爽、曹芳、桓范、司马孚、TODO
    2. SP武将：TODO
    3. 已在标准版或其他扩展中出现的武将：TODO
    4. 神武将：司马懿
30. 淮南三叛（251 - 258）
    1. 武将：王淩、毌丘俭、文钦、文鸯、诸葛诞、司马师、王昶、王基
    2. SP武将：TODO
    3. 已在标准版或其他扩展中出现的武将：TODO
    4. 神武将：TODO
31. 东吴变乱（253 - 258）
    1. 武将：孙亮、孙休、孙峻、孙綝、诸葛恪、TODO
    2. SP武将：TODO
    3. 已在标准版或其他扩展中出现的武将：TODO
    4. 神武将：TODO
32. 玉碎九重（260）
    1. 武将：曹髦、王沈、王经、司马昭、贾充、成济&成倅、TODO
    2. SP武将：TODO
    3. 已在标准版或其他扩展中出现的武将：TODO
    4. 神武将：TODO
33. 二士争功（263）
    1. 武将：邓艾、钟会、诸葛瞻、卫瓘、谯周、黄皓、罗宪、TODO
    2. SP武将：刘禅2、姜维3
    3. 已在标准版或其他扩展中出现的武将：TODO
    4. 神武将：暂无
34. 晋代魏祚（265）
    1. 武将：司马炎、杨艳、裴秀、曹奂、TODO
    2. SP武将：暂无
    3. 已在标准版或其他扩展中出现的武将：TODO
    4. 神武将：暂无
35. 西陵之战&交州之战（263 - 272）
    1. 武将：羊祜、陆抗、步阐、薛珝、陶璜、毛炅、TODO
    2. SP武将：TODO
    3. 已在标准版或其他扩展中出现的武将：TODO
    4. 神武将：TODO
36. 重归一统（279 - 280）
    1. 武将：王濬、王浑、司马伷、孙皓、张悌、岑昏、TODO
    2. SP武将：暂无
    3. 已在标准版或其他扩展中出现的武将：TODO
    4. 神武将：暂无

### 次要事件系列

1. 西凉之乱（184 - 187）
   1. 武将：北宫伯玉、王国、韩遂、边章、TODO
   2. SP武将：董卓2、马腾2
   3. 已在标准版或其他扩展中出现的武将：皇甫嵩
   4. 神武将：无
2. 文苑英华
    1. 武将：陈寿、钟繇、张芝、马日磾、TODO
    2. SP武将：TODO
    3. 已在标准版或其他扩展中出现的武将：曹植、TODO
    4. 神武将：TODO
3. 三教九流
   1. 武将：于吉、左慈、马钧、蒲元、张仲景、董奉、刘徽、赵爽
   2. SP武将：TODO
   3. 已在标准版或其他扩展中出现的武将：华佗
   4. 神武将：TODO
4. 威服四夷
   1. 武将：于夫罗、轲比能、彻里吉、曹彰、田豫、关索卫温&诸葛直、卑弥呼、TODO
   2. SP武将：TODO
   3. 已在标准版或其他扩展中出现的武将：无
   4. 神武将：TODO

### 场景（特殊模式）系列

- 新场景一般配合新牌堆，否则默认使用重置计划标准版牌堆。
- 新场景使用武将如无修改，则默认使用重置计划中的版本（相同武将编号）。

1. 黄巾起义（184 - 185）
2. 龙蹙虎狼（192 - 195）
3. 南鲁党争（242 - 250）
4. 魏晋嬗代（249 - 265）
5. TODO

## 其他游戏模式

1. [国战](./hegemony/main.md)

## 参考资料

1. 武将的平衡性设计参考了[这篇文章](https://zhuanlan.zhihu.com/p/41804782)。
2. 部分武将的设计创意来自于这个系列：[1](https://zhuanlan.zhihu.com/p/58644621)、[2](https://zhuanlan.zhihu.com/p/59212688)、[3](https://zhuanlan.zhihu.com/p/58921610)、[4](https://zhuanlan.zhihu.com/p/59131515)、[5](https://zhuanlan.zhihu.com/p/59344207)，在之后的部分不再另加引用。
3. 三国事典：<https://www.rottk.com/>
4. 三国演义全文：<http://www.purepen.com/sgyy/>
5. 三国志全文（带裴松之注）：<http://www.guoxue123.com/shibu/0101/00sgz/>
6. 后汉书全文（带翻译）：<http://www.guoxuemeng.com/guoxue/houhanshu/>
7. 后汉书全文：<http://www.guoxue123.com/shibu/0101/00hhs/index.htm>
8. 资治通鉴全文：<http://www.guoxue123.com/shibu/0101/01zztj/index.htm>
   1. 具体目录：卷五十八（181-187）至卷八十一（280-288）
9.  其他参考资料：
   1. 《孙子兵法》
      1. 原文：<http://www.guoxue123.com/zhibu/0201/00sz/index.htm>
      2. 带翻译：<http://www.guoxuemeng.com/guoxue/sunzibingfa/>
   2. 《英雄记》（作者：王粲）
      1. 百科：<https://baike.baidu.com/item/%E8%8B%B1%E9%9B%84%E8%AE%B0/5827119>
      2. 原文：<http://www.guoxue123.com/biji/han/0000/033.htm>
   3. 《襄阳耆旧记》（作者：习凿齿）
      1. 原文：<http://www.guoxue123.com/biji/qing/0000/043.htm>
   4. 《古今刀剑录》（作者：陶弘景）
      1. 原文：<http://www.guoxue123.com/zhibu/0201/0200/210.htm>
   5. 《续后汉书》（作者：郝经）
   6. 《十七史百将传》（作者：张预）
      1. 原文：<http://www.guoxue123.com/shibu/0201/01bjz/index.htm>
   7. 《季汉辅臣赞》（作者：杨戏）
      1. 原文：见《三国志·蜀书·邓张宗杨传第十五》
   8. [搜韵网-词典功能](https://sou-yun.cn/AllusionsIndex.aspx?sort=People)
   9. 《全三国文》（辑录：严可均）
      1. 原文：<https://www.zhonghuashu.com/wiki/%E5%85%A8%E4%B8%89%E5%9C%8B%E6%96%87>
      2. 原文2：<https://www.zhonghuadiancang.com/lishizhuanji/quansanguowen/>

## 杂项

1. 桌游模拟器(TTS)模组：<https://steamcommunity.com/sharedfiles/filedetails/?id=2789883871>
   1. ID: 2789883871
   2. **TODO**：更新版本
