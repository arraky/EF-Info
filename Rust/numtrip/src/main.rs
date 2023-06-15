#![allow(unused)]

use std::io;
use rand::Rng;
use ndarray::arr2;


fn main() {

    let row = 5;
    let col = 5;
    let mut roundcount = 0;
    let mut field = arr2([]);
    let mut i = 0;

    while i < row {
        field.push([]);
        let mut j = 0;
        while j < col {
            let mut num = 2^(rand::thread_rng().gen_range(1..=3));
            field[i].push(num);
            j = j + 1
        }
        i = i + 1;
    }

    println!("{field}")
}