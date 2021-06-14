FROM php:7.4.12-fpm

RUN apt-get update
RUN apt-get install -y wget git unzip

# Install Node.js 12
# RUN apt-get install -y npm \
#   && npm install n -g \
#   && n 12

# RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - \
#  && apt-get install -y nodejs

# Copy php-fpm conf
RUN mkdir -p /var/log/php-fpm
COPY docker.conf /usr/local/etc/php-fpm.d/

# 何かソースからビルドする PHP Extensions を入れたい場合
# RUN apk --no-cache add icu-dev autoconf make g++ gcc

# Install PHP Extensions
RUN apt-get install -y zlib1g-dev default-mysql-client libonig-dev libzip-dev zip unzip libjpeg-dev libfreetype6-dev
RUN apt-get install -y libmagick++-dev libmagickwand-dev libpq-dev libfreetype6-dev libjpeg62-turbo-dev libpng-dev libwebp-dev libxpm-dev
RUN docker-php-ext-configure gd --with-freetype=/usr/include/ --with-jpeg=/usr/include/
RUN docker-php-ext-install -j$(nproc) zip gd mysqli pdo_mysql mbstring

# Install Composer
# RUN curl -sS https://getcomposer.org/installer | php
# RUN mv composer.phar /usr/local/bin/composer
# RUN composer self-update

WORKDIR /var/www

# php-fpmはデフォルトのユーザwww-dataで動く。https://stackoverflow.com/questions/48619445/permission-denied-error-using-laravel-docker
# 変更する場合は /usr/local/etc/php-fpm.d/www.conf でユーザー名を変える。
# args の USER_ID を取得
ARG USER_ID
# shell でやっていたのを image 作成時に
RUN useradd -u $USER_ID -s /bin/bash www && mkdir -p /home/www && chown $USER_ID:$USER_ID /home/www
RUN adduser www www-data
RUN chown -R www:www-data /var/www

# RUN composer global require "laravel/installer"