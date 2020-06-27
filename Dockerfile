FROM python:3.8
ENV PYTHONBUFFERED 1

RUN mkdir /app
WORKDIR /app

EXPOSE 9000

COPY requirments.txt /app/
RUN pip install -r requirments.txt
COPY . /app/

CMD [ "python", "start.py" ]