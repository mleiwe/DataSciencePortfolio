FROM python:3.9-slim

RUN pip install pipenv
#Get the Pipfile to build the environment
WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

#Bring the predict script and model file
COPY ["predict.py", "model.bin", "./"]

#Expose the port
EXPOSE 9696

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "predict:app" ]
 