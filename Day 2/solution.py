from re import search

f = open('input.txt')
fin = [i.strip() for i in f.readlines()]


def part_one():
    valid = 0
    for line in fin:
        data = search(r'^(\d+)-(\d+) ([a-z]): ([a-z]+)$', line)

        rng = range(int(data.group(1)), int(data.group(2)) + 1)
        lt = data.group(3)
        password = data.group(4)

        if password.count(lt) in rng:
            valid += 1
            
    return valid


def part_two():
    valid = 0
    for line in fin:
        data = search('(\d+)-(\d+) ([a-z]): ([a-z]+)', line)

        a, b = int(data.group(1)), int(data.group(2))
        lt = data.group(3)
        password = data.group(4)
        
        if (password[a-1] == lt) ^ (password[b-1] == lt):
            valid += 1
            
    return valid


if __name__ == '__main__':
    print("Part 1:", part_one())
    print("Part 2:", part_two())








        
