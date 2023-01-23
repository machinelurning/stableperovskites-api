FROM python:3.8.15

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR /opt/stableperovskites-api

ADD ./stableperovskites-api /opt/stableperovskites-api
RUN pip install --upgrade pip
RUN pip install -r /opt/stableperovskites-api/requirements.txt

RUN chmod +x /opt/stableperovskites-api/run.sh
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

EXPOSE 8001

CMD ["bash", "./run.sh"]