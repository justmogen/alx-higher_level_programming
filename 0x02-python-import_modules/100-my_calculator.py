#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import sub, add, div, mul
    from sys import argv

    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    
    args = {"-": sub, "+": add, "/": div, "*": mul}
    if argv[2] not in list(args.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

    a = int(argv[1])
    b = int(argv[3])
    print("{} {} {} = {}".format(a, argv[2], b, args[argv[2]](a, b)))
