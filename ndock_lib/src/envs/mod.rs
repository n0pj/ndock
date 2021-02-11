pub mod any;
pub mod main;
pub mod master;
pub mod staging;

use crate::YamlParser;
pub use any::Any;
use colored::*;
pub use main::Main;
pub use master::Master;
use regex::Regex;
pub use staging::Staging;
use std::env;

pub trait Env {
  fn env(&self) {}
  fn command(&mut self, command: &str) {}
  fn run(&self) {}
  fn test(&self) {}
  fn start(&self) {}
  fn stop(&self) {}
  fn up(&self) {}
  fn down(&self) {}
  fn rm(&self) {}
  fn rmi(&self) {}
  fn force_rm(&self) {}
  fn force_rmi(&self) {}
  fn build(&self) {}
  fn shell(&self) {}

  // container_name を自動生成する
  fn generate_container_name(&self, file_path: &str) {
    let automated_settings = YamlParser::load_only_string(&file_path).unwrap();

    let re_container_name = Regex::new(r"( *)container_name: (.*)").unwrap();

    let mut new_automated_settings = String::new();

    let project_name = env::var("PROJECT_NAME");
    let project_name = match project_name {
      Ok(project_name) => project_name.to_string(),
      Err(_) => {
        println!("{}", "Could not read the .env".red());
        println!("{}", "Please copy from .env.example".red());
        panic!()
      }
    };

    for line in automated_settings.lines() {
      let container_name_caps = re_container_name.captures(&line);

      // capture が None ならただ push
      if let None = container_name_caps {
        new_automated_settings.push_str(line);
        new_automated_settings.push_str("\n");
        continue;
      }

      let container_name_caps = container_name_caps.unwrap();
      // let container_name = container_name_caps.get(0); // full
      let whitespaces = container_name_caps.get(1).unwrap(); // whitespaces
      let whitespaces = whitespaces.as_str(); // whitespaces
      let whitespaces = whitespaces.to_string(); // whitespaces
      let container_name = container_name_caps.get(2).unwrap(); // container_name のみ
      let container_name = container_name.as_str(); // container_name のみ

      // let new_container_name = &project_name + println!("{:?}", line);
      let project_name = project_name.clone();
      let new_container_name = project_name + container_name;
      let new_container_name_prop = format!("container_name: {}", new_container_name);
      let new_container_name_prop = whitespaces + &new_container_name_prop;

      new_automated_settings.push_str(&new_container_name_prop);
      new_automated_settings.push_str("\n");
    }
    let new_automated_settings = YamlParser::load_from_str(&new_automated_settings);
    let new_automated_settings = match new_automated_settings {
      Ok(new_automated_settings) => new_automated_settings,
      Err(_) => {
        println!(
          "{} ... {}",
          "Error, file format is right?".red(),
          file_path.red()
        );
        panic!()
      }
    };
    YamlParser::save(&new_automated_settings, file_path);
  }
}
