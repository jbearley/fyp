import datetime

majors = [ 
    "Accounting",
    "Actuarial Science",
    "Business Law",
    "Data Analytics",
    "Economics (BSBA)",
    "Finance",
    #"Management",
]
minors = [
    "Accounting",
    "Actuarial Science",
    "Business Law",
    "Data Analytics",
    "Economics",
    "Information Systems",
    "Management",
]
concentrations = [
    "Behavior Analysis of Developmental Disabilities",
    "Biophysics",
    "Comparative Animal Behavior",
    "Global and Comparative Public Health",
    "Human Resources Management",
    "Interdisciplinary Study of the Humanities and Sciences",
]

semesters = []

today = datetime.date.today()
currentYear = today.year
i = -3
while i < 3:
    fallSemester = "Fall " +str(currentYear + i)
    springSemester = "Spring " + str(currentYear + i)
    semesters.append(fallSemester)
    semesters.append(springSemester)
    i += 1

drake_curriculum = {
    "majors": majors,
    "minors": minors,
    "concentrations": concentrations,
    "semesters": semesters,
}
