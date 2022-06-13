# Use an existing image as a base
FROM python:3.9


# The WORKDIR command is used to define the working directory 
# of a Docker container at any given time. The command is specified in the Dockerfile. 
# Reference : https://www.educative.io/edpresso/what-is-the-workdir-command-in-docker
 # WORKDIR '/backend' 
WORKDIR /usr/src/app



# COPY is a dockerfile command that copies files from a local source location
# to a destination in the Docker container. 
# A Dockerfile is a text file with instructions to set up a Docker container.
# Reference: https://www.educative.io/edpresso/how-to-use-copy-in-docker
# 

# This command will copy "requirements.txt" file to the /requirements.
# COPY <src> <dest>
COPY requirements.txt  ./
# Download and install dependencies 
RUN pip install --no-cache-dir -r requirements.txt


#COPY ./app  /code/app
# 
COPY .  .   

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
#CMD ["uvicorn", "main:app"]








