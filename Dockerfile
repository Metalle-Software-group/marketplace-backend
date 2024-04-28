FROM python:3.12-alpine3.19

WORKDIR /backend

COPY . .

EXPOSE 8000

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py makemigrations && python manage.py migrate
RUN python manage.py migrate --run-syncdb

ENTRYPOINT [ "python", "./manage.py" ,"runserver" ]