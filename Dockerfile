FROM python:3.11

RUN pip install --upgrade pip

WORKDIR /warmup

COPY . /warmup

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask","--app","run","run"]
