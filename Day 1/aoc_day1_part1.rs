fn load_input() -> Vec<i32> {
    let file = std::fs::read_to_string("input.txt")
        .unwrap();

    let inp: Vec<i32> = file.lines()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
    
    return inp;
}

fn main() {
    let inp = load_input();
    
    for i in &inp {
        if inp.contains(&(2020 - i)) {
            println!("{}", (i * (2020 - i)));
            break;
        }
    }
}