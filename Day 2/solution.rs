use regex::Regex;

fn main() {
    println!("Part 1: {}", part_one());
    println!("Part 2: {}", part_two())
}

fn load_input() -> Vec<String> {
    let file = std::fs::read_to_string("input.txt")
        .expect("Couldn't open the file");

    file
        .lines()
        .map(|s| s.to_owned())
        .collect::<Vec<String>>()
}

fn part_one() -> i32 {
    let inp = load_input();
    let re = Regex::new(r"(\d+)-(\d+) ([a-z]): ([a-z]+)").unwrap();

    let mut count = 0;
    for line in inp {
        let caps = re.captures(&line).expect("Can't find any match");

        let a: usize = caps[1].parse().unwrap();
        let b: usize = caps[2].parse().unwrap();
        let lt = &caps[3];
        let password = &caps[4];
        
        if (a..=b).contains(&(password.matches(&lt).count())) {
            count += 1;
        }
    }
    count
}

fn part_two() -> i32 {
    let inp = load_input();
    let re = Regex::new(r"(\d+)-(\d+) ([a-z]): ([a-z]+)").unwrap();

    let mut count = 0;
    for line in inp {
        let caps = re.captures(&line).expect("Can't find any match");

        let a = caps[1].parse::<usize>().unwrap() - 1;
        let b = caps[2].parse::<usize>().unwrap() - 1;
        let lt = &caps[3];
        let password = &caps[4];
        
        if (&password[a..=a] == lt) ^ (&password[b..=b] == lt) {
            count += 1;
        }
    }
    count
}