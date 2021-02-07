#[macro_use]
extern crate clap;
extern crate ndock_lib;
use clap::{App, Arg, SubCommand};

fn main() {
    let app = App::new(crate_name!())
        .version(crate_version!()) // バージョン情報
        .author(crate_authors!()) // 作者情報
        .about(crate_description!()) // このアプリについて
        .arg(
            Arg::with_name("env") // 位置引数を定義
                .help("sample positional argument") // ヘルプメッセージ
                .required(true), // この引数は必須であることを定義
        )
        .arg(
            Arg::with_name("flg") // フラグを定義
                .help("sample flag") // ヘルプメッセージ
                .short("f") // ショートコマンド
                .long("flag"), // ロングコマンド
        )
        .arg(
            Arg::with_name("opt") // オプションを定義
                .help("sample option") // ヘルプメッセージ
                .short("o") // ショートコマンド
                .long("opt") // ロングコマンド
                .takes_value(true), // 値を持つことを定義
        )
        .subcommand(
            SubCommand::with_name("sub") // サブコマンドを定義
                .about("sample subcommand") // このサブコマンドについて
                .arg(
                    Arg::with_name("subflg") // フラグを定義
                        .help("sample flag by sub") // ヘルプメッセージ
                        .short("f") // ショートコマンド
                        .long("flag"), // ロングコマンド
                ),
        );

    let matches = app.get_matches();

    if let Some(o) = matches.value_of("pa") {
        println!("{}", o)
    }
    println!(
        "flag is {}",
        if matches.is_present("flg") {
            "on"
        } else {
            "off"
        }
    );

    if let Some(ref matches) = matches.subcommand_matches("sub") {
        println!("subcom detect");

        println!(
            "subflg is {}",
            if matches.is_present("subflg") {
                "on"
            } else {
                "off"
            }
        )
    }
}
