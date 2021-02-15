pub struct NDock {
    start_time: String,
    end_time: String,
}
use super::docker::Docker;
use super::ArgParser;
use super::EnvParser;
use super::Time;
use super::YamlParser;
use colored::*;
use serde_yaml::{self, Value};
use std::env;
use std::thread::sleep;
use std::time;

impl NDock {
    const START_TIME: String = String::new();

    pub fn new() -> Self {
        let start_time = String::new();
        let end_time = String::new();
        println!(
            "[{}] Start {} ... ",
            Time::to_string(Time::now(None)).cyan(),
            "ndock".cyan()
        );

        Self {
            start_time,
            end_time,
        }
    }

    pub fn run(&self) {
        let env_parser = EnvParser::new();
        env_parser.analyse_user_id();

        let app = ArgParser::new();
        let matches = app.get_matches();
        // let command = matches.value_of("command");

        let command = matches.value_of("command");
        let command = match command {
            Some(command) => command.to_string(),
            // command が指定されていない
            None => {
                // .env から取得
                let command = env::var("DEFAULT_COMMAND");
                match command {
                    Ok(command) => command.to_string(),
                    Err(_) => {
                        println!("{}", "Could not read the .env".red());
                        println!("{}", "Please copy from .env.example".red());
                        panic!()
                    }
                }
            }
        };

        let env = matches.value_of("env");
        let env = match env {
            // env が指定
            Some(env) => Docker::new(env),
            // env が指定されていない
            None => {
                // .env から取得
                let default_env = env::var("DEFAULT_ENV");
                let default_env = match default_env {
                    Ok(default_env) => default_env,
                    Err(_) => {
                        println!("{}", "Could not read the .env".red());
                        println!("{}", "Please copy from .env.example".red());
                        panic!()
                    }
                };
                Docker::new(&default_env)
            }
        };

        let mut env = if let Some(env) = env { env } else { panic!() };

        env.command(&command);

        // ndock 処理開始
        env.run();
        // let test = YamlParser::import_with_load("docker_settings/test.yaml");
        // YamlParser::save(&test.unwrap(), "docker_settings/test_out.yaml");
        self.drop()
    }

    pub fn drop(&self) -> () {
        println!(
            "[{}] Exit {} ...",
            Time::to_string(Time::now(None)).cyan(),
            "ndock".cyan()
        );
    }
}

pub mod ndock {
    impl super::NDock {}
}
