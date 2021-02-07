use dotenv;
use std::env;

struct EnvParser {}

impl EnvParser {
  pub fn new() -> Self {
    Self {}
  }

  pub fn save() {}
}

pub mod env_parser {
  impl super::EnvParser {}
}
