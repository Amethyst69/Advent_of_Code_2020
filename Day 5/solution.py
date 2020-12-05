inp = [i.strip() for i in open("input.txt").readlines()]


def solution():
    data = []

    for bd_pass in inp:
        row, t = (0, 127)
        for i in range(7):
            if bd_pass[i] == "F":
                t = (row + t) // 2
            else:
                row = (row + t + 1) / 2

        col, t = (0, 7)
        for i in range(7, 10):
            if bd_pass[i] == "L":
                t = (col + t) // 2
            else:
                col = (col + t + 1)/2

        data.append(int(row * 8 + col))
        
    return data
    

if __name__ == '__main__':
    data = solution()
    mn, mx = min(data), max(data)
    l = len(data) + 1

    print("Part 1:", mx)
    print("Part 2:", l * (l-1) // 2 + l * mn - sum(data))
