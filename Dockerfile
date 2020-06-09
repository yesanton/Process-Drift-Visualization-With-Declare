# Use the official image as a parent image.
FROM openjdk:10-jdk

# Set the working directory.
WORKDIR /app

RUN apt-get update && apt-get -y install \
	python3-pip \
        && apt-get clean \
        && rm -rf /tmp/* /var/tmp/* \
        && rm -rf /var/lib/apt/lists/*

# Copy python package requirements
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the file from your host to your current location.
COPY . .

ENV FLASK_APP /app/src/scenarios_server.py

ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]

# that is how i run it
#   docker run -it  --name flaskcont -p 5000:5000 -d <image ID or name>
#   docker start flaskcont
#   docker  exec -it flaskcont bash (to get to the shell)
