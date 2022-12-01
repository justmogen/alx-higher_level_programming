#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    count = len(argv) - 1  # not including filename while countimng
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for n in range(count):
        print("{}: {}".format(n + 1, argv[n + 1]))
