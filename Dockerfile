FROM python:3.9-slim


COPY . /usr/src/app
WORKDIR /usr/src/app



RUN pip install --user telebot
RUN pip install --user sqlite3
# run app
CMD ["python", "main.py"]


