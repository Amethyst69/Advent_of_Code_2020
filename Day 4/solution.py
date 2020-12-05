import re


f = open("input.txt")
inp = f.read().split("\n\n")

def part_one():
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    
    valid = 0    
    for passport in inp:
        if all(map(lambda v: v in passport, required)):
            valid += 1
            
    return valid


def part_two():
    valid = 0
    patterns = ["byr:(19[2-9][0-9]|200[0-2])",
                "iyr:(201[0-9]|2020)",
                "eyr:(202[0-9]|2030)",
                "hgt:(?:(?:1[5-8][0-9]|19[0-3])cm|(?:59|6[0-9]|7[0-6])in)",
               r"hcl:(#[a-f0-9]{6})\b",
               r"ecl:(amb|blu|brn|gry|grn|hzl|oth)",
               r"pid:([0-9]{9})\b"]

    for passport in inp:
        for patt in patterns:
            if not re.search(patt, passport):
                break
        else:
            valid += 1
            
    return valid
            
            
if __name__ == '__main__':
    print("Part 1:", part_one())
    print("Part 2:", part_two())













