FROM python:3.8.5-alpine
COPY . /app
WORKDIR /app
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev
RUN pip install --upgrade pip
RUN pip install pymysql
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["clase04p/server.py"]
