from collections import OrderedDict
from operator import itemgetter
from class_prereqs_score import class_prereqs_score
from class_is_prereq_score import class_is_prereq_score
from dictionaries2 import *
from balanceCredits import *


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



def Jplacement_algorithm(requirements, dict_2, dict_3, dict_4, dict_6,dict_7, startingSemester, popped_courses):
    startingSemesterYear = startingSemester.split(" ")
    # Calculate prerequisite dictionary 
    prereq_dict = class_prereqs_score(requirements)

    # Calculate post-requisite dictionary 
    postreq_dict = class_is_prereq_score(requirements)[0]

    spots_dict = {}

    for course in requirements:
        
        prereq_score = prereq_dict[course]
        postreq_score = postreq_dict[course]
        yearOfferings = dict_7[course]
        
        fit = 1
        fits_arr = []

        # Loop to find available semesters for the course based on course type
        while fit <= 8:
            if fit >= prereq_score and fit <= 8 - postreq_score + 1:
                if "Fall" in startingSemester:
                    if int(dict_2[course][0])==1 and fit % 2 != 0: #offered fall, fall semester
                        fits_arr.append(fit) #that works
                    elif int(dict_2[course][1])==1 and fit % 2 == 0: #offered spring, spring semester
                        fits_arr.append(fit) #that works
                    
                    #check if classes are offered in odd/even years and adjust accordingly
                    
                    if int(startingSemesterYear[1]) % 2 == 0: #semesters 1, 4, 5, and 8 are in even years
                        if int(yearOfferings[0]) == 0: # if the course isn't offered in odd years
                            for oddYrSemester in [2,3,6,7]:
                                if oddYrSemester in fits_arr:
                                    fits_arr.remove(oddYrSemester) #remove all odd year semesters from fits_arr
                        if int(yearOfferings[1]) == 0: # if the course isn't offered in even years
                            for evenYrSemester in [1,4,5,8]:
                                if evenYrSemester in fits_arr:
                                    fits_arr.remove(evenYrSemester) #make it not fit in any even year semesters
                                
                    else: #semesters 2, 3, 6, and 7 are in even years
                        if int(yearOfferings[1]) == 0: # if the course isn't offered in even years
                            for evenYrSemester in [2,3,6,7]:
                                if evenYrSemester in fits_arr:
                                    fits_arr.remove(evenYrSemester) #remove all even year semesters from fits_arr
                        if int(yearOfferings[0]) == 0: # if the course isn't offered in odd years
                            for oddYrSemester in [1,4,5,8]:
                                if oddYrSemester in fits_arr:
                                    fits_arr.remove(oddYrSemester) #make it not fit in any odd year semesters
                        
                else:
                    if int(dict_2[course][0])==1 and fit % 2 == 0: #offered fall, fall semester
                        fits_arr.append(fit) #that works
                    elif int(dict_2[course][1])==1 and fit % 2 != 0: #offered spring, spring semester
                        fits_arr.append(fit) #that works
                        
                    #check if classes are offered in odd/even years and adjust accordingly
                        
                    if int(startingSemesterYear[1]) % 2 == 0: #semesters 1, 2, 5, and 6 are in even years
                        if int(yearOfferings[0]) == 0: # if the course isn't offered in odd years
                            for oddYrSemester in [3,4,7,8]:
                                if oddYrSemester in fits_arr:
                                    fits_arr.remove(oddYrSemester) #remove all odd year semesters from fits_arr
                        if int(yearOfferings[1]) == 0: # if the course isn't offered in even years
                            for evenYrSemester in [1,2,5,6]:
                                if evenYrSemester in fits_arr:
                                    fits_arr.remove(evenYrSemester) #make it not fit in any even year semesters
                                
                    else: #semesters 3, 4, 7, and 8 are in even years
                        if int(yearOfferings[1]) == 0: # if the course isn't offered in even years
                            for evenYrSemester in [3,4,7,8]:
                                if evenYrSemester in fits_arr:
                                    fits_arr.remove(evenYrSemester) #remove all even year semesters from fits_arr
                        if int(yearOfferings[0]) == 0: # if the course isn't offered in odd years
                            for oddYrSemester in [1,2,5,6]:
                                if oddYrSemester in fits_arr:
                                    fits_arr.remove(oddYrSemester) #make it not fit in any odd year semesters
            
            #check year requirements and remove values that don't fit
            
            if dict_4[course] != None: # if there is a year requirement
                yearReq = dict_4[course]
                if yearReq == "FR": # has to be taken during freshman year
                    for num in [3,4,5,6,7,8]:
                        if num in fits_arr:
                            fits_arr.remove(num) #can't fit anywhere but freshman year
                elif yearReq == "SO": # has to be taken sophmore yr or later
                    for num in [1,2]:
                        if num in fits_arr:
                            fits_arr.remove(num) #can't fit in freshman year
                elif yearReq == "JR": # has to be taken junior yr or later
                    for num in [1,2,3,4]:
                        if num in fits_arr:
                            fits_arr.remove(num) #can't fit in freshman or sophmore year
                elif yearReq == "SR": # has to be taken senior yr
                    for num in [1,2,3,4,5,6]:
                        if num in fits_arr:
                            fits_arr.remove(num) #can't fit in freshman, sophomore, or junior year
            fit += 1
        spots_dict[course] = fits_arr
    # Fill semester lists for required courses first
    semester_lists = {}

    # Using a for loop to fill the dictionary
    for i in range(1, 9):
        semester_lists[i] = []
    # Initialize semester lists

    # Function to fill semester lists with courses
    def fill_semester_lists(course_dict, semester_lists, credits_left, requirements):
        course_dict = sorted(course_dict.items(), key=itemgetter(1))
        course_dict = OrderedDict(course_dict)
        for course, info in course_dict.items():
            #course,info are variable used to iterate
            #course_dict.items are the value (of key:value pairs) of spots_dict = semester numbers avaliable
            for semester in info:
 
                if credits_left[semester] >= float(dict_3[course]):
                    good = True  # Assume the course can be added initially
                    for a in semester_lists[semester]:
                        if a in requirements[course] or semester not in course_dict[course]:
                            # If a course in this semester is a prerequisite for the current course,
                            # or if this semester is not available for the current course, set good to False
                            good = False
                            break  # No need to continue checking once good is False
                    if good:
                        semester_lists[semester].append(course)
                        credits_left[semester] = credits_left[semester] - float(dict_3[course])
                        break 
                # if credits_left[semester] >= dict_3[course]:
                #     semester_lists[semester].append(course)
                #     credits_left[semester] -= dict_3[course]
                #     break

    # Fill semester lists for required courses
    credits_left = {i: 18 for i in range(1, 9)}  # Initialize credits left for each semester
    fill_semester_lists(spots_dict, semester_lists, credits_left, requirements)
    
    # Fill semester lists for AOI courses

    aoi_req = ['Artistic Literacy','Critical Thinking','Engaged Citizen','Global and Cultural Understanding','Historical Foundations','Historical Foundations','Information Literacy','Quantitative Literacy','Scientific Literacy','Scientific Literacy','Values and Ethics','Written Communication']


    def check_for_aoi(aoireqs, dict_6, semesterlist):
        for semNumber in semesterlist:
            for course in semesterlist[semNumber]:
                for aoicourse, info in dict_6.items():
                    if course == aoicourse:
                        print("?", course, aoicourse)
                        if info in aoireqs:
                            aoireqs.remove(info)
                        break
        print(aoireqs)
        return aoireqs

    def fill_aoi_courses(semester_lists, credits_left, aoireqs):
        i = 1
        j = len(aoireqs) - 1
        print(str(semester_lists[1]))
    
        
        while sum(credits_left.values()) > 24:
            if i <= 8:
                while credits_left[i] > 5 and j >= 0:
                    print("aoireqs for credits_left[i] > 5"+aoireqs[j])
                    semester_lists[i].append(aoireqs[j])
                    print("semester_lists[i] for credits_left[i] > 5"+ str(semester_lists[i]))
                    aoireqs.remove(aoireqs[j])
                    credits_left[i] -= 3
                    j -= 1
                i += 1
            else:
                break
        
        while sum(credits_left.values()) > 24:
            if i <= 8:
                while credits_left[i] > 4 and j >= 0:
                    print("aoireqs for credits_left[i] > 4"+aoireqs[j])
                    semester_lists[i].append(aoireqs[j])
                    print("semester_lists[i] for credits_left[i] > 4"+ str(semester_lists[i]))
                    aoireqs.remove(aoireqs[j])
                    credits_left[i] -= 3
                    j -= 1
                i += 1
            else:
                break
            
        while sum(credits_left.values()) > 24: #not meeting min credit requirement
            if i <= 8:
                while credits_left[i] > 3 and j >= 0:
                 
                    print("aoireqs for credits_left[i] > 3"+aoireqs[j])
                    semester_lists[i].append(aoireqs[j])
                    print("semester_lists[i] for credits_left[i] > 3"+ str(semester_lists[i]))
                    aoireqs.remove(aoireqs[j])
                    credits_left[i] -= 3
                    j -= 1
                i += 1
            else:
                break
              
        return semester_lists


    # def fill_for_aoi(aoireqs,dict_6,semesterlist):
    #     for type in aoireqs:
    #         for aoicourse, info in dict_6.items():
    #            if 
    #             if info == type :
    #                 for semester in fits_arr:
    #                     if credits_left[semester] >= 3:
    #                         semesterlist[semester].append(aoicourse)
    #                         credits_left[semester] -= 3
    #                         break

    # def fill_placeholder_courses(semester_lists, credits_left):
    #     placeholder_course = "Placeholder"
    #     remaining_elective_slots = sum(credits_left.values()) // 3  # Calculate the number of elective slots remaining
    #     elective_slots_filled = 0
    #     for semester, slots_left in credits_left.items():
    #         while slots_left >= 4 and elective_slots_filled < remaining_elective_slots:
    #             semester_lists[semester].append(placeholder_course)
    #             elective_slots_filled += 1
    #             slots_left -= 3
    
    def fill_placeholder_courses(semester_lists, credits_left):
        i = 1
        j = 1
        
        while sum(credits_left.values()) > 24:
            if i <= 8:
                while credits_left[i] > 5:
                    semester_lists[i].append("Elective Course " + str(j))
                    credits_left[i] -= 3
                    j += 1
                i += 1
            else:
                break
            
        while sum(credits_left.values()) > 24:
            if i <= 8:
                while credits_left[i] > 4:
                    semester_lists[i].append("Elective Course " + str(j))
                    credits_left[i] -= 3
                    j += 1
                i += 1
            else:
                break
            
        i = 1
        print()
        while sum(credits_left.values()) > 24: #not meeting min credit requirement
            if credits_left[i] > 3:
                semester_lists[i].append("Elective Course " + str(j))
                credits_left[i] -= 3
                j += 1
            i += 1
            if i == 9:
                print("ERROR")
                break
            
        return semester_lists
                

    counter = 0
    new = False
    credits_left_list = []
    for a in credits_left:
        credits_left_list.append(credits_left[a])
    while max(credits_left_list) > 3 + min(credits_left_list):
        #print("you need to balance!")
        stuffTuple = loadBalance(credits_left, semester_lists, spots_dict, dict_3, counter, new)
        credits_left = stuffTuple[0]
        semester_lists = stuffTuple[1]
        counter = stuffTuple[2]
        new = stuffTuple[3]
        if counter >= 20:
            break

    aois_left = check_for_aoi(aoi_req, dict_6, semester_lists)
    semester_lists = fill_aoi_courses(semester_lists, credits_left, aoi_req)
    semester_lists = fill_placeholder_courses(semester_lists, credits_left)
    
    # Print the filled semester lists
    #print("Semester Lists:")
    semesterLists = [0]
    for semester, courses in semester_lists.items():
        for course in courses:
            if course in popped_courses:
                dict_3[course] = float(dict_3[course]) - .5
                courses.insert(courses.index(course)+1, popped_courses[course])
        #print(f"Semester {semester}: {courses}")
        semesterLists.append(courses)
        
        
    return semesterLists, aois_left
