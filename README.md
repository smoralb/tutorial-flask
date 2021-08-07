# Flask Cheatsheet

## ENV
- Deactivate env -> deactivate
- Run env (Windows 10) -> env\Scripts\activate.bat

## APP
- Debug mode on -> In ```run.py```, ```set "FLASK_ENV=development"```
- Run the app -> ```flask run``` or ```python -m flask run```

# CREATE NEW ENDPOINT
- Add the decorator ```route()``` to the function we want to use.

```
@app.route('/')
def hello_world(): return 'Hello, World!'
```