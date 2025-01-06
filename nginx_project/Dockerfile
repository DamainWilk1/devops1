FROM ubuntu:24.04

RUN apt update -y && apt install -y nginx nano

WORKDIR /var/www/html

COPY index.html .

EXPOSE 8080

CMD ["nginx","-g","daemon off;"]
