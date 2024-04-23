# Shopping Cart Test

A simple application that simulates an online shopping cart.

## Installation and Running

The application may be built and run locally or in a container.

### Local Installation

First, create a virtual environment and activate it.

```
python -m venv .venv
```

```
source .venv/bin/activate
```

Next install the application's dependencies.

```
pip install -r requirements.txt
```

Finally, set up the database and run the application.

```
python manage.py makemigrations
```

```
python manage.py migrate
```

```
python manage.py loaddata fixture.json
```

```
python manage.py runserver
```

### Running in a Container

To build and run the application with Docker, issue the following commands.

```
docker build . -t cart-app
```

```
docker run -p 8000:8000 cart-app:latest
```

Whether you are running the application locally or in a container, you may reach it in your browser at [localhost:8000/cart](localhost:8000/cart).

## Testing

Unit tests may be run with the command `python manage.py test`.
