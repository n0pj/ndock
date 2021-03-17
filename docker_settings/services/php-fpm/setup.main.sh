#!/bin/bash
# add user
# cs_*.sh で指定した USER_ID( 引数 ) を受け取る
USER_ID=$1

# chown
chown -R ${USER_ID}:${USER_ID} node_modules && chown -R ${USER_ID}:${USER_ID} vendor
chown -R www:www-data storage/
chmod -R 774 storage/

# migration
# su -c "composer install" www
# su -c "php artisan migrate:fresh" www
# su -c "php artisan db:seed" www
# su -c "php artisan storage:link" www
# su -c "yarn" www
