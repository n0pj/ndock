USER_ID=`id -u`
docker-compose -f docker_settings/automated_main.yaml exec php-fpm bash -c "bash /setup.sh ${USER_ID}"
