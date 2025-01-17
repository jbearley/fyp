from app import app
from flask import render_template, request
import sys
from placement_algorithm import *
from Jacob import *
from collections import OrderedDict
from operator import itemgetter
from class_prereqs_score import class_prereqs_score
from class_is_prereq_score import class_is_prereq_score
from dictionaries2 import *
from finalizeSchedule import *
from reqsFormat import *

sys.path.append("app")  # This must be called before importing below modules
from app.static_data import drake_curriculum

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
        "classes": serialize(request.args.get("classes")) if request.args.get("classes") else [],
        "semesters": request.args.get("semesters") if request.args.get("semesters") else ""
    }
    try:
        majors = []
        for major in user_choices["majors"]:
            majors.append(major.upper())
        if majors == []:
            majors.append("ACTUARIAL SCIENCE")
    except:
        majors = []
        
    try:
        minors = []
        for minor in user_choices["minors"]:
            minors.append(minor.upper())
    except:
        minors = []
        
    if user_choices["semesters"] == "":  
        startingSemester = "Fall 2022"
    else:
        startingSemester = user_choices["semesters"]
    
    dictionaries = createDictionaries(majors, minors)
    dict_1 = dictionaries[0]
    dict_2 = dictionaries[1]
    dict_3 = dictionaries[2]
    dict_4 = dictionaries[3]
    dict_5 = dictionaries[4]
    dict_6 = dictionaries[5]
    dict_7 = dictionaries[6]
    dict_8 = dictionaries[7]
    dict_9 = dictionaries[8]
    popped_classes = dictionaries[9]
    placement_output = Jplacement_algorithm(dict_1, dict_2, dict_3, dict_4, dict_6, dict_7, startingSemester, popped_classes)
    semesterList = placement_output[0]
    aois_left = placement_output[1]
    styles_to_enqueue = ["main.css"]
    scripts_to_enqueue = ["main.js"]
    return render_template(
        "main.html",
        title="Four-Year Plan Generator",
        classes_by_semester=finalCheck(dict_2, dict_3, dict_4, dict_6, dict_7, dict_8, dict_9, startingSemester, semesterList),
        requirements = getRequirementsForFrontEnd(majors, minors),
        drake_curriculum=drake_curriculum,
        user_choices=user_choices,
        styles_to_enqueue=styles_to_enqueue,
        scripts_to_enqueue=scripts_to_enqueue,
    )
