#![allow(unused)]

use std::io;
use rand::Rng;
use ndarray::arr2;
 //constants
const ROW: i32 =5;
const COL: i32 =5;

fn main() {

    //generate numbers
    let mut roundcount = 0;
    fieldgen();
    //build the playing field
    playground()
}
//playing field building functions

fn fieldgen() {
    let mut field: Vec<Vec<i32>> = vec![];
    //create the field
    let mut i = 0;
    while i < ROW {
        let a = vec![];
        field.push(a);
        let mut j = 0;
        while j < COL {
            let num = 2_i32.pow(rand::thread_rng().gen_range(1..=4));
            field[i as usize].push(num);
            j = j + 1;
        }
        i = i + 1;
    }
    // to print the field numbers:
    for inner_vector in &field {
        inner_vector.iter().for_each(|element| {
            println!("{}", element);
        });
    }
}

fn fieldnum() {
    use std::io::{self, Write};
    print!("   ");
    for i in 1..(ROW+1) {
        print!("   {}    ",i);
        io::stdout().flush().unwrap(); //Flush to print without newline
    }
}

fn line() {
    use std::io::{self, Write};
    print!("  ");
    for i in 0..ROW {
        print!("+-------")
    }
    print!("+")
    
}

fn playground() {
    fieldgen()
    fieldnum();
    println!("");
    for i in ROW {
        line();
        print!("{} ",i);
        for j in COL {
            if 100>field[i][j] && field[i][j]>10 {
                print!("| {}  ",field[i][j]);
            }
            else if 1000>field[i][j] && field[i][j]>100 {
                print!("|{} ",field[i][j]);
            }
            
            else{
                print!("|  {}  ",field[i][j]);
            }
        }
        println!("|")

    }
}