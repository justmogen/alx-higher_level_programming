#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    count = 0
    for n in range(1, len(argv)):
        count = count + int(argv[n])
    print("{}".format(count))
