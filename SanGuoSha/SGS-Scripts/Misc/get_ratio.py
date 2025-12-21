import argparse

def main():
    parser = argparse.ArgumentParser(description='Get ratio.')
    parser.add_argument('counts', nargs='+', type=int)
    parser.add_argument('-t', '--total', type=int, default=164)

    args = parser.parse_args()

    for count in args.counts:
        ratio = count / args.total * 100
        print(f'{ratio:.03f}%')


if __name__ == '__main__':
    main()
