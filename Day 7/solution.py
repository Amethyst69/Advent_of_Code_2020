import re


def load(filename):
    inp = open(filename).read().split("\n")
    
    bags = {}
    for line in inp:
        bag_name = line.split(" bags contain ")[0]
        bag = re.findall("\d ([a-z]+\s[a-z]+)", line)
        bags.update({bag_name: [*bag]})

    return bags


def part_one(target, bag_rules):
    outer_bags = set()
    
    for key in bag_rules:
        if target in bag_rules[key]:
            outer_bags.add((key))
            outer_bags.update(part_one(key, bag_rules))
            
    if outer_bags:
        return outer_bags

    return set([target])


if __name__ == "__main__":
    bag_rules = load("input.txt")
    print("Part 1:", len(part_one("shiny gold", bag_rules)))
