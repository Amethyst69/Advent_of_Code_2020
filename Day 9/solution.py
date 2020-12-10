from itertools import combinations
from collections import deque


def part_one():
    stack = deque(inp[:25], maxlen=25)

    for num in inp[25:]:
        valid = any([pair for pair in combinations(stack, 2) if sum(pair) == num])
        
        if valid:
            stack.append(num)
        else:
            return num


def part_two():
    target = part_one()

    left, right = (0, 1)
    s = inp[left]

    while s != target:
        if s < target:
            s += inp[right]
            right += 1
        if s > target:
            s -= inp[left]
            left += 1

    return min(inp[left:right]) + max(inp[left:right])
        

if __name__ == '__main__':
    inp = [int(i) for i in open("input.txt").read().split("\n")]
    print("Part 1:", part_one())
    print("Part 2:", part_two())













