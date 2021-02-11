# <font color="Cyan">ndock</font>

このプロジェクトは、n0pj が docker, docker-compose を便利に簡単に、より汎用的に使用できるように作られたものである。

## tree

```
├── README.md
├── docker_settings // docker 向けの設定ディレクトリ
│   ├── cs_main.sh // main の ./ndock -e main -c shell で実行される custom_shell
│   ├── cs_master.sh // 上と同様
│   ├── cs_staging.sh // 上と同様
│   ├── main.yaml // main の docker-compose file、ここには import 文を書くことができる
│   ├── master.yaml // 上と同様
│   ├── staging.yaml // 上と同様
│   └── services // ここに各 service が入る
│       ├── express
│       │   ├── Dockerfile
│       │   ├── entrypoint.sh
│           └── express.yaml // 各 service には import 用の yaml を作成するのが好ましい
└── volumes // www, home, log など、各種マウントするためのディレクトリ
    ├── home
    │   └── django
    ├── logs
    │   ├── nginx
    │   │   ├── access.log
    │   │   └── error.log
    │   └── php-fpm
    ├── mysql
    │   ├── conf.d
    │   │   ├── custom.cnf
    │   │   └── my.cnf
    │   ├── pool
    │   │   ├── ca.pem
    │   │   ├── client-cert.pem
    │   │   ├── public_key.pem
    │   │   └── server-cert.pem
    │   └── sql
    └── www
```

## 特徴、目玉

・yaml の import が可能 ( ndock を挟む場合 )
・.env を使用した、自動で USER_ID を設定 ( yaml には設定が必要 )
・.env を使用した、env, command のデフォルト指定、設定すると、./ndock だけで起動ができる
・.env を使用した、container_name を プロジェクトごとに一意な名前を設定できる
・docker, docker-compose の長いコマンドをより短く簡単に使用できる

## 使用方法、各コマンド

### ndock

基本的には、ndock バイナリを使用し、コマンド引数を指定して利用する。

```shell
./ndock
```

#### -e, --env

実行する環境を選択する。環境は以下の 4 種類となっている。
・any
・main ( 開発用 )
・staging ( 仮本番用 )
・master ( 本番用 )
なお、.env に DEFAULT_ENV を設定することで、-e, --env を短縮することができる。
この env を選択することにより、docker_settings の {env}.yaml が読み込まれる。

#### -c, --command

選択した環境によって、実行できるコマンドが異なる。

##### any

・stop
・rm
・rmi

##### main

##### staging

##### master
