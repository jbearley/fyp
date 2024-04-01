from placement_algorithm import *

def addSemester(pastSemName):
    if "Fall " in pastSemName:
        next1 = "Spring "
        pastSemName = int(pastSemName.replace("Fall ", ""))
        next2 = pastSemName + 1
    else:
        next1 = "Fall "
        next2 = int(pastSemName.replace("Spring ", ""))
    return next1 + str(next2)
    

major = "ACTUARIAL SCIENCE" #don't hardcode later
startingSemester = "Fall 2022" #ditto
dictionaries = createDictionaries(major)
dict_1 = dictionaries[0]
dict_2 = dictionaries[1]
dict_3 = dictionaries[2]
dict_4 = dictionaries[3]
dict_5 = dictionaries[4]
dict_7 = dictionaries[5]
dict_8 = dictionaries[6]
semesterList = placement_algorithm(dict_1)

semesterList = [0, ["ACTS 50", "ACTS 131"], ["ACTS 161"], [], [], [], [], [], []]

def finalCheck(dict_2, dict_7, dict_8, startingSemester, semesterList):
    working = True
    currentSemester = startingSemester
    while working:
        for oneSemesterList in semesterList[1:]: #look at schedule semester by semester
            if "Fall " in currentSemester:
                currentSeason = "Fall"
                currentYear = int(currentSemester.replace("Fall ", ""))
            else:
                currentSeason = "Spring"
                currentYear = int(currentSemester.replace("Spring ", ""))
            for semesterClass in oneSemesterList: #for each class in the selected semester
                #Confirm that classes are placed when they are offered.
                if semesterClass == "AOI": #ignore AOIs - may need to update this depending on how we end up formatting these
                    continue
                #check fall/spring
                if currentSeason == "Fall":
                    fallOffered = dict_2[semesterClass][0]
                    if int(fallOffered) == 0:
                        print(semesterClass, "is not offered in fall")
                        working = False
                        break
                else:
                    springOffered = dict_2[semesterClass][1]
                    if int(springOffered) == 0:
                        print(semesterClass, "is not offered in spring")
                        working = False
                        break
                #check odd/even years
                yearOfferings = dict_7[semesterClass]
                if yearOfferings != "11": #if it isn't offered every year...
                    if currentYear % 2 == 0 and yearOfferings[1] != 1: #if even semester and not offered then
                        print(semesterClass, "is not offered in even years")
                    elif currentYear % 2 != 0 and yearOfferings[0] != 1: #if even semester and not offered then
                        print(semesterClass, "is not offered in odd years")
                currentSemester = addSemester(currentSeason + " " + str(currentYear))
        if working:
            return reformat(semesterList, startingSemester, dict_8)
    return "ERROR - INVALID SCHEDULE"

def reformat(semesterList, startingSemester, dict_8):
    finalSchedule = {}
    semester = startingSemester
    i = 1
    while i <= 8:
        tempList = []
        for course in semesterList[i]:
            tempList.append(dict_8[course]) #gets dictionary for course with all info we pass tp frontend
        finalSchedule[semester] = tempList #add entry for the semester
        
        semester = addSemester(semester)
        i+=1
    return finalSchedule

print(finalCheck(dict_2, dict_7, dict_8, startingSemester, semesterList))