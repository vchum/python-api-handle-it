FROM python:3

WORKDIR /app

COPY app/requirements.txt requirements.txt 

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP="main"

COPY app/ .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]