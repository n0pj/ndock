FROM python:3
ENV PYTHONUNBUFFERED 1
# RUN mkdir /code
# WORKDIR /code
# RUN pip install -r requirements.txt
RUN apt-get -y update
# django を動かすには、↓ がいる
# sudo apt install python3-dev
# sudo apt install libmysqlclient-dev

# debian だとちょっと違う？これだった。libmariadb-dev-compat libmariadb-dev
RUN apt-get install -y python3-dev
RUN apt-get install -y libmariadb-dev-compat libmariadb-dev