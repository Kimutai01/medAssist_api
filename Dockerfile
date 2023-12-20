FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirement.txt .

RUN pip install -r requirement.txt

COPY . .

EXPOSE 8001

CMD ["python", "manage.py", "runserver"]