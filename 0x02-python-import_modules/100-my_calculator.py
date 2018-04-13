#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit (1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = [('+', add(a, b)),
                ('-', sub(a, b)),
                ('*', mul(a, b)),
                ('/', div(a, b))]

    for i in operator:
        if i[0] == sys.argv[2]:
            print("{} {} {} = {:d}".format(a, i[0], b, i[1]))
            exit (0)

    print("Unknown operator. Available operators: +, -, * and /")
    exit (1)
