use clap::Arg;

pub struct Commands {}

impl Commands {
    pub fn env() -> Arg<'static, 'static> {
        Arg::with_name("env")
            .short("e")
            .long("env")
            .takes_value(true)
    }

    pub fn command() -> Arg<'static, 'static> {
        Arg::with_name("command")
            .short("c")
            .long("command")
            .takes_value(true)
    }

    pub fn uri() -> Arg<'static, 'static> {
        Arg::with_name("uri")
            .short("u")
            .long("uri")
            .takes_value(true)
    }

    pub fn branch() -> Arg<'static, 'static> {
        Arg::with_name("branch")
            .short("b")
            .long("branch")
            .takes_value(true)
    }
}

pub mod commands {
    impl super::Commands {}
}
