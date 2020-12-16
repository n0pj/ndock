# // この順でコマンド実行
# cd web
# git clone -b local https://github.com/shinroh/tz-concierge-web-management-version.git
# cd ../
# docker-compose -f docker-compose-develop.yml up -d
# docker exec -it ndock_tz_php bash -c '
# composer install &&
# php artisan migrate:fresh &&
# php artisan db:seed &&
# chown -R www-data:www-data storage/
# '
docker-compose -f ndock/ndock.yml up -d
