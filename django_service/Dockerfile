FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/app/static
WORKDIR /usr/src/app
#COPY Pipfile /usr/src/app/
#RUN apk update \
#  && apk add --virtual build-tools gcc python3-dev musl-dev \
#  && apk add postgresql-dev
#RUN pip install pipenv
#RUN pipenv lock --pre
#RUN pipenv install --system --dev
#RUN pipenv install --system --deploy
#RUN apk del build-tools
COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
ADD . /usr/src/app/
#CMD ["python3", "manage.py", "collectstatic" , "--noinput" ]
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]