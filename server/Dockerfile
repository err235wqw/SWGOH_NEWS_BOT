FROM python:3.13-slim
COPY requirements.txt .
RUN pip install -r server/requirements.txt
ADD server.py /server/
WORKDIR /server/