def part_one():
    return sum(len(set(i.replace('\n', ''))) for i in groups)


def part_two():
    tot = 0
    for group in groups:
        chars = set(group.replace('\n', ''))
        for ch in chars:
            if group.count(ch) == len(group.splitlines()):
                tot += 1
    return tot

        
if __name__ == '__main__':
    groups = open('input.txt').read().split('\n\n')
    print("Part 1:", part_one())
    print("Part 2:", part_two())
