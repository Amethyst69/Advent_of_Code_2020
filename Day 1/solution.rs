fn main() {
    let inp = load_input();
    println!("Part 1: {}", part_one(&inp));
    println!("Part 2: {}", part_two(&inp));
}

fn load_input() -> Vec<i32> {
    let file = std::fs::read_to_string("input.txt")
        .unwrap();

    file
        .lines()
        .map(|x| x.parse::<i32>().unwrap())
        .collect::<Vec<i32>>()
}

fn part_one(inp: &Vec<i32>) -> i32 {
    for i in inp {
        if inp.contains(&(2020 - i)) {
            return i * (2020 - i)
        }
    }
    0
}

fn part_two(inp: &Vec<i32>) -> i32 {
    for x in inp {
        for y in inp {
            let z = 2020 - x - y;
            if inp.contains(&z) {
                return x * y * z;
            }
        }
    }
    0
}
