use std::io::{BufRead,Write};

pub fn test() -> i32 {
    42
}

pub fn multiply_string<R,W>(mut source:R,mut destination:W)
where
    R: BufRead,
    W: Write,
{
    let mut s = String::new();
    source.read_line(&mut s).expect("Unable to read!");

    let params: Vec<u32> = s.trim().split(" ").map(|x| x.parse().unwrap()).collect();
    let prod = params.iter().copied().product::<u32>();

    writeln!(destination,"{}",prod);
}