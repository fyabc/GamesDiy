#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import argparse

from rich.console import Console

from src.core.card import CardType


console = Console()


def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    for ct in CardType:
        console.print(ct)


if __name__ == '__main__':
    main()
