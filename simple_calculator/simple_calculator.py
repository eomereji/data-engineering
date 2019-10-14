
# simple python calculator program


import argparse


def main():
    parser = argparse.ArgumentParser(description="calculator")
    parser.add_argument('integers', metavar='N', type=int, nargs=2,
                        help='an integer for the accumulator')
    parser.add_argument('--add', action='store_true',
                        help="Adds a set of numbers")
    parser.add_argument('--sub', action='store_true',
                        help="Subtracts a set of numbers")
    parser.add_argument('--multiply', action='store_true',
                        help="Multiplies a set of numbers")
    parser.add_argument('--divide', action='store_true',
                        help="Divides a set of numbers")

    args = parser.parse_args()
    print(calc(args))


def calc(args):
    if args.add:
        return sum(args.integers)
    if args.sub:
        return args.integers[0]-args.integers[1]
    if args.multiply:
        return args.integers[0]*args.integers[1]
    if args.divide:
        return args.integers[0]/args.integers[1]
    else:
        return "You have chosen an invalid opearation"


if __name__ == "__main__":
    main()
