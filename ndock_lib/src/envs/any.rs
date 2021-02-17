use crate::envs::Env;
use crate::Time;
use colored::*;
use eval::eval;
use regex::Regex;
use std::process::Command;

pub struct Any {
    pub env: String,
    pub command: Option<AllowCommand>,
    pub load_file: String,
    pub shell_file: String,
}

pub enum AllowCommand {
    Stop,
    RM,
    RMI,
    // ForceRM,
    // ForceRMI,
}

impl Env for Any {
    fn command(&mut self, command: &str) {
        println!(
            "[{}] Current command is ... {}",
            Time::to_string(Time::now(None)).cyan(),
            &command.green()
        );

        match command {
            "stop" => {
                self.command = Some(AllowCommand::Stop);
            }
            "rm" => {
                self.command = Some(AllowCommand::RM);
            }
            "rmi" => {
                self.command = Some(AllowCommand::RMI);
            }
            // "force-rm" => {
            //     self.command = Some(AllowCommand::ForceRM);
            // }
            // "force-rmi" => {
            //     self.command = Some(AllowCommand::ForceRMI);
            // }
            _ => {
                println!("Not allowed the command ... {}", command.red());
                println!(
                    "{} ... {}",
                    "These commands only".red(),
                    "stop, rm, rmi".green()
                );
                panic!()
            }
        }
    }

    fn run(&self) {
        let command = &self.command;
        match command {
            Some(AllowCommand::Stop) => self.stop(),
            Some(AllowCommand::RM) => self.rm(),
            Some(AllowCommand::RMI) => self.rmi(),
            // Some(AllowCommand::ForceRM) => self.force_rm(),
            // Some(AllowCommand::ForceRMI) => self.force_rmi(),
            None => {
                println!("{}", "Unknown Error".red());
                panic!()
            }
        }
    }

    fn stop(&self) {
        match Command::new("docker").arg("-v").status() {
            Ok(_) => {}
            Err(_) => {
                println!("{}", "Unknown error, realy installed docker?".yellow());
                panic!()
            }
        }

        let docker_ps = Command::new("docker")
            .arg("ps")
            .arg("-a")
            .arg("-q")
            .output()
            .expect("error");
        let docker_ps = String::from_utf8(docker_ps.stdout).unwrap();

        let mut docker_ps_vec = vec![];

        for line in docker_ps.lines() {
            docker_ps_vec.push(line)
        }

        Command::new("docker")
            .arg("stop")
            // .arg(format!("`{}`", docker_ps))
            .args(docker_ps_vec)
            .status()
            .expect("error");
    }

    fn rm(&self) {
        match Command::new("docker").arg("-v").status() {
            Ok(_) => {}
            Err(_) => {
                println!("{}", "Unknown error, realy installed docker?".yellow());
                panic!()
            }
        }

        let docker_ps = Command::new("docker")
            .arg("ps")
            .arg("-a")
            .arg("-q")
            .output()
            .expect("error");
        let docker_ps = String::from_utf8(docker_ps.stdout).unwrap();

        let mut docker_ps_vec = vec![];

        for line in docker_ps.lines() {
            docker_ps_vec.push(line)
        }

        Command::new("docker")
            .arg("rm")
            .args(docker_ps_vec)
            .status()
            .expect("error");
    }

    fn rmi(&self) {
        match Command::new("docker").arg("-v").status() {
            Ok(_) => {}
            Err(_) => {
                println!(
                    "{}",
                    "Unknown error, realy installed docker-compose?".yellow()
                );
                panic!()
            }
        }

        let docker_images = Command::new("docker")
            .arg("images")
            .arg("-q")
            .output()
            .expect("error");
        let docker_images = String::from_utf8(docker_images.stdout).unwrap();

        let mut docker_images_vec = vec![];

        for line in docker_images.lines() {
            docker_images_vec.push(line)
        }

        Command::new("docker")
            .arg("rmi")
            .args(docker_images_vec)
            .status()
            .expect("error");
    }
}

pub mod any {
    impl super::Any {}
}
