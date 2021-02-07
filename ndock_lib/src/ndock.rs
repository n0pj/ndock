pub struct NDock {
    start_time: String,
    end_time: String,
}
use super::docker::Docker;
use super::ArgParser;
use super::Time;
use super::YamlParser;
use colored::*;
use serde_yaml::{self, Value};
use std::thread::sleep;
use std::time;

impl NDock {
    const START_TIME: String = String::new();

    pub fn new() -> Self {
        let start_time = String::new();
        let end_time = String::new();
        println!(
            "[{}] Start ndock ... ",
            Time::to_string(Time::now(None)).blue()
        );
        Self {
            start_time,
            end_time,
        }
    }

    pub fn run(&self) {
        let settings = YamlParser::import_with_load("settings.yaml");

        YamlParser::save(&settings.unwrap(), "test2.yaml");

        let app = ArgParser::new();
        let matches = app.get_matches();
        // let command = matches.value_of("command");
        let command = matches.value_of("command");
        let command = command.unwrap().to_string();
        let env = matches.value_of("env");
        let env = match env {
            Some(env) => Docker::new(env),
            None => {
                panic!()
            }
        };

        let mut env = if let Some(env) = env { env } else { panic!() };

        env.command(&command);
        env.run();

        self.drop()
    }

    pub fn drop(&self) -> () {
        println!(
            "[{}] Start ndock ... {}",
            Time::to_string(Time::now(None)).blue(),
            "done".green()
        );
    }
}

pub mod ndock {
    impl super::NDock {}
}
