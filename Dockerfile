FROM python:3.9
COPY requirements.txt .
RUN pip install --quiet -r requirements.txt
COPY . .
EXPOSE 8000
RUN python manage.py migrate polls
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]