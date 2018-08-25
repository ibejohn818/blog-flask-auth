# Flask Auth Demo

Demo for blog post

[https://johnchardy.com/blog/flask-authentication-authorization/class-based-decorator.html](https://johnchardy.com/blog/flask-authentication-authorization/class-based-decorator.html) https://johnchardy.com/blog/flask-authentication-authorization/class-based-decorator.html

## Requirements
- [Docker](https://www.docker.com/get-started) Docker
- Docker Compose[Docker Compose](https://docs.docker.com/compose/install/) 

## Instructions

To run the demonstration first build the docker images

`docker-compose build`

Then run the demo by starting the docker compose stack

`docker-compose up`

When the stack is running, visit the demo by opening a web browser and navigating to http://localhost (http://127.0.0.0 http://0.0.0.0)

There you can mock a login session and groups and click the links to view the auth responses.

The flask server is running in hot reload so if you edit the flask app or authorize decorator the flask server will restart.