#[macro_use]
extern crate clap;
extern crate chrono;
extern crate colored;
extern crate dotenv;
#[macro_use]
extern crate dotenv_codegen;
extern crate eval;
extern crate serde;
extern crate serde_yaml;

pub mod arg_parser;
pub mod commands;
pub mod docker;
pub mod env_parser;
pub mod envs;
pub mod ndock;
pub mod time;
pub mod yaml_parser;

pub use arg_parser::ArgParser;
pub use commands::Commands;
pub use docker::Docker;
pub use env_parser::EnvParser;
pub use envs::any::Any;
pub use envs::main::Main;
pub use envs::master::Master;
pub use envs::staging::Staging;
pub use ndock::NDock;
pub use time::Time;
pub use yaml_parser::YamlParser;

// pub use envs::main;

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}
