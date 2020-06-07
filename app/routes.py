from app import app
from flask import render_template
from sqlalchemy

@app.route("/")
@app.route("/index")
def index():
    return "here we go!"