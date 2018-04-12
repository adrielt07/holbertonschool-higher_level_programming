#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = 0
    if (len(sys.argv) == 1):
        print("0 arguments.")

    elif (len(sys.argv) == 2):
        print("{} argument:".format(len(sys.argv)-1))
        print("{}".format(sys.argv[1]))

    else:
        print("{} arguments:".format(len(sys.argv)-1))
        for i in sys.argv[1:]:
            a += 1
            print("{:d}: {}".format(a, i))
