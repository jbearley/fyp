
from collections import OrderedDict
from operator import itemgetter
from class_prereqs_score import class_prereqs_score
from class_is_prereq_score import class_is_prereq_score
# Given requirements dictionary
requirements = {
    "acct 41": [],
    "acct 42": ["acct 41"],
    "fin 101": ["acct 42", "is 44", "econ 2", "acts 131"],
    "bus 195": ["fin 101", "mktg 101", "mgmt 110", "mgmt 120"],
    "acts 131": ["math 70"],
    "acts 135": ["acts 131"],
    "stat 170": ["stat 40", "acts 135"],
    "acts 150": ["acts 120", "acts 131"],
    "mgmt 120": ["acts 135"],
    "acts 161": ["acts 131"],
    "is 44": [],
    "econ 2": [],
    "mktg 101": ["econ 2"],
    "mgmt 110": [],
    "mgmt 120": ["acts 135"],
    "math 50": [],
    "math 70": ["math 50"],
    "stat 40": [],
    "acts 120": ["math 70"]

}


# Calculate prerequisite dictionary 
#stores as a dictonary the course(key) and the # of prereqs to that course(value)
prereq_dict = class_prereqs_score(requirements)

# Calculate post-requisite dictionary 
#stores as a dictonary the course(key) and the # of courses that course is to a prereq to(value)
postreq_dict = class_is_prereq_score(requirements)[0]

# Print the outputs
print("Prerequisite Dictionary:")
print(prereq_dict)
print("\nPost-Requisite Dictionary:")
print(postreq_dict)

spots_dict = {}

for a in class_prereqs_score(requirements):
    prereq_score = prereq_dict[a]
    print("Prerequisite score:"  + str(prereq_dict[a]))
    postreq_score = postreq_dict[a]
    print("\nPost-Requisite score:" + str(postreq_dict[a]))
    fit = 1
    fits_arr = []
    #fit_arr is the semesters that fits 
    while fit <=8:
        #this loop takes the postreq and prereq
        if fit >= prereq_score and fit <= 8-postreq_score+1:
            #this is where we need to add a checker to see what type of courses are being added AOI/electives
            fits_arr.append(fit)
            print("fits_arr:" + str(fits_arr))
        fit += 1
    spots_dict[a] = fits_arr
    print("just sportdict"+str(spots_dict))
    print("sportdict[a]"+str(spots_dict[a]))

    #sorted turn array into dictionary
    spots_dict = sorted(spots_dict.items(), key=itemgetter(1))
    print("sorted spot dict"+str(spots_dict))
    #orderedDict orders them
    spots_dict = OrderedDict(spots_dict)
    #spot_dict is now a course(key) paired with the avaiable semsters(values)
    print("ordered spot dict"+str(spots_dict))

    #for now, I'm assuming everything is 3 credits... will have to change that later
    creditsLeft = [0,12,12,12,12,12,12,12,12]
    semesterLists = [0,[],[],[],[],[],[],[],[]]

    for course in spots_dict:
        j = 1
        while j <= 8: 
            #looping through 8 semsters
            if j in spots_dict[course]:
                i=1
                #looping through a courses avaliable semster 
                while i <= 8:
                    if creditsLeft[i] != 0:   
                        good = True
                        for a in semesterLists[i]:
                            #if those aren't pre-reqs of course, continue
                            #if we move on to the next tier and a spot isn't filled, leave it empty 
                            if a in requirements[course] or i not in spots_dict[course]:
                                good = False
                        if good:
                            semesterLists[i].append(course)
                            creditsLeft[i] -= 3
                            break
                    i += 1
                break
            j+=1
        else:
            print("ERROR")
            break
    
    print("spots dict:")
    print(spots_dict)
    print("semester lists")
    print(semesterLists)
    print()


from collections import OrderedDict
from operator import itemgetter
from class_prereqs_score import class_prereqs_score
from class_is_prereq_score import class_is_prereq_score

# Given requirements dictionary
requirements = {
    "acct 41": [],
    "acct 42": ["acct 41"],
    "fin 101": ["acct 42", "is 44", "econ 2", "acts 131"],
    "bus 195": ["fin 101", "mktg 101", "mgmt 110", "mgmt 120"],
    "acts 131": ["math 70"],
    "acts 135": ["acts 131"],
    "stat 170": ["stat 40", "acts 135"],
    "acts 150": ["acts 120", "acts 131"],
    "mgmt 120": ["acts 135"],
    "acts 161": ["acts 131"],
    "is 44": [],
    "econ 2": [],
    "mktg 101": ["econ 2"],
    "mgmt 110": [],
    "mgmt 120": ["acts 135"],
    "math 50": [],
    "math 70": ["math 50"],
    "stat 40": [],
    "acts 120": ["math 70"]
}

# Major requirements
major_requirements = ["acct 41", "acct 42", "fin 101"]

# AOI courses
aoi_courses = ["acts 131", "acts 135", "stat 170", "acts 150", "mgmt 120", "acts 161"]

# Calculate prerequisite dictionary 
prereq_dict = class_prereqs_score(requirements)

# Calculate post-requisite dictionary 
postreq_dict = class_is_prereq_score(requirements)[0]

# Print the outputs
print("Prerequisite Dictionary:")
print(prereq_dict)
print("\nPost-Requisite Dictionary:")
print(postreq_dict)

spots_dict = {}

for course in requirements:
    # Check if course is AOI, elective, or required for major
    if course in major_requirements:
        course_type = 'required'
    elif course in aoi_courses:
        course_type = 'aoi'
    else:
        course_type = 'elective'
    
    prereq_score = prereq_dict[course]
    postreq_score = postreq_dict[course]
    
    fit = 1
    fits_arr = []

    # Loop to find available semesters for the course based on course type
    while fit <= 8:
        if fit >= prereq_score and fit <= 8 - postreq_score + 1:
            fits_arr.append(fit)
        fit += 1
    
    spots_dict[course] = {'type': course_type, 'fits': fits_arr}

# Separate AOI courses, electives, and required courses
aoi_courses_dict = {k: v for k, v in spots_dict.items() if v['type'] == 'aoi'}
elective_courses_dict = {k: v for k, v in spots_dict.items() if v['type'] == 'elective'}
required_courses_dict = {k: v for k, v in spots_dict.items() if v['type'] == 'required'}

# Fill semester lists for required courses first
semester_lists = {i: [] for i in range(1, 9)}  # Initialize semester lists

# Function to fill semester lists with courses
def fill_semester_lists(course_dict, semester_lists, credits_left):
    for course, info in course_dict.items():
        fits_arr = info['fits']
        for semester in fits_arr:
            if credits_left[semester] >= 3:
                semester_lists[semester].append(course)
                credits_left[semester] -= 3
                break

# Fill semester lists for required courses
credits_left = {i: 12 for i in range(1, 9)}  # Initialize credits left for each semester
fill_semester_lists(required_courses_dict, semester_lists, credits_left)

# Fill semester lists for AOI courses
for course, info in aoi_courses_dict.items():
    fits_arr = info['fits']
    for semester in fits_arr:
        if credits_left[semester] >= 3:
            semester_lists[semester].append(course)
            credits_left[semester] -= 3
            break

# Fill remaining spots with electives and placeholders
placeholder_course = "Placeholder"
remaining_elective_slots = sum(credits_left.values()) // 3  # Calculate the number of elective slots remaining
elective_slots_filled = 0
for semester, slots_left in credits_left.items():
    while slots_left >= 3 and elective_slots_filled < remaining_elective_slots:
        semester_lists[semester].append(placeholder_course)
        elective_slots_filled += 1
        slots_left -= 3

# Print the filled semester lists
print("Semester Lists:")
for semester, courses in semester_lists.items():
    print(f"Semester {semester}: {courses}")

# Print the elective courses
print("\nElective Courses:")
for course, info in elective_courses_dict.items():
    fits_arr = info['fits']
    print(f"{course}: Available in semesters {fits_arr}")

