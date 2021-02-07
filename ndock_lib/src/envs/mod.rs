pub mod any;
pub mod main;
pub mod master;
pub mod staging;

pub use any::Any;
pub use main::Main;
pub use master::Master;
pub use staging::Staging;

pub trait Env {
  fn env(&self) {}
  fn command(&mut self, command: &str) {}
  fn run(&self) {}
  fn test(&self) {}
  fn start(&self) {}
  fn stop(&self) {}
  fn up(&self) {}
  fn down(&self) {}
  fn build(&self) {}
  fn shell(&self) {}
}
