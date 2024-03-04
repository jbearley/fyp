from app import app
from flask import render_template
import sys
sys.path.append("app")
from dummy_data import random_classes_by_semester


@app.route("/")
@app.route("/index")
def index():
    styles_to_enqueue = ["main.css"]
    scripts_to_enqueue = ["main.js"]
    return render_template(
        "main.html",
        title="Drake Four-Year Plan Generator",
        classes_by_semester=random_classes_by_semester(),
        styles_to_enqueue=styles_to_enqueue,
        scripts_to_enqueue=scripts_to_enqueue,
    )
