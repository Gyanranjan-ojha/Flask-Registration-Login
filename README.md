
# Project Title

A brief description of what this project does and who it's for


# Flask Login and Registraion

1. The primary objective of this project would be to build a Login and Registraion System with full authentication.

2. When a new user is registered the user details will be save in MySQL database localhost server and when a user is about to login then authentication will be check from saved data.

## create a .env credentials with details
**Database:** MySQL Database

```
MYSQL_USER=<user_name>
MYSQL_DB=<db_name>
MYSQL_HOST=localhost
MYSQL_PASSWORD=<user_password>
MYSQL_PORT=3306
SQLALCHEMY_DATABASE_URI=mysql+pymysql://<user_name>:<user_password>@localhost:3306/<db_name>
```
## create a .flaskenv credentials with details
```
FLASK_APP=wsgi.py
FLASK_SKIP_DOTENV=1
FLASK_ENV=development
FLASK_DEBUG=1
FLASK_RUN_HOST=127.0.0.1
FLASK_RUN_PORT=5000
SECRET_KEY=''
```

## Run Locally

Clone the project

```bash
  git clone https://github.com/Gyanranjan-ojha/Flask-Registration-Login.git
```

Go to the project directory

```bash
  cd Flask-Registration-Login
```

create a virtual environment
```bash
  python/python3 -m venv venv
```

activate the virtual environment
```bash
  .\venv\Scripts\activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  flask run
```

Given database name in .env file will be going to create automatically if not exists.

## Tech Stack

**Client:** HTML, CSS, Bootstrap,Javascript

**Server:** Flask

**Database:** MySQL Database