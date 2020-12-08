# Quizzer

# Installation

    pipenv install --dev

    pipenv shell

    python manage.py makemigrations polls

    python manage.py migrate

    python manage.py runserver


# Docker

    docker build -t quizzer .

    docker run --rm -it -p 8000:8000 quizzer