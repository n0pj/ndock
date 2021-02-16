# <font color="Cyan">ndock</font>

このプロジェクトは、n0pj が docker, docker-compose を便利に簡単に、より汎用的に使用できるように作られたものである。

## tree

```
├── ndock ( cli tool )
├── .env.example // 最初に cp .env.example .env
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
    ├── home // django, node, rust 系のアプリを入れる
    │   └── django
    ├── logs
    │   ├── nginx
    │   │   ├── access.log
    │   │   └── error.log
    │   └── php-fpm
    ├── mysql
    │   ├── conf.d // mysql の conf.d にマウントする用
    │   │   ├── custom.cnf
    │   │   └── my.cnf
    │   ├── pool // データベースの pool
    │   │   ├── ca.pem
    │   │   ├── client-cert.pem
    │   │   ├── public_key.pem
    │   │   └── server-cert.pem
    │   └── sql // データベース初期実行 sql 用
    └── www // laravel や静的・動的なサイトを設置する用
```

## 特徴、目玉

・yaml の import が可能 ( ndock を挟む場合 )  
・.env を使用した、自動で USER_ID を設定 ( yaml には設定が必要 )  
・.env を使用した、env, command のデフォルト指定、設定すると、./ndock だけで起動ができる  
・.env を使用した、container_name を プロジェクトごとに一意な名前を設定できる  
・docker, docker-compose の長いコマンドをより短く簡単に使用できる  

## 使用方法、各コマンド

### ndock

基本的には、ndock バイナリを使用し、コマンド引数を指定して利用する。初期設定が完了していれば、これだけで起動できる。
```shell
./ndock
```
以下で .env のコピーを行う。
```
cp .env.example .env
```

最初は以下のコマンドで image のダウンロードと build、 container の作成と起動を行う。
```
./ndock -c up
```
以下で container の起動を行う。
```
./ndock -c start
```
止める時は以下で container の停止を行う。
```
./ndock -c stop
```
#### -e, --env

実行する環境を選択する。環境は以下の 4 種類となっている。  
・any  
・main ( 開発用 )  
・staging ( 仮本番用 )  
・master ( 本番用 )  
また、.env に DEFAULT_ENV を設定することで、-e, --env を短縮することができる。
この env を選択することにより、docker_settings の {env}.yaml が読み込まれる。

#### -c, --command

選択した環境によって、実行できるコマンドが異なる。

##### any

・stop  
docker stop \`docker ps -a -q\` と同等  
・rm  
docker rm \`docker ps -a -q\` と同等  
・rmi  
docker rmi \`docker images -q\` と同等  

##### main

・start  
docker-compose -f docker-compose.yaml start と同等  
・stop  
docker-compose -f docker-compose.yaml stop と同等  
・up  
docker-compose -f docker-compose.yaml up -d と同等  
・down  
docker-compose -f docker-compose.yaml down --rmi all --volumes --remove-orphans と同等  
・build  
docker-compose -f docker-compose.yaml build と同等  
・shell  
sh docker_settings/cs_{env}.sh と同等  

##### staging
main と同等

##### master
main と同等

## ndock の yaml import 機能
ndock では、ndock 内で yaml が使用される場合、以下のように書いた yaml は import 処理が行われる。  
※起点は ndock がある場所からとなる

```yaml
networks:
  network:
    driver: bridge
services:
  import: docker_settings/services/mysql/mysql.yaml
  import: docker_settings/services/nginx/nginx.yaml
  import: docker_settings/services/php-fpm/php-fpm.yaml
```
import: {file_name}.yaml と書くことで解析 -> 置換され、automated_{env}.yaml というファイルが生成される。
docker が実行される時は、この生成されたファイルが読み込まれる。
また、以下のように無限ループされる記述では、import ループ処理が 10 回 を超えた場合に強制的に終了され、その時点のデータが生成される。
```yaml
// test.yaml
services:
  import: docker_settings/services/mysql/mysql.yaml
 
// mysql.yaml
mysql:
  container_name: mysql
  import: docker_settings/services/mysql/mysql.yaml
```

## ndock の自動 USER_ID 設定機能
id -u で取得された id が .env の USER_ID=1000 のように設定される。
yaml 内では、以下のように指定することができる。
```yaml
command: bash -c 'usermod -o -u ${USER_ID} www-data; groupmod -o -g ${USER_ID} www-data; php-fpm'
```

## ndock の container_name 設定機能
ndock では、プロジェクトごとに container_name を変更する機能がある。.env に以下のように記述することで、
```
PROJECT_NAME=ndock_
```
以下のように設定されていた場合、
```
container_name: mysql
```
生成されるファイルでは、以下のように設定される。
```
container_name: ndock_mysql
```

## ndock の shell 機能
./ndock -c shell とすることで、docker_settings/cs_{env}.sh が読み込まれるようになっている。  
※起点は ndock がある場所からとなる
