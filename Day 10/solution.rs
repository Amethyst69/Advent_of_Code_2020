
fn main() {
    let inp = load_input("input.txt");
    println!("Part 1: {}", part_one(&inp));
}

fn load_input(filename: &str) -> Vec<i32> {
    let file = std::fs::read_to_string(filename)
        .expect("Couldn't open the file");

    file
        .lines()
        .map(|x| x.parse().unwrap())
        .collect()
}

fn part_one(adapters: &Vec<i32>) -> i32 {
    let mut adapters = adapters.to_vec();
    adapters.push(adapters.iter().max().unwrap() + 3);

    let mut effective = 0;
    let mut tdiff = 0;
    let mut odiff = 0;
    while !adapters.is_empty() {
        if adapters.contains(&(effective + 1)) {
            effective += 1;
            odiff += 1;
        } else if adapters.contains(&(effective + 3)) {
            effective += 3;
            tdiff += 1;
        }
        adapters.remove(adapters.iter().position(|x| x == &effective).unwrap());
    }
    tdiff * odiff
}