# // この順でコマンド実行
cd web
git clone https://github.com/shinroh/trust-jv-dealer-system.git
cd ../
docker-compose -f docker-compose-develop.yml up -d
docker exec -it php bash -c '
composer install &&
php artisan migrate:fresh &&
php artisan db:seed &&
chown -R www-data:www-data storage/
'
