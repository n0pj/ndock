FROM php:7.2.34-fpm

RUN apt update
RUN apt install -y wget git unzip

# Install Node.js 12
# RUN apt install -y npm \
#   && npm install n -g \
#   && n 12

# RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - \
#  && apt install -y nodejs

# Copy php-fpm conf
RUN mkdir -p /var/log/php-fpm
COPY docker.conf /usr/local/etc/php-fpm.d/

# 何かソースからビルドする PHP Extensions を入れたい場合
# RUN apk --no-cache add icu-dev autoconf make g++ gcc

# Install PHP Extensions
RUN apt install -y zlib1g-dev default-mysql-client libonig-dev libzip-dev zip unzip libjpeg-dev libfreetype6-dev
RUN apt install -y libmagick++-dev libmagickwand-dev libpq-dev libfreetype6-dev libjpeg62-turbo-dev libpng-dev libwebp-dev libxpm-dev
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/
RUN docker-php-ext-install -j$(nproc) zip gd mysqli pdo_mysql mbstring

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer
RUN composer self-update

WORKDIR /var/www/tz-concierge-web-management-version

# php-fpmはデフォルトのユーザwww-dataで動く。https://stackoverflow.com/questions/48619445/permission-denied-error-using-laravel-docker
# 変更する場合は /usr/local/etc/php-fpm.d/www.conf でユーザー名を変える。
RUN chown -R www-data:www-data /var/www

RUN composer global require "laravel/installer"
