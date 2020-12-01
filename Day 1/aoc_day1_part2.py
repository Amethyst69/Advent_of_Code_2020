f = open("input.txt")
inp = [int(i.replace("\n", "")) for i in f.readlines()]


def solution():
    for n in range(len(inp)):
        for k in inp:
            for v in inp:
                if inp[n] + k + v == 2020:
                    return inp[n] * k * v
        inp.pop(n)


if __name__ == "__main__":
    result = solution()
    print(result)
