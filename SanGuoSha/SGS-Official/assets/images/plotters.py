# coding: utf-8

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

def card_num_distribution():
    """Plot `Std-CardNumDistribution.png`."""
    total = np.fromstring('12 14 12 12 13 12 12 12 12 12 12 14 12', sep=' ')

    jb = np.fromstring('0 6 6 6 6 8 9 11 11 10 7 3 2', sep=' ')
    jn = np.fromstring('7 1 6 6 0 3 3 1 1 2 5 9 6', sep=' ')
    zb = np.fromstring('5 7 0 0 7 1 0 0 0 0 0 2 4', sep=' ')

    jb /= total
    jn /= total
    zb /= total

    x = np.arange(1, 14, 1)
    xlabels = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
    plt.plot(x, jb, '*-', color='k', label='基本牌')
    plt.plot(x, jn, 'o-', color='b', label='锦囊牌')
    plt.plot(x, zb, '+-', color='r', label='装备牌')

    plt.legend()
    plt.grid()
    plt.ylim(ymin=-0.01, ymax=1.01)
    ax = plt.gca()
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(1.0))
    plt.xticks(x, xlabels)

    plt.show()


def card_suit_distribution():
    """Plot `Std-CardSuitDistribution.png`."""
    jb = np.fromstring('14 22 20 29', sep=' ')
    jn = np.fromstring('16 15 14 5', sep=' ')
    zb = np.fromstring('10 3 6 7', sep=' ')
    total = np.fromstring('40 40 40 41', sep=' ')

    jb /= total
    jn /= total
    zb /= total

    x = np.arange(1, 5, 1)
    xlabels = '黑桃 红桃 草花 方片'.split()

    plt.bar(x - 0.2, jb, color='k', width=0.2, label='基本牌')
    plt.bar(x, jn, color='b', width=0.2, label='锦囊牌')
    plt.bar(x + 0.2, zb, color='r', width=0.2, label='装备牌')

    plt.legend()
    plt.grid()
    ax = plt.gca()
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(1.0))
    plt.xticks(x, xlabels)

    plt.show()


def main():
    matplotlib.rc('font',**{
        'sans-serif': 'Microsoft YaHei'
    })

    # card_num_distribution()
    card_suit_distribution()


if __name__ == '__main__':
    main()
