extern crate ndock_lib;
// use ndock_lib::ArgParser;
use ndock_lib::NDock;
// use ndock_lib::YamlParser;

fn main() {
    let ndock = NDock::new();
    ndock.run();
    ndock.drop()
}
