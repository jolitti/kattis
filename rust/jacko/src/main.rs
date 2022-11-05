use std::io;
mod solver;

fn main() {
    
    solver::multiply_string(io::stdin().lock(), io::stdout());

}

#[test]
fn test_mul() {
    let mut s = Vec::new();
    solver::multiply_string(&b"2 2 2"[..],&mut s);
    assert_eq!(std::str::from_utf8(&s[..]).unwrap().trim(),"8");
    
    let mut s = Vec::new();
    solver::multiply_string(&b"3 4 5"[..],&mut s);
    assert_eq!(std::str::from_utf8(&s[..]).unwrap().trim(),"60");

    let mut s = Vec::new();
    solver::multiply_string(&b"3 1 5"[..],&mut s);
    assert_eq!(std::str::from_utf8(&s[..]).unwrap().trim(),"15");
}