import sys


def itoBase(nb, base):
    nums = []
    res = []
    b = len(base)
    while (nb != 0):
        nums.append(nb % b)
        nb = nb // b
    nums.reverse()
    for l in nums:
        res.append(str(base[l]))
    return "".join(res)


def main():
    usage = ("\033[1m" + "\033[91m" +
             "Usage:" + " python3 task1.py number base_string" +
             "\033[0m")
    if len(sys.argv) != 3:
        print(usage)
        exit()
    print(itoBase(int(sys.argv[1]), sys.argv[2]))


if __name__ == "__main__":
    main()