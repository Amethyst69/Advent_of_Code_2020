def part_one(adapters):
    effective = 0
    t, o = (0, 0)
    
    while adapters:
        if effective + 1 in adapters:
            effective += 1
            o += 1
        elif effective + 3 in adapters:
            effective += 3
            t += 1
        adapters.remove(effective)

    return t * o


def part_two(adapters):
    adapters.append(0)
    adapters.sort()

    paths = [0] * (max(adapters) + 1)
    paths[0] = 1

    for i in range(1, max(adapters) + 1):
        for j in range(1, 4):
            if i - j in adapters:
                paths[i] += paths[i - j]

    return paths[-1]
    

if __name__ == '__main__':
    inp = [int(i) for i in open("input.txt").read().split("\n")]
    inp.append(max(inp)+3)
    
    print("Part 1:", part_one(inp.copy()))
    print("Part 2:", part_two(inp.copy()))
