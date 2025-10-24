# FAST API

### Creating virtual environment

```
python -m venv .venv
```

### Activating virtual environment (cmd)

```
.venv\Scripts\activate.bat
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

### For running

```
uvicorn {main file}:app --host 0.0.0.0 --port 8000 --reload
```

> uvicorn main:app --host 0.0.0.0 --port 8000 --reload
