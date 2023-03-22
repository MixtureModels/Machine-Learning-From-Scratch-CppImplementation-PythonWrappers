#[macro_use]
extern crate cpython;

use cpython::{Python, PyResult};

// Rust boilerplate for running add vector function
fn addVectors(_py: Python, vecOne: Vec<i32>>, vecTwo: Vec<i32>) -> () {
    let mut computeVal = 0u32;

    for (i, elem) in vecOne.Iter().Enumerate()) {
        computeVal = vecOne[i] + vecTwo[i];
    }

}

