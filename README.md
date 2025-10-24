# FAST API

### Creating virtual environment

```
python -m venv .venv
```

### Activating virtual environment (cmd)

```
.venv\Script\activate.bat
```

### Dependencies

```
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv
```

fastapi
uvicorn - server running
sqlclchemy - ORM (object relational mapper) for db operation mapping
psycopg2-binary - driver to connect
python-dotnev - env management

Storing in requirements.txt file

> pip freeze > requirements.txt
