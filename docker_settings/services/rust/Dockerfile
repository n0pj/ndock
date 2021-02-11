FROM rust:1.49
ARG USER_ID

# ユーザーを作成
# ARG USER_ID=1000
RUN useradd -m -u ${USER_ID} docker

# 作成したユーザーに切り替える
USER ${USER_ID}

# RUN apt-get -y update
