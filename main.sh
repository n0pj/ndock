#!/bin/bash
echo "script=" $0		#スクリプト名を表示
echo "count=" $#		#引数の個数を表示
echo "No.1=" $1			#1つ目の引数を表示
echo "No.2=" $2			#2つ目の引数を表示
echo "all=" $@

specify_env=$1
envs=('main' 'staging' 'master' 'ndock')

specify_order=$2
orders=('start' 'stop' 'setup')

# 省略されているか等の確認をして、デフォルトを設定
if [ "$specify_env" = '' ]; then
  specify_env="${envs[0]}"
  echo "Set default enviroment '${envs[0]}'"
fi
# for env in ${envs[@]}; do
#   if [ $env != $specify_env ]; then
#     echo 'Unknown enviroment. Current set enviroments is these '${envs[@]}
#     specify_env="${envs[0]}"
#     echo "Set default enviroment '${envs[0]}'"
#   fi
# done
function in_array_envs () {
  specify_env=$1
  envs=$2
  result=false
  for env in ${envs[@]}; do
    if [ $env = $specify_env ]; then
      result=true
      return $resu;t
    fi
  done
  return $result
}
test=in_array_envs $specify_env $envs
echo $test

# 省略されているか等の確認をして、デフォルトを設定
for order in ${orders[@]}; do
  if [ "$specify_order" = '' ]; then
    specify_order="${orders[0]}"
    echo "Set default order '${orders[0]}'"
    break
  fi

  if [ $env != $specify_order ]; then
    echo 'Unknown order. Current set orders is these '${orders[@]}
    specify_order="${orders[0]}"
    echo "Set default order '${orders[0]}'"
    break
  fi
done

# main の場合
if [ $env = 'main' ]; then
  case $order in
    'start' ) docker-compose -f docker-compose-develop.yml up -d ;;
    'stop' ) echo 'test' ;;
    * ) echo 'Fatal error.' ;;
  esac
fi