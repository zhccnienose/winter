FROM python:3.11

WORKDIR /warmup
COPY . .

EXPOSE 5000

ENV FLASK_DEBUG=True \
    FLASK_APP=run.py \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_ENV=development \
    SECRET_KEY="secret_key" \
    JWT_SECRET_KEY="jwt_secret_key" \
    MYSQL_USER_NAME=root \
    MYSQL_USER_PASSWORD=310257813 \
    MYSQL_HOSTNAME=47.115.212.55 \
    MYSQL_PORT=3306 \
    MYSQL_DATABASE_NAME=winter


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN flask db migrate
RUN flask db upgrade

CMD ["flask","--app","run","run"]
