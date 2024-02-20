FROM python:alpine3.19

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt

RUN pip3 install requests

COPY . /app

#ENV FLASK_APP=app

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]