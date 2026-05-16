#!/usr/bin/env python3
"""Create an empty SanGuoSha extension pack template.

Usage:
    python scripts/create_ext_pack.py --name "扩展包N：XXXX" [--cards-only | --heroes-only] [--output FILE]
"""

import argparse
import sys
import io
from pathlib import Path

# Ensure UTF-8 output on Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

CARD_TABLE = """\
### 全牌表

| 花色\\点数 |   A   |   2   |   3   |   4   |   5   |   6   |   7   |   8   |   9   |  10   |   J   |   Q   |   K   |
| :-------: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|     ♠     |       |       |       |       |       |       |       |       |       |       |       |       |       |
|     ♥     |       |       |       |       |       |       |       |       |       |       |       |       |       |
|     ♣     |       |       |       |       |       |       |       |       |       |       |       |       |       |
|     ♦     |       |       |       |       |       |       |       |       |       |       |       |       |       |
"""

GAME_CARDS_SECTION = f"""\
## 游戏牌

{CARD_TABLE}
> 说明：

### 游戏牌说明

1. ![示例锦囊](../assets/images/cards/E4-SA-示例锦囊.png) 【示例锦囊】：锦囊，普通
   出牌阶段，对所有其他角色使用。目标角色依次选择一项：1.交给你一张手牌；2.失去1点体力。

   > 引文："示例引文"
   > 说明设计意图、机制联动或特殊规则。

"""

HEROES_SECTION = """\
## 武将

1. ![示例武将](../assets/images/heroes/E4-示例武将.png) E4-QUN000 示例武将 男 群 4体力/6上限 称号：示例称号
    1. 【技能一】：出牌阶段限一次，你可以弃置一张牌，对一名其他角色造成1点伤害。
    2. 【技能二】：每回合限一次，当一名其他角色对你造成伤害时，你可以进行判定，若结果为黑色，你摸一张牌。

    > 【技能一】探索新机制：说明机制特点。
    > 【技能二】可与其他技能或卡牌联动，体现设计思路。

"""


def build_template(name: str, include_cards: bool, include_heroes: bool) -> str:
    lines = [f"# 三国杀重置计划 {name}", ""]

    if include_cards:
        lines.append("## 新概念\n")
        lines.append("## 特殊玩法说明\n")
        lines.append(GAME_CARDS_SECTION)

    if include_heroes:
        lines.append(HEROES_SECTION)

    lines.extend(["----\n", "----\n"])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Create an empty SanGuoSha extension pack template")
    parser.add_argument("--name", default="扩展包N：XXXX", help="Extension pack name (default: 扩展包N：XXXX)")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--cards-only", action="store_true", help="Generate game cards section only")
    group.add_argument("--heroes-only", action="store_true", help="Generate heroes section only")
    parser.add_argument("--output", "-o", help="Output file path (default: stdout)")
    args = parser.parse_args()

    include_cards = args.cards_only or not (args.cards_only or args.heroes_only)
    include_heroes = args.heroes_only or not (args.cards_only or args.heroes_only)

    content = build_template(args.name, include_cards, include_heroes)

    if args.output:
        Path(args.output).write_text(content, encoding="utf-8")
    else:
        print(content, end="")


if __name__ == "__main__":
    main()
