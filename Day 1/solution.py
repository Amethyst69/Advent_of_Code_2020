f = open("input.txt")
inp = [int(i.replace("\n", "")) for i in f.readlines()]


def part_one():
    return [i * (2020 - i) for i in inp if (2020 - i) in inp][0]
   
def part_two():
    for n in range(len(inp)):
        for k in inp:
            for v in inp:
                if inp[n] + k + v == 2020:
                    return inp[n] * k * v
        inp.pop(n)


if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:", part_two())
