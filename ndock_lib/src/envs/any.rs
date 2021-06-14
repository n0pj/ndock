use crate::envs::Env;
use crate::Time;
use colored::*;
// use eval::eval;
// use regex::Regex;
// use std::env;
// use std::fs::copy;
// use fs_extra::dir::copy;
use fs_extra::copy_items;
use fs_extra::dir::CopyOptions;
// use std::path::Path;
use std::process::Command;

pub struct Any {
    pub env: String,
    pub command: Option<AllowCommand>,
    pub load_file: String,
    pub shell_file: String,
}

pub enum AllowCommand {
    Stop,
    Rm,
    Rmi,
    SetupWordPress,
    // ForceRM,
    // ForceRMI
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
                self.command = Some(AllowCommand::Rm);
            }
            "rmi" => {
                self.command = Some(AllowCommand::Rmi);
            }
            "setup-wordpress" => {
                self.command = Some(AllowCommand::SetupWordPress);
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
                    "stop, rm, rmi, setup-wordpress".green()
                );
                panic!()
            }
        }
    }

    fn run(&self) {
        let command = &self.command;
        match command {
            Some(AllowCommand::Stop) => self.stop(),
            Some(AllowCommand::Rm) => self.rm(),
            Some(AllowCommand::Rmi) => self.rmi(),
            Some(AllowCommand::SetupWordPress) => self.setup_wordpress(),
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

    fn setup_wordpress(&self) {
        self.change_directory("volumes/www");

        println!(
            "[{}] Download files ... ",
            Time::to_string(Time::now(None)).cyan(),
        );
        Command::new("curl")
            .arg("-O")
            .arg("https://ja.wordpress.org/latest-ja.tar.gz")
            .status()
            .expect("error");
        println!(
            "[{}] Download files ... {}",
            Time::to_string(Time::now(None)).cyan(),
            "done".green()
        );

        println!(
            "[{}] Extract files ... ",
            Time::to_string(Time::now(None)).cyan(),
        );
        Command::new("tar")
            .arg("-zxvf")
            .arg("latest-ja.tar.gz")
            .output()
            .expect("error");
        println!(
            "[{}] Extract files ... {}",
            Time::to_string(Time::now(None)).cyan(),
            "done".green()
        );

        println!("┌---------------------------------------┐");
        println!("|      Please execute next command      |");
        println!("|      {}            |", "./ndock -e main -c up".green());
        println!("└---------------------------------------┘");

        println!(
            "[{}] Setup WordPress  ... {}",
            Time::to_string(Time::now(None)).cyan(),
            "done".green()
        );

        self.change_directory("../../");

        let nginx_copy_result = vec!["volumes/setup_files/wordpress/nginx"];
        let php_fpm_copy_result = vec!["volumes/setup_files/wordpress/php-fpm"];
        let wordpress_copy_result = vec!["volumes/setup_files/wordpress/wordpress"];

        let mut dir_options = CopyOptions::new();
        dir_options.overwrite = true;

        println!(
            "[{}] Copy files ... ",
            Time::to_string(Time::now(None)).cyan(),
        );

        copy_items(&nginx_copy_result, "docker_settings/services", &dir_options)
            .expect("nginx files copy error");
        copy_items(
            &php_fpm_copy_result,
            "docker_settings/services",
            &dir_options,
        )
        .expect("php-fpm files copy error");
        copy_items(&wordpress_copy_result, "volumes/www", &dir_options)
            .expect("wordpress files copy error");

        println!(
            "[{}] Copy files ... {}",
            Time::to_string(Time::now(None)).cyan(),
            "done".green()
        );
        // Command::new("./ndock")
        //     .arg("-c")
        //     .arg("up")
        //     .status()
        //     .expect("error");
    }
}

pub mod any {
    impl super::Any {}
}
