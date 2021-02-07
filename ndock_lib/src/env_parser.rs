use crate::Time;
use colored::*;
use colored::*;
use dotenv::dotenv;
use regex::Regex;
use std::env;
use std::fs;
use std::fs::{File, OpenOptions};
use std::io::{self, Read, Write};
use std::process::Command;

pub struct EnvParser {}

impl EnvParser {
  pub fn new() -> Self {
    if dotenv().is_err() {
      println!("{}", "Not found .env".red());
      println!("{}", "Please copy from .env.example".red());
      panic!()
    }

    Self {}
  }

  pub fn parse_env() {
    let dotenv_str = fs::read_to_string(".env");
    let dotenv_str = match dotenv_str {
      Ok(s) => s,
      Err(_) => {
        println!("{}", "Not found .env".red());
        println!("{}", "Please copy from .env.example".red());
        panic!()
      }
    };

    let user_id = Command::new("id").arg("-u").output().expect("eee");
    let user_id = String::from_utf8(user_id.stdout).unwrap();
    let mut new_dotenv_str = String::new();

    let re = Regex::new(r"(?m)(USER_ID)").unwrap();

    for line in dotenv_str.lines() {
      let mat = re.find(&line);
      match mat {
        Some(_) => {
          let user_id_line = format!("USER_ID={}", user_id);
          new_dotenv_str.push_str(&user_id_line);
          new_dotenv_str.push_str("\n");
          continue;
        }
        None => {
          new_dotenv_str.push_str(&line);
          new_dotenv_str.push_str("\n");
          continue;
        }
      }
    }
  }

  pub fn analyse_user_id(&self) {
    let dotenv_str = fs::read_to_string(".env");
    let dotenv_str = match dotenv_str {
      Ok(s) => s,
      Err(_) => {
        println!("{}", "Not found .env".red());
        println!("{}", "Please copy from .env.example".red());
        panic!()
      }
    };

    let user_id = Command::new("id").arg("-u").output().expect("eee");
    let user_id = String::from_utf8(user_id.stdout).unwrap();
    println!(
      "[{}] Current USER_ID ... {}",
      Time::to_string(Time::now(None)).blue(),
      user_id.green()
    );
    let mut new_dotenv_str = String::new();

    let re = Regex::new(r"(?m)(USER_ID)").unwrap();
    let re_n = Regex::new(r"(?m)\n").unwrap();
    let dotenv_str_lines = dotenv_str.lines();

    for line in dotenv_str_lines {
      let mat = re.find(&line);
      if line == "" || line == "\r" || line == "\n" {
        continue;
      }

      match mat {
        Some(_) => {
          let user_id_line = format!("USER_ID={}", user_id);
          let mat = re_n.find(&line);
          new_dotenv_str.push_str(&user_id_line);

          // 改行がなかったら追加
          if let None = mat {
            new_dotenv_str.push_str("\n");
          }
          continue;
        }
        None => {
          new_dotenv_str.push_str(&line);
          let mat = re_n.find(&line);

          // 改行がなかったら追加
          if let None = mat {
            new_dotenv_str.push_str("\n");
          }
          continue;
        }
      }
    }

    self.save(&new_dotenv_str, ".env")
  }

  pub fn save(&self, text: &str, path: &str) {
    let mut writer = OpenOptions::new().write(true).open(path);

    if let Err(_) = writer {
      writer = File::create(path);
    }

    if let Ok(mut writer) = writer {
      let bytes = text.as_bytes();
      &writer.set_len(0);
      &writer.write_all(&bytes).unwrap();
    }
  }
}

pub mod env_parser {
  impl super::EnvParser {}
}
