FROM python:3.8-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8000

#RUN pip install --no-cache-dir uvicorn gunicorn

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

COPY ./gunicorn_conf.py /gunicorn_conf.py

COPY ./start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh

# add requirements
COPY ./app/requirements.txt /app/requirements.txt

# install requirements
RUN pip install -r ./app/requirements.txt

#RUN pip install --no-cache-dir fastapi

COPY ./app /app
WORKDIR /app/
ENV PYTHONPATH=/app

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Uvicorn
CMD ["/start.sh"]

# expose
EXPOSE 8000