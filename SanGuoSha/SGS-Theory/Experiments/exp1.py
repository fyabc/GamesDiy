#! /usr/bin/python
# -*- coding: utf-8 -*-

"""技能摸牌期望计算：关羽【忠义】

【忠义】：出牌阶段限一次，你可以将一张♥手牌交给一名其他角色，然后摸一张牌。本局游戏中，你只能对同一名角色发动【忠义】。

假定所有的♥牌都用来发动【忠义】，且一直能发动【忠义】。

计算前15回合的摸牌数期望。

结果：
    0.827  0.7538 0.7152 0.6946 0.6908
    0.6743 0.6754 0.6711 0.6727 0.6796
    0.6785 0.6758 0.6689 0.666  0.6633

    收敛于2/3；前五回合平均收益为0.7363。
"""

from random import random

import numpy as np

INIT_HAND = 4
EACH_TURN_DRAW = 2
N_TURNS = 15
P_CARD = 0.25
N_EXPERIMENTS = 10000

def get():
    return True if random() < P_CARD else False

def experiment():
    hand = [get() for _ in range(INIT_HAND)]

    result = []

    for _ in range(N_TURNS):
        hand.extend(get() for _ in range(EACH_TURN_DRAW))

        try:
            hand.remove(True)
        except ValueError:
            # target card is not present.
            result.append(0)
        else:
            # Remove one target card, add a new card.
            result.append(1)
            hand.append(get())

    return result


def main():
    experiments = [experiment() for _ in range(N_EXPERIMENTS)]
    experiments = np.array(experiments)

    print(experiments.shape)
    print(experiments.mean(axis=0))


if __name__ == '__main__':
    main()
