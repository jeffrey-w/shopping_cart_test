FROM python

ENV PIP_ROOT_USER_ACTION=ignore
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py loaddata fixture.json
EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
