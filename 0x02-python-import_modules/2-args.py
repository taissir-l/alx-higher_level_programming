#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    leng = len(sys.argv) - 1
    if leng == 0:
        print("0 arguments.")
    elif leng == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(leng))
    for i in range(leng):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
