# currency-exchanger
Web application for currency exchanges, money transfers and stock trading. Academical

### Install
#### Backend
1. Install [poetry](https://github.com/python-poetry/poetry)
2. `cd backend`
3. Run `poetry install`
4. Run `poetry shell`

### Frontend
1. Make sure yarn is installed
2. Run `yarn install`

### Docker
Recommended setup

1. Install [docker](https://docs.docker.com/get-docker/)
and [docker-compose](https://docs.docker.com/compose/install/)
2. Build the images, in the project root:
    ```shell script
    docker-compose build
    ```
3. Run containers:
    ```shell script
    docker-compose up
    ```
4. To run the migrations:
    ```shell script
    docker-compose exec backend python manage.py migrate
    ```

#### Pre-commit hooks
To run linters and formatters before each commit, run:
```shell script
pre-commit install
```
To run linters and formatters for all files, run:
```shell script
pre-commit run --all
```
