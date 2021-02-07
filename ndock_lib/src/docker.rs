// pub struct Docker {}

use super::envs::Any;
use super::envs::Env;
use super::envs::Main;
use super::envs::Master;
use super::envs::Staging;
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
        match env {
            "any" => Some(Box::new(Any {
                env: "any".to_string(),
                command: None,
                load_file: "".to_string(),
                shell_file: "docker/cs_main.sh".to_string(),
            })),
            "main" => Some(Box::new(Main {
                env: "main".to_string(),
                command: None,
                load_file: "docker/automated_main.yaml".to_string(),
                shell_file: "docker/cs_main.sh".to_string(),
            })),
            "master" => Some(Box::new(Master {
                env: "master".to_string(),
                command: None,
                load_file: "docker/automated_master.yaml".to_string(),
                shell_file: "docker/cs_main.sh".to_string(),
            })),
            "staging" => Some(Box::new(Staging {
                env: "staging".to_string(),
                command: None,
                load_file: "docker/automated_staging.yaml".to_string(),
                shell_file: "docker/cs_main.sh".to_string(),
            })),
            _ => None,
        }
    }
}

pub mod docker {
    impl super::Docker {}
}
