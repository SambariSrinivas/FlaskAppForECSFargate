FROM python:3.8.18-slim

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8081 

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]

