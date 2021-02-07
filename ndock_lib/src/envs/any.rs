use crate::envs::Env;
use colored::*;
use eval::eval;

pub struct Any {
    pub env: String,
    pub command: Option<AllowCommand>,
    pub load_file: String,
    pub shell_file: String,
}

pub enum AllowCommand {
    Start,
    Stop,
    Up,
    Down,
    Build,
    Shell,
}

impl Env for Any {
    fn env(&self) {}

    fn command(&mut self, command: &str) {
        match command {
            _ => {
                println!("Not allowed command: {}", command.red());
                panic!()
            }
        }
    }
}

pub mod any {
    impl super::Any {}
}
