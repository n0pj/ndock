use super::commands::Commands;
use clap::App;
use colored::*;

pub struct ArgParser {}

impl ArgParser {
    pub fn new() -> App<'static, 'static> {
        println!("{}", "ArgParser loaded ... ".green());

        App::new(crate_name!())
            .version(crate_version!())
            .author(crate_authors!())
            .about(crate_description!())
            .arg(Commands::env())
            .arg(Commands::command())
            .arg(Commands::uri())
            .arg(Commands::branch())
    }
}

pub mod arg_parser {
    impl super::ArgParser {}
}
