# Use the official image as a parent image.
FROM openjdk:10-jdk

# Set the working directory.
WORKDIR /usr/src/app

# Run the command inside your image filesystem.
# run all things to install packages and python, everything put in one run
#RUN npm install

RUN apt-get update && apt-get -y install python3-pip && pip3 install Flask && pip3 install -U scikit-learn && pip3 install ruptures && pip3 install matplotlib && pip3 install seaborn && pip3 install pm4py


# Copy the file from your host to your current location.
COPY . .

# Inform Docker that the container is listening on the specified port at runtime.
EXPOSE 5000

# Run the specified command within the container.
#CMD [ "npm", "start" ]

CMD [ "cd", "src"]
CMD [ "export", "FLASK_APP=scenario_1.py" ]
CMD ["flask", "run"]
# export FLASK_APP=scenario_1.py
#??? to make debug
# export FLASK_ENV=development
#flask run


# that is how i run it
#   docker run -it  --name flaskcont -p 5000:5000 -d 8ce42d1b8b80
#   docker start flaskcont
#   docker  exec -it flaskcont bash
