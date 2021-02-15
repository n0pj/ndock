use crate::envs::Env;
use crate::Time;
use crate::YamlParser;
use colored::*;
use eval::eval;
use std::process::Command;

pub struct Staging {
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

impl Env for Staging {
    fn command(&mut self, command: &str) {
        println!(
            "[{}] Current command is ... {}",
            Time::to_string(Time::now(None)).cyan(),
            &command.green()
        );

        match command {
            "start" => {
                self.command = Some(AllowCommand::Start);
            }
            "stop" => {
                self.command = Some(AllowCommand::Stop);
            }
            "up" => {
                self.command = Some(AllowCommand::Up);
            }
            "down" => {
                self.command = Some(AllowCommand::Down);
            }
            "build" => {
                self.command = Some(AllowCommand::Build);
            }
            "shell" => {
                self.command = Some(AllowCommand::Shell);
            }
            _ => {
                println!("Not allowed the command ... {}", command.red());
                println!(
                    "{} ... {}",
                    "These commands only".red(),
                    "start, stop, up, down, build, shell".green()
                );
                panic!()
            }
        }
    }

    fn run(&self) {
        let command = &self.command;
        match command {
            Some(AllowCommand::Start) => self.start(),
            Some(AllowCommand::Stop) => self.stop(),
            Some(AllowCommand::Up) => self.up(),
            Some(AllowCommand::Down) => self.down(),
            Some(AllowCommand::Build) => self.build(),
            Some(AllowCommand::Shell) => self.shell(),
            None => {
                println!("{}", "Unknown Error".red());
                panic!()
            }
        }
    }

    fn up(&self) {
        match Command::new("docker-compose").arg("-v").status() {
            Ok(_) => {}
            Err(_) => {
                println!(
                    "{}",
                    "Unknown error, realy installed docker-compose?".yellow()
                );
                panic!()
            }
        }

        let load_file = &*self.load_file;

        let file_path = format!("docker_settings/{}.yaml", &self.env);
        let settings = YamlParser::import_with_load(&file_path);
        YamlParser::save(&settings.unwrap(), &load_file);
        Command::new("docker-compose")
            .arg("-f")
            .arg(&load_file)
            .arg("up")
            .arg("-d")
            .status()
            .expect("error");
    }

    fn start(&self) {
        match Command::new("docker-compose").arg("-v").status() {
            Ok(_) => {}
            Err(_) => {
                println!(
                    "{}",
                    "Unknown error, realy installed docker-compose?".yellow()
                );
                panic!()
            }
        }

        let load_file = &*self.load_file;

        let file_path = format!("docker_settings/{}.yaml", &self.env);
        let settings = YamlParser::import_with_load(&file_path);
        YamlParser::save(&settings.unwrap(), &load_file);
        Command::new("docker-compose")
            .arg("-f")
            .arg(&load_file)
            .arg("start")
            .status()
            .expect("error");
    }

    fn stop(&self) {
        match Command::new("docker-compose").arg("-v").status() {
            Ok(_) => {}
            Err(_) => {
                println!(
                    "{}",
                    "Unknown error, realy installed docker-compose?".yellow()
                );
                panic!()
            }
        }

        let load_file = &*self.load_file;

        let file_path = format!("docker_settings/{}.yaml", &self.env);
        let settings = YamlParser::import_with_load(&file_path);
        YamlParser::save(&settings.unwrap(), &load_file);
        Command::new("docker-compose")
            .arg("-f")
            .arg(&load_file)
            .arg("stop")
            .status()
            .expect("error");
        println!(
            "[{}] Stop ndock {} ... {}",
            Time::to_string(Time::now(None)).cyan(),
            &self.env,
            "done".green()
        );
    }

    fn down(&self) {
        match Command::new("docker-compose").arg("-v").status() {
            Ok(_) => {}
            Err(_) => {
                println!(
                    "{}",
                    "Unknown error, realy installed docker-compose?".yellow()
                );
                panic!()
            }
        }

        let load_file = &*self.load_file;

        let file_path = format!("docker_settings/{}.yaml", &self.env);
        let settings = YamlParser::import_with_load(&file_path);
        YamlParser::save(&settings.unwrap(), &load_file);
        Command::new("docker-compose")
            .arg("-f")
            .arg(&load_file)
            .arg("down")
            .arg("--rmi")
            .arg("all")
            .arg("--volumes")
            .arg("--remove-orphans")
            .status()
            .expect("error");
        println!(
            "[{}] Down ndock {} ... {}",
            Time::to_string(Time::now(None)).cyan(),
            &self.env,
            "done".green()
        );
    }

    fn build(&self) {
        match Command::new("docker-compose").arg("-v").status() {
            Ok(_) => {}
            Err(_) => {
                println!(
                    "{}",
                    "Unknown error, realy installed docker-compose?".yellow()
                );
                panic!()
            }
        }

        let load_file = &*self.load_file;

        let file_path = format!("docker_settings/{}.yaml", &self.env);
        let settings = YamlParser::import_with_load(&file_path);
        YamlParser::save(&settings.unwrap(), &load_file);
        Command::new("docker-compose")
            .arg("-f")
            .arg(&load_file)
            .arg("build")
            .status()
            .expect("error");
    }

    fn shell(&self) {
        let shell_file = format!("docker_settings/cs_{}.sh", &self.env);
        Command::new("sh").arg(&shell_file).status().expect("error");
        println!(
            "[{}] Run Shell {} ... {}",
            Time::to_string(Time::now(None)).cyan(),
            &self.env,
            "done".green()
        );
    }
}

pub mod staging {
    impl super::Staging {}
}
