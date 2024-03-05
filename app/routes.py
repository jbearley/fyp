from app import app
from flask import render_template
import sys

sys.path.append("app")
from dummy_data import random_classes_by_semester


majors = [
    "Anthropology and Sociology",
    "Astronomy",
    "Biochemistry, Cell and Molecular Biology",
    "Biology",
    "Chemistry",
    "Computer Science",
    "Data Analytics",
    "English",
    "Environmental Science",
    "History",
    "International Relations",
    "English",
    "Writing",
    "Rhetoric and Media Studies",
    "Environmental Science",
    "History",
    "International Relations",
    "Kinesiology",
    "Law, Politics and Society",
    "Mathematics",
    "Mathematics Education (Secondary)",
]
minors = [
    "Anthropology",
    "Biology",
    "Chemistry",
    "Computer Science",
    "Cybersecurity",
    "Data Analytics",
    "English",
    "Writing",
    "Rhetoric and Media Studies",
    "History",
    "International Relations",
    "Mathematics",
    "Mathematics Education (Secondary)",
    "Military Studies",
]
concentrations = [
    "Behavior Analysis of Developmental Disabilities",
    "Biophysics",
    "Comparative Animal Behavior",
    "Global and Comparative Public Health",
    "Human Resources Management",
    "Interdisciplinary Study of the Humanities and Sciences",
    "Global and Comparative Public Health",
    "Human Resources Management",
    "Interdisciplinary Study of the Humanities and Sciences",
]
# complete from this link https://www.drake.edu/academics/undergraduate/majors/ up to "Military Studies" (from "College / School Listing" view)
drake_curriculum = {
    "majors": majors,
    "minors": minors,
    "concentrations": concentrations,
}
user_choices = {
    "majors": ["Computer Science", "English", "Anthropology and Sociology"],
    "minors": [],
    "concentrations": []
}

@app.route("/")
@app.route("/index")
def index():
    styles_to_enqueue = ["main.css"]
    scripts_to_enqueue = ["main.js"]
    return render_template(
        "main.html",
        title="Drake Four-Year Plan Generator",
        classes_by_semester=random_classes_by_semester(),
        drake_curriculum=drake_curriculum,
        user_choices=user_choices,
        styles_to_enqueue=styles_to_enqueue,
        scripts_to_enqueue=scripts_to_enqueue,
    )
