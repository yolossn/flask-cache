FROM ubuntu:latest

WORKDIR /app

COPY requirements.txt .

RUN apt update
RUN apt -y upgrade
RUN apt -y  install libmemcached-dev systemd
RUN apt -y install python3 python3-pip
RUN python3 -m pip install -r requirements.txt

RUN apt -y install memcached
COPY . .
COPY .flaskenv .

EXPOSE 5000
RUN chmod +x init.sh
CMD "./init.sh"