pub struct NDock {
  start_time: String,
  end_time: String,
}
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
      "[{}] Starting ndock ... ",
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
    // let docker_settings;

    // if let Ok(settings) = &settings {
    //   docker_settings = &settings["docker_settings"];
    // } else {
    //   println!("Can not load ... {}", "'settings.yaml'".red());
    //   panic!()
    // }

    // if let Some(docker_settings) = docker_settings.as_mapping() {
    //   for v in docker_settings {
    //     println!("{:?}", v);
    //     let image_name = v.0;

    //     // let image_name = String::from(v.0);

    //     let test = &YamlParser::to_yvstring("nginx");
    //     if image_name == test {
    //       println!("yes!!! {:?}", test)
    //     }
    //   }
    // }
  }

  pub fn arg_parse() {
    let app = ArgParser::new();

    let matches = app.get_matches();

    if let Some(o) = matches.value_of("pa") {
      println!("{}", o)
    }
  }

  pub fn drop(&self) -> () {
    println!(
      "[{}] Exit ndock ... {}",
      Time::to_string(Time::now(None)).blue(),
      "done".green()
    );
  }
}

pub mod ndock {
  impl super::NDock {}
}
