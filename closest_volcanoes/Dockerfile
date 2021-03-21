FROM python:3.6-alpine

EXPOSE 8000

RUN apk add --no-cache gcc python3-dev musl-dev

ADD . /geodjango-volcanoes

WORKDIR /geodjango-volcanoes

RUN pip install -r requirements.txt

RUN python closest_volcanoes/manage.py makemigrations

RUN python closest_volcanoes/manage.py migrate

CMD [ "python", "closest_volcanoes/manage.py", "runserver", "0.0.0.0:8000" ]