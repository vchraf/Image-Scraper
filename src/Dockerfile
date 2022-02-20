FROM python:3.9

WORKDIR /scraper/src

COPY scrap.py .

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

CMD [ "python", "app.py" ]

