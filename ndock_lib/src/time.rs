use chrono::format::{DelayedFormat, StrftimeItems};
use chrono::Local;

pub struct Time {}

impl Time {
  pub fn now(time: Option<&'static str>) -> DelayedFormat<StrftimeItems<'static>> {
    Local::now().format(time.unwrap_or("%H:%M:%S"))
  }

  pub fn to_string(time: DelayedFormat<StrftimeItems<'static>>) -> String {
    format!("{}", time)
  }
}

pub mod time {
  impl super::Time {}
}
