from placement_algorithm import *
from Jacob import *
from collections import OrderedDict
from operator import itemgetter
from class_prereqs_score import class_prereqs_score
from class_is_prereq_score import class_is_prereq_score
from dictionaries2 import *

def addSemester(pastSemName):
    if "Fall " in pastSemName:
        next1 = "Spring "
        pastSemName = int(pastSemName.replace("Fall ", ""))
        next2 = pastSemName + 1
    else:
        next1 = "Fall "
        next2 = int(pastSemName.replace("Spring ", ""))
    return next1 + str(next2)
    
#semesterList = Jplacement_algorithm(dict_1, dict_2, dict_3, dict_4, dict_6, dict_7, startingSemester)

#semesterList = [0, ["MATH 50", "ACTS 50", "ACTS 131"], ["ACTS 161"], [], [], [], [], [], []]

def finalCheck(dict_2, dict_3, dict_4, dict_6, dict_7, dict_8, dict_9, startingSemester, semesterList):
    #print(semesterList)
    aoi_req = ['Artistic Literacy','Critical Thinking','Engaged Citizen','Global and Cultural Understanding','Historical Foundations','Historical Foundations','Information Literacy','Quantitative Literacy','Scientific Literacy','Scientific Literacy','Values and Ethics','Written Communication']

    working = True
    retest = False
    currentSemester = startingSemester
    semesterCounter = 0
    while working:
        for oneSemesterList in semesterList[1:]: #look at schedule semester by semester
            semesterCounter += 1
            #get current values updated
            if "Fall " in currentSemester:
                currentSeason = "Fall"
                currentYear = int(currentSemester.replace("Fall ", ""))
            else:
                currentSeason = "Spring"
                currentYear = int(currentSemester.replace("Spring ", ""))
            #look at classes
            for semesterClass in oneSemesterList: #for each class in the selected semester
                #Confirm that classes are placed when they are offered.
                if "Elective" in semesterClass or "AOI" in semesterClass: 
                    continue
                #check fall/spring
                if currentSeason == "Fall":
                    fallOffered = dict_2[semesterClass][0]
                    if int(fallOffered) == 0:
                        print(semesterClass, "is not offered in fall")
                        # semesterList[semesterCounter].remove(semesterClass)
                        # semesterList[semesterCounter-1].append(semesterClass)
                        # retest = True
                        #working = False
                        #break
                else:
                    springOffered = dict_2[semesterClass][1]
                    if int(springOffered) == 0:
                        print(semesterClass, "is not offered in spring")
                        # semesterList[semesterCounter].remove(semesterClass)
                        # semesterList[semesterCounter+1].append(semesterClass)
                        # retest = True
                        working = False
                        break
                #check odd/even years
                yearOfferings = dict_7[semesterClass]
                if yearOfferings != "11": #if it isn't offered every year...
                    if currentYear % 2 == 0 and int(yearOfferings[1]) != 1: #if even semester and not offered then
                        print(semesterClass, "is not offered in even years")
                        working = False
                        break
                    elif currentYear % 2 != 0 and int(yearOfferings[0]) != 1: #if odd semester and not offered then
                        print(semesterClass, "is not offered in odd years")
                        working = False
                        break
                #check grade requirements
                gradeReqs = dict_4[semesterClass]
                if gradeReqs != None:
                    if gradeReqs == "FR" and semesterCounter > 2:
                        print(semesterClass, "is only offered to Freshman.")
                        working = False
                        break
                    if gradeReqs == "SO" and semesterCounter <3:
                        print(semesterClass, "requires at least Sophomore status.")
                        working = False
                        break
                    elif gradeReqs == "JR" and semesterCounter <5:
                        print(semesterClass, "requires at least Junior status.")
                        working = False
                        break
                    elif gradeReqs == "SR" and semesterCounter < 7:
                        print(semesterClass, "requires Senior status.")
                        working = False
                        break
                currentSemester = addSemester(currentSeason + " " + str(currentYear))
        if working:
            if retest:
                return finalCheck(dict_2, dict_3, dict_4, dict_7, dict_8, startingSemester, semesterList)
            else:
                return reformat(semesterList, startingSemester, dict_3, dict_6, dict_9)
    return "ERROR - INVALID SCHEDULE"

def reformat(semesterList, startingSemester, dict_3, dict_6, dict_9):
        aoi_req = ['Artistic Literacy','Critical Thinking','Engaged Citizen','Global and Cultural Understanding','Historical Foundations','Historical Foundations','Information Literacy','Quantitative Literacy','Scientific Literacy','Scientific Literacy','Values and Ethics','Written Communication']

        finalSchedule = {}
        semester = startingSemester
        i = 1
        while i <= 8:
            finalSchedule[semester] = {}
            tempList = {}
            for course in semesterList[i]:
                courseDict = {}
                #for each course, we need the name, course_num and attributes
                if "Elective" not in course and "AOI" not in course:
                    courseTitle = dict_9[course]
                    courseCredits = float(dict_3[course])
                    if courseCredits % 1 == 0:
                        courseCredits = int(courseCredits)
                    if course in dict_6:
                        courseAttributes = dict_6[course]
                    elif "MATH" in course:
                        courseAttributes = "Quantitative Literacy"
                    else:
                        courseAttributes = None
                    courseDict[course] = {'title': courseTitle, 'course_number': course, 'num_credits': courseCredits , 'attributes': [courseAttributes]}
                elif "AOI" in course:
                    if "Historical Foundations" in course:
                        courseDict[course] = {'title': course, 'course_number': "", 'num_credits': 3, 'attributes': ["Historical Foundations"]}
                    elif "Scientific Literacy" in course and "Lab" in course:
                        courseDict[course] = {'title': course, 'course_number': "", 'num_credits': 4.5, 'attributes': ["Scientific Literacy"]}
                    else:
                        courseDict[course] = {'title': course, 'course_number': "", 'num_credits': 3, 'attributes': [course[:-4]]}
                else:
                    courseDict[course] = {'title': course, 'course_number': "", 'num_credits': 3, 'attributes': []}
                #have courses with 0 credits appear first
                if courseDict[course]["num_credits"] == 0 and "Elective" not in courseDict[course]["title"]:
                    finalSchedule[semester].update({course:courseDict[course]})
                else:
                    tempList[course] = courseDict[course]
            for key in tempList:
                finalSchedule[semester].update({key:tempList[key]})
            semester = addSemester(semester)
            i+=1
        return finalSchedule


def reformat2(semesterList, startingSemester, dict_8):
    finalSchedule = {}
    semester = startingSemester
    i = 1
    while i <= 8:
        tempList = []
        for course in semesterList[i]:
            if "Elective" not in course and "AOI" not in course:
                tempList.append(dict_8[course]) #gets dictionary for course with all info we pass to frontend
            else:
                tempList.append(course)
        finalSchedule[semester] = tempList #add entry for this semester
        
        semester = addSemester(semester)
        i+=1
    return finalSchedule

#print(finalCheck(dict_2, dict_4, dict_7, dict_8, startingSemester, semesterList))
