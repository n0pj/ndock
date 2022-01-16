FROM rust:1.57
ARG USER_ID
# RUN apt-get -y update

USER ${USER_ID}:${USER_ID}

# RUN apt install -y libmysqlclient-dev
RUN cargo install cargo-watch
RUN cargo install diesel_cli --no-default-features --features mysql

# # ユーザーを作成
# # ARG USER_ID=1000
# RUN useradd -m -u ${USER_ID} rust

# # 作成したユーザーに切り替える
# USER ${USER_ID}

# ENV USER=rust

WORKDIR /code
