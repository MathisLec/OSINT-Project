FROM python:latest

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

COPY ./resources .

# install dependencies
RUN pip install -r requirements.txt

RUN mkdir /code/scans

# copy the content of the local src directory to the working directory
COPY ./ .

# command to run on container start
CMD [ "python", "./main.py" ]