# solar water heater simulation
To run the web app, please first make sure the docker is installed, and then download the <code>docker-compose.yml</code> file in this repo. And then in the same directory where <code>docker-compose.yml</code> is, run the commands:

```console
docker-compose up -d # start the services
```
The docker will automatically download the two image for backend and frontend which is on [docker hub](https://hub.docker.com/repository/docker/jw979/solar-heater/general).

The frontend will then be running on <code>http://localhost:8080/</code>, 
and the backend will be running on <code>http://localhost:8000/</code>.

<br>
To stop the web app, run the command.

```console
docker-compose down # stop the services
```
