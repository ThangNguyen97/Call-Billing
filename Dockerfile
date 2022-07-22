FROM python:3.7-slim

COPY ./requirements.txt /requirements.txt
COPY ./src /src
RUN pip3 install -r ./requirements.txt

WORKDIR /src

CMD ["python3", "app.py"]

EXPOSE 6868
