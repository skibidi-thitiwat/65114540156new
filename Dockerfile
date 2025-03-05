
FROM python:3.12.3

WORKDIR /Yowai

COPY . . 

RUN pip install --no-cache-dir -r requirements.txt


COPY . /Yowai/


EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
