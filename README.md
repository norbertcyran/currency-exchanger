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

#### Fixer.io API
To fetch currency rates every hour from Fixer.io API,
[create a free account](https://fixer.io/product). After you get your account,
in the `backend` directory create `.env` file, inside provide your API key:
```dotenv
FIXER_IO_API_KEY=<your-api-key>
```
Now, restart the application and now currency rates will be fetched every hour.

To fetch currency rates right away, use `python manage.py update_currency_rates`.

**WARNING**: Do not commit your `.env` file.

### Polygon.io API
To fetch stock prices once a day(from two days ago),
[create an account](https://polygon.io/). After you get an account,
in the `backend` directory create `.env` file, inside provide your API key:
```dotenv
POLYGON_IO_API_KEY=<your-api-key>
```
Restart an app and stocks will be fetched once a day.

To fetch stocks right away, use `python manage.py update_stocks`

**WARNING**: Do not commit your `.env` file.




#### Pre-commit hooks
To run linters and formatters before each commit, run:
```shell script
pre-commit install
```
To run linters and formatters for all files, run:
```shell script
pre-commit run --all
```
