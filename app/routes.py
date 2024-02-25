from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    data = {'key1': 'value1'}
    styles_to_enqueue = ['main.css']
    scripts_to_enqueue = ['main.js']
    return render_template('main.html', title="Drake Four-Year Plan Generator", data=data, styles_to_enqueue=styles_to_enqueue, scripts_to_enqueue=scripts_to_enqueue)
