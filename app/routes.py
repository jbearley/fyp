from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    data = {'key1': 'value1'}
    return render_template('main.html', title="Drake Four-Year Plan Generator", data=data)
