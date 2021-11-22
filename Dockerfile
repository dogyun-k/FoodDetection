FROM python:3.7

COPY . /app

RUN /usr/local/bin/python -m pip install --upgrade pip

WORKDIR /app

RUN pip3 install -r ./requirements.txt

CMD ["python3", "-m", "./server/flask", "run", "--host=0.0.0.0"]