f = open("input.txt")
inp = [int(i.replace("\n", "")) for i in f.readlines()]


def solution():
    for n in range(len(inp)):
        for k in inp:
            if inp[n] + k == 2020:
                return inp[n] * k
        inp.pop(n)

# Runtime complexity: O(n)
def alternative_solution():
    return [i * (2020 - i) for i in inp if (2020 - i) in inp][0]


if __name__ == "__main__":
    result = solution()
    print(result)
