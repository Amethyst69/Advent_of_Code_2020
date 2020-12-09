def part_one():
    acc = 0
    cache = []

    i = 0
    while i not in cache:
        cache.append(i)
        
        instr, value = operations[i]
        if instr == "acc":
            acc += int(value)
        elif instr == "jmp":
            i += int(value)
            continue          
        i += 1
        
    return acc


def part_two():
    for n in range(len(operations)):
        acc = 0
        cache = []
        
        i = 0
        while i >= 0 and i < len(operations):
            if i in cache:
                res = None
                break
            
            cache.append(i)
            
            instr, value = operations[i]

            if i == n:
                instr = {'jmp': 'nop', 'nop': 'jmp'}.get(instr, instr)

            if instr == 'acc':
                acc += int(value)

            elif instr == 'jmp':
                i += int(value)
                continue
            i += 1
            
            res = acc

        if res:
            return res


if __name__ == '__main__':
    fin = open("input.txt").read().split("\n")
    operations = [op.split() for op in fin]

    print("Part 1:", part_one())
    print("Part 2:", part_two())
