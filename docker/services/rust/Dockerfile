FROM rust:1.49
ARG UID

# ユーザーを作成
# ARG UID=1000
RUN useradd -m -u ${UID} docker

# 作成したユーザーに切り替える
USER ${UID}

# RUN apt-get -y update
