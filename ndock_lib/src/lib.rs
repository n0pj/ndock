#[macro_use]
extern crate clap;
extern crate chrono;
extern crate colored;
extern crate serde;
extern crate serde_yaml;

pub mod arg_parser;
pub mod commands;
pub mod ndock;
pub mod time;
pub mod yaml_parser;
pub use arg_parser::ArgParser;
pub use commands::Commands;
pub use ndock::NDock;
pub use time::Time;
pub use yaml_parser::YamlParser;

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}
