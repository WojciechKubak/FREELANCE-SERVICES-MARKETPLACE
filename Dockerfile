FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY /Pipfile.lock /Pipfile /app/
RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile
COPY . /app

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "app", "app.wsgi:application", "--reload"]
