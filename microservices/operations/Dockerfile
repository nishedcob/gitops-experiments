
FROM python:3.5

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY base_app.py .

CMD [ "python", "./base_app.py" ]
