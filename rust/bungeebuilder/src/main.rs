use std::io;

fn main() -> io::Result<()> {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer)?;
    buffer.clear();
    io::stdin().read_line(&mut buffer)?;
    println!("buffer: {buffer}");

    let peaks: Vec<usize> = buffer.trim().split(" ")
                                .map(
                                    |s| {
                                        println!("{}",s);
                                        s.trim().parse::<usize>().unwrap()
                                    }
                                ).collect();
    println!("{peaks:?}");
    Ok(())
}
