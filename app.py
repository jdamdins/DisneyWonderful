import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from sqlalchemy import func, create_engine
app = Flask(__name__)
engine = create_engine("sqlite:///db/project2.sqlite")


# Heroku check
is_heroku = False
if 'IS_HEROKU' in os.environ:
    is_heroku = True

# Import your config file(s) and variable(s)
if is_heroku == False:
    from config import host, port, username, password, database 
else:
    host = os.environ.get('host')
    port = os.environ.get('port')
    username = os.environ.get('username')
    password = os.environ.get('password')
    database = os.environ.get('database')


@app.route("/")
def home():
    # Render Home Page
    return "Front_End_Page"

    
