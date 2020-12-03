f = open('input.txt')
fin = [i.strip() for i in f.readlines()]


def solution(right, down):
    trees = 0
    x_pos = 0
    for i in range(0, len(fin), down):
        line = fin[i]
        
        if line[x_pos % 31] == "#":
            trees += 1
        x_pos += right
            
    return trees


if __name__ == '__main__':
    print("Part 1:", solution(3, 1))

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    part_two = 1
    for r, d in slopes:
        part_two *= solution(r, d)
    print("Part 2:", part_two)
