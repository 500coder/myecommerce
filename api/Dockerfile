FROM python:3.9.22-alpine3.21

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 5000

CMD  ["flask", "run"] 


