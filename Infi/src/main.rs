use std::fs;
use std::time::Instant;
use rayon::prelude::*;

enum Opp {
    PushN(i32),
    PushX,
    PushY,
    PushZ,
    Add,
    Jmpos(usize),
    Ret,
}

fn catagorize_instruction(ins: &str) -> Opp {
    if ins.contains("push") {
        if ins.contains("X") {
            return Opp::PushX;
        } else if ins.contains("Y") {
            return Opp::PushY;
        } else if ins.contains("Z") {
            return Opp::PushZ;
        } else {
            let num: i32 = ins.split(" ").nth(1).unwrap()
            .parse().expect("Failed to parse number");
            return Opp::PushN(num);
        }
    } else if ins.contains("add") {
        return Opp::Add;
    } else if ins.contains("jmpos") {
        let num: usize = ins.split(" ").nth(1).unwrap()
        .parse().expect("Failed to parse number");
        return Opp::Jmpos(num);
    } else {
        return Opp::Ret;
    }
}

const NEIGHBORS: [(i32, i32, i32); 6] = [
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1)
];

fn main() {
    let now = Instant::now();

    let binding: String = fs::read_to_string("input.txt")
        .expect("Should have been able to read the file");

    let instructions: Vec<Opp> = binding.split("\n").collect::<Vec<_>>()
        .par_iter().map(|ins| catagorize_instruction(ins)).collect();

    let elapsed0 = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed0);

    let mut blocks = 0;
    let mut clouds = 0;

    let mut cloud_array: [[[bool; 30]; 30]; 30] = [[[false; 30]; 30]; 30];

    cloud_array.par_iter_mut().enumerate().for_each(|(x, sx)| {
        sx.par_iter_mut().enumerate().for_each(|(y, sy)| {
            sy.par_iter_mut().enumerate().for_each(|(z, data)| {
                // initilize program counter at first line of code
                let mut pc: usize = 0;
                let mut stack: Vec<i32> = Vec::new();
                loop {
                    // get current instruction
                    let instruction = &instructions[pc];
                    pc += 1;
                    // when a line starts with push it is either
                    // push X, push Y, push Z, or push N where N is an integer
                    // If it is one of the first three, we will push that position-value to the stack
                    // otherwise, push N to the stack
                    match instruction {
                        Opp::PushX => stack.push(x as i32),
                        Opp::PushY => {
                            stack.push(y as i32)
                        },
                        Opp::PushZ => {
                            stack.push(z as i32)
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
                    *data = true;
                }
            });
        });
    });

    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed);

    let mut checking: Vec<(i32, i32, i32)> = Vec::new();
    let mut cx = 0;
    let mut cy = 0;
    let mut cz = 0;

    loop {
        if checking.is_empty() {
            while !cloud_array[cx as usize][cy as usize][cz as usize] {
                cx += 1;
                if cx == 30 {
                    cx = 0;
                    cy += 1;
                }
                if cy == 30 {
                    cy = 0;
                    cz += 1;
                }
                if cz == 30 {
                    println!("There are {blocks} blocks of snow, making up {clouds} clouds");

                    let elapsed2 = now.elapsed();
                    println!("Elapsed: {:.2?}", elapsed2);
                    std::process::exit(0);
                }
            }
            checking.push((cx, cy, cz));
            clouds += 1;
        }

        let (x, y, z) = checking.pop().expect("there weren't one");
        
        for (dx, dy, dz) in NEIGHBORS {
            let nx = x + dx;
            let ny = y + dy;
            let nz = z + dz;
            if nx < 0 || ny < 0 || nz < 0 || nx > 29 || ny > 29 || nz > 29 {
                continue;
            }
            if cloud_array[nx as usize][ny as usize][nz as usize] {
                cloud_array[nx as usize][ny as usize][nz as usize] = false;
                blocks += 1;
                checking.push((nx, ny, nz));
            }
        }   
    }
}