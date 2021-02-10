// pub struct Docker {}

use super::envs::Any;
use super::envs::Env;
use super::envs::Main;
use super::envs::Master;
use super::envs::Staging;
use super::Time;
use colored::*;

#[derive(Debug)]
pub struct Docker {}

// pub trait DefaultMethods {
//   fn new();
//   fn call(&self, command: &str) {}
//   fn start() {}
//   fn down() {}
// }

impl Docker {
    pub fn new(env: &str) -> Option<Box<dyn Env + 'static>> {
        println!(
            "[{}] Current env is ... {}",
            Time::to_string(Time::now(None)).cyan(),
            &env.green()
        );

        match env {
            "any" => Some(Box::new(Any {
                env: "any".to_string(),
                command: None,
                load_file: "".to_string(),
                shell_file: "".to_string(),
            })),
            "main" => Some(Box::new(Main {
                env: "main".to_string(),
                command: None,
                load_file: "docker_settings/automated_main.yaml".to_string(),
                shell_file: "docker_settings/cs_main.sh".to_string(),
            })),
            "master" => Some(Box::new(Master {
                env: "master".to_string(),
                command: None,
                load_file: "docker_settings/automated_master.yaml".to_string(),
                shell_file: "docker_settings/cs_master.sh".to_string(),
            })),
            "staging" => Some(Box::new(Staging {
                env: "staging".to_string(),
                command: None,
                load_file: "docker_settings/automated_staging.yaml".to_string(),
                shell_file: "docker_settings/cs_staging.sh".to_string(),
            })),
            _ => {
                println!("{} ... {}", "Not allowed the env".red(), &env.red());
                println!(
                    "{} ... {}",
                    "These envs only".red(),
                    "any, main, master, staging".green()
                );
                panic!()
            }
        }
    }
}

pub mod docker {
    impl super::Docker {}
}
