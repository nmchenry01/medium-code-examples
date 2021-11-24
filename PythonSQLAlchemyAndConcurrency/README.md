# Python, SQLAlchemy, and Concurrency

## Getting Started

The only requirement(s) to run this project are [Docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/).

To run the code examples start by running the following from the root of the `/PythonSQLAlchemyAndConcurrency` directory:

```sh
docker-compose up --build
```

Once the docker container is running, run the following to run bash in the running docker container:

```sh
docker exec -it python_sqlalchemy_and_concurrency_app bash
```

You should now have an bash shell running in the docker container. From here, you can run the python scripts as you normally would, IE:

```sh
python src/coroutine_1.py
python src/sqlalchemy_1.py
```
