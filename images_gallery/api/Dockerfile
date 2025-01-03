FROM python:3.9

WORKDIR /app

EXPOSE 5050

COPY Pipfile Pipfile.lock ./
COPY requirements.txt .

RUN pip install pipenv
#RUN pipenv requirements > requirements.txt
#RUN pipenv lock -r > requirements.txt
RUN pip install -r requirements.txt
RUN pipenv --version

COPY . ./

CMD ["python", "main.py"]