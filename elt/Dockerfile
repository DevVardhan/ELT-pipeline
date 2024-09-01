FROM python:3.8-slim

RUN apt-get update && apt-get install -y postgresql-Client

COPY elt_script.py .

CMD [ "python" , "elt_script.py" ]