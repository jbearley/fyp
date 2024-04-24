import datetime

majors = [
    "Actuarial Science", 
    "Accounting",
    "Economics (BSBA)",
    "Business Law",
    "Data Analytics",
    "Finance",
    "Management",
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
    
# complete from this link https://www.drake.edu/academics/undergraduate/majors/ up to "Military Studies" (from "College / School Listing" view)
drake_curriculum = {
    "majors": majors,
    "minors": minors,
    "concentrations": concentrations,
    "semesters": semesters,
}
