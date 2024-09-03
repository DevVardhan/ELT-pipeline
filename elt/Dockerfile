FROM python:3.8-slim

RUN apt-get update && apt-get install -y postgresql-client cron

COPY start.sh/app/start.sh .
COPY elt_script.py .

WORKDIR /app

# runs the cron job at 3 am every day
RUN echo "0 3 * * * python/app/elt_script.py" | crontab -
CMD [ "python" , "elt_script.py" ]