use std::collections::HashSet;

fn main() {
    let groups = load_input("input.txt");
    println!("Part 1: {}", part_one(&groups));
    println!("Part 2: {}", part_two(&groups));
}

fn load_input(filename: &str) -> Vec<String> {
    let file = std::fs::read_to_string(filename)
        .expect("Couldn't open the file.");

    file
        .split("\r\n\r\n")
        .map(|x| x.to_owned())
        .collect()
}

fn part_one(groups: &Vec<String>) -> i32 {
    let mut tot = 0;
    for i in groups {
        let mut set: HashSet<char> = HashSet::new();
        set.extend(i.replace("\r\n", "").chars());
        tot += set.len();
    }
    tot as i32
}

fn part_two(groups: &Vec<String>) -> i32 {
    let mut tot = 0;
    for i in groups {
        let mut chars: HashSet<char> = HashSet::new();
        chars.extend(i.replace("\r\n", "").chars());

        for ch in &chars {
            if i.matches(*ch).count() == i.lines().count() {
                tot += 1
            }
        }
    }
    tot
}



