
fn main() {
    let inp = load_input(r"C:\Users\florm\Desktop\input.txt");
    println!("Part 1: {}", part_one(&inp));
}

fn load_input(filename: &str) -> Vec<Vec<String>> {
    let operations = std::fs::read_to_string(filename)
        .expect("Couldn't open the file.");

    operations
        .lines()
        .map(|x| x.split_whitespace()
                 .map(str::to_owned)
                 .collect())
        .collect()
}

fn part_one(operations: &Vec<Vec<String>>) -> i32 {
    let mut acc = 0;
    let mut cache = vec![];

    let mut i: i32 = 0;
    while !cache.contains(&i) {
        cache.push(i);

        let instr = &operations[i as usize][0];
        let value: i32 = (&operations[i as usize][1]).parse().unwrap();
        
        if instr == "acc" {
            acc += value;
        } else if instr == "jmp" {
            i += value;
            continue;
        }
        i += 1;
    } 
    acc as i32
}