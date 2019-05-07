FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN pip install -U pip 
RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/app/static
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
ADD . /usr/src/app/
#CMD ["python3", "manage.py", "collectstatic" , "--noinput" ]
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["python", "manage.py", "makemigrations"]
# CMD ["python", "manage.py", "migrate"]