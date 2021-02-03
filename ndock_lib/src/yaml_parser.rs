use colored::*;
use regex::Regex;
use serde_yaml;
use std::fs::{File, OpenOptions};
use std::io::{self, Read, Write};
pub struct YamlParser {}

impl YamlParser {
  pub fn new() -> Self {
    Self {}
  }
  // pub fn load(path: &str) -> Result<String, io::Error> {
  pub fn import_with_load(path: &str) -> Result<serde_yaml::Value, serde_yaml::Error> {
    let mut main: String = super::YamlParser::load_only_string(&path).unwrap();
    main = super::YamlParser::exists_import_block(main, path);

    serde_yaml::from_str(&main)
  }

  pub fn exists_import_block(main: String, path: &str) -> String {
    let mut result = main.clone();
    let mut exists_import_block = true;
    let mut import_count = 0;

    while exists_import_block {
      // println!("{}", s);
      let re = Regex::new(r"( *)import: (.*.yaml)").unwrap();

      let main_clone = result.clone();
      let caps_iter = re.captures_iter(&main_clone);

      for cap in caps_iter {
        let mat0 = cap.get(0).unwrap(); // full import context
        let mat1 = cap.get(1).unwrap(); // whitespaces
        let mat2 = cap.get(2).unwrap(); // filename
        let import_path = mat2.as_str();
        let whitespaces = mat1.as_str();
        let prop_with_import_path = mat0.as_str();

        let sub: String = super::YamlParser::load_only_string(&import_path).unwrap();
        let mut new_sub = String::new();
        for line in sub.lines() {
          new_sub.push_str(whitespaces);
          new_sub.push_str(line);
          new_sub.push_str("\n");
        }
        result = result.replacen(prop_with_import_path, &new_sub, 1);
      }
      if !re.is_match(&result) {
        exists_import_block = false;
      }
      if import_count + 1 >= 10 {
        exists_import_block = false;

        println!("File ... {}", &path);
        println!("Import 10 more ... {}", "force quit import".yellow())
      }
      import_count += 1;
    }
    result
  }

  // pub fn loop_import(string: String) -> String {

  // }

  pub fn load_only_string(path: &str) -> Result<String, io::Error> {
    let mut s = String::new();
    File::open(&path)?.read_to_string(&mut s)?;
    Ok(s)
  }

  pub fn load_from_str(s: &str) -> Result<serde_yaml::Value, serde_yaml::Error> {
    serde_yaml::from_str(&s)
  }

  pub fn load(path: &str) -> Result<serde_yaml::Value, serde_yaml::Error> {
    let mut s = String::new();
    File::open(&path).unwrap().read_to_string(&mut s).unwrap();

    serde_yaml::from_str(&s)
  }

  pub fn save(yaml_struct: &serde_yaml::Value, path: &str) -> () {
    let mut writer = OpenOptions::new().write(true).open(path);

    if let Err(_) = writer {
      writer = File::create(path);
    }

    if let Ok(mut writer) = writer {
      let result = serde_yaml::to_string(&yaml_struct).unwrap();
      let bytes = &result.as_bytes();
      &writer.set_len(0);
      &writer.write_all(&bytes).unwrap();
    }

    // let writer2 = File::create("test.yaml").unwrap();
  }

  // pub fn load(path: &str) -> Result<File, io::Error> {
  //   File::open(&path)
  // }

  pub fn to_yvstring(string: &str) -> serde_yaml::Value {
    serde_yaml::Value::String(String::from(string))
  }
}

pub mod yaml_parser {
  impl super::YamlParser {}
}
