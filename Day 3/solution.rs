
fn main() {
    let inp = load_input();
    println!("Part 1: {}", solution(3, 1, &inp));

    let mut part_two = 1;
    let slopes = vec![(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)];
    for (r, d) in slopes {
        part_two *= solution(r, d, &inp);
    }
    println!("Part 2: {}", part_two);
}

fn load_input() -> Vec<String> {
    let file = std::fs::read_to_string(r"C:\Users\florm\Desktop\input.txt")
        .expect("Couldn't open the file");

    file
        .lines()
        .map(|s| s.to_owned())
        .collect::<Vec<String>>()
}

fn solution(right: usize, down: usize, inp: &Vec<String>) -> i64 {
    let mut x_pos: usize = 0;
    let mut trees: i64 = 0;

    for i in (0..inp.len()).step_by(down) {
        let line = &inp[i];
        if line.chars().nth(x_pos % 31).unwrap() == '#' {
            trees += 1;
        }
        x_pos += right;
    }
    trees
}




