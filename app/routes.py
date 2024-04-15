from app import app
from flask import render_template, request
import sys

sys.path.append("app")  # This must be called before importing below modules
from app.random_dummy_data import Dummy_Data
from app.static_dummy_data import drake_curriculum

# We receive lists represented as strings in the URL and convert them to python lists
from util import serialize


@app.route("/")
def index():
    # User's inputs that are going to be applied to this render
    user_choices = {
        "majors": (
            serialize(request.args.get("majors")) if request.args.get("majors") else []
        ),
        "minors": (
            serialize(request.args.get("minors")) if request.args.get("minors") else []
        ),
        "concentrations": (
            serialize(request.args.get("concentrations"))
            if request.args.get("concentrations")
            else []
        ),
    }
    print(user_choices)
    data = Dummy_Data(user_choices)  # Dummy data!! Replace this with real FYP
    styles_to_enqueue = ["main.css"]
    scripts_to_enqueue = ["main.js"]
    return render_template(
        "main.html",
        title="Drake Four-Year Plan Generator",
        classes_by_semester=data.get_FYP(),
        requirements=data.get_requirements(),
        drake_curriculum=drake_curriculum,
        user_choices=user_choices,
        styles_to_enqueue=styles_to_enqueue,
        scripts_to_enqueue=scripts_to_enqueue,
    )
