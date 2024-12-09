use std::fs;
use std::collections::HashSet;
use std::time::Instant;
extern crate rayon;
use rayon::prelude::*;


// rustc -C opt-level=3 puzzle.rs

enum Opp {
    PushN(i32),
    PushX,
    PushY,
    PushZ,
    Add,
    Jmpos(i32),
    Ret,
}

fn main() {
    let now = Instant::now();

    let binding: String = fs::read_to_string("input.txt")
        .expect("Should have been able to read the file");
    let inp: Vec<&str> = binding.split("\n").collect::<Vec<_>>();

    let mut instructions: Vec<Opp> = Vec::new();

    // parse instructions
    for ins in inp.clone() {
        if ins.contains("push") {
            if ins.contains("X") {
                instructions.push(Opp::PushX);
            } else if ins.contains("Y") {
                instructions.push(Opp::PushY);
            } else if ins.contains("Z") {
                instructions.push(Opp::PushZ);
            } else {
                let subs = ins.split(" ").nth(1).unwrap();
                let num: i32 = subs.parse().expect("Failed to parse number");
                instructions.push(Opp::PushN(num));
            }
        // If the instruction is add, we take the first two elements from
        // the stack, add them, and push them back on the stack
        } else if ins.contains("add") {
            instructions.push(Opp::Add);
        // If the instruction is jmpos, we jump the following number of lines
        // forward if the first element of the stack is non-negitive
        } else if ins.contains("jmpos") {
            let subs = ins.split(" ").nth(1).unwrap();
            let num: i32 = subs.parse().expect("Failed to parse number");
            instructions.push(Opp::Jmpos(num));
        // When we land on ret, the program halts, and the top value on the stack is 'returned'
        } else if ins.contains("ret") {
            instructions.push(Opp::Ret);
        }
    }

    const NEIGHBORS: [(i32, i32, i32); 6] = [
        (1, 0, 0), (-1, 0, 0),
        (0, 1, 0), (0, -1, 0),
        (0, 0, 1), (0, 0, -1)
    ];

    let mut unchecked: HashSet<(i32, i32, i32)> = HashSet::new();
    let mut blocks = 0;
    let mut clouds = 0;


    let mut stack: Vec<i32> = Vec::new();

    let iter = 0..30;
    iter.for_each(|x| {
        for y in 0..30 {
            for z in 0..30 {
                // initilize program counter at first line of code
                let mut pc: i32 = 0;
                stack.clear();
                loop {
                    // get current instruction
                    let instruction = &instructions[pc as usize];
                    pc += 1;
                    // when a line starts with push it is either
                    // push X, push Y, push Z, or push N where N is an integer
                    // If it is one of the first three, we will push that position-value to the stack
                    // otherwise, push N to the stack
                    match instruction {
                        Opp::PushX => stack.push(x),
                        Opp::PushY => {
                            stack.push(y)
                        },
                        Opp::PushZ => {
                            stack.push(z)
                        },
                        Opp::PushN(n) => {
                            stack.push(*n)
                        },
                        Opp::Add => {
                            let a = stack.pop().expect("uh oh a");
                            let b = stack.pop().expect("uh oh b");
                            stack.push(a + b);
                        },
                        Opp::Jmpos(p) => {
                            if *stack.last().expect("uh oh") >= 0 {
                                pc += p;
                            }
                        },
                        Opp::Ret => {
                            break
                        }
                    }
                }
                if stack.pop().expect("uh oh c") > 0 {
                    // add to the number of blocks in clouds
                    blocks += 1;
                    unchecked.insert((x, y, z));
                }
            }
        }
    });

    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed);

    let mut checking: Vec<(i32, i32, i32)> = Vec::new();

    while !unchecked.is_empty() {
        if checking.is_empty() {
            let elem = unchecked.iter().next().unwrap().clone();
            unchecked.remove(&elem);
            checking.push(elem);
            clouds += 1;
        }

        let pos = checking.pop().expect("there weren't one");
        
        for (dx, dy, dz) in NEIGHBORS {
            let neighbor_pos = (pos.0 + dx, pos.1 + dy, pos.2 + dz);
            if unchecked.contains(&neighbor_pos) {
                unchecked.remove(&neighbor_pos);
                checking.push(neighbor_pos);
            }
        }

        
    }

    println!("There are {blocks} blocks of snow, making up {clouds} clouds");

    let elapsed2 = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed2);
}
