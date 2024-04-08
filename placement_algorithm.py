from collections import OrderedDict
from operator import itemgetter
from class_prereqs_score import class_prereqs_score
from class_is_prereq_score import class_is_prereq_score
from dictionaries2 import *


def placement_algorithm(requirements, dict_2, dict_3, startingSemester):
    prereq_dict = class_prereqs_score(requirements)
    postreq_dict = (class_is_prereq_score(requirements))[0]

    spots_dict = {}
    for a in class_prereqs_score(requirements):
        prereq_score = prereq_dict[a]
        postreq_score = postreq_dict[a]
        fit = 1
        fits_arr = []
        while fit <=8:
            if fit >= prereq_score and fit <= 8-postreq_score+1:
                if "Fall" in startingSemester:
                    if int(dict_2[a][0])==1 and fit % 2 != 0: #offered fall, fall semester
                        fits_arr.append(fit) #that works
                    elif int(dict_2[a][1])==1 and fit % 2 == 0: #offered spring, spring semester
                        fits_arr.append(fit) #that works
                else:
                    if int(dict_2[a][0])==1 and fit % 2 == 0: #offered fall, fall semester
                        fits_arr.append(fit) #that works
                    elif int(dict_2[a][1])==1 and fit % 2 != 0: #offered spring, spring semester
                        fits_arr.append(fit) #that works
            fit += 1
        spots_dict[a] = fits_arr
    #print(spots_dict)
        #here would be where you check class requirements and also incorporate that info?

    spots_dict = sorted(spots_dict.items(), key=itemgetter(1))
    spots_dict = OrderedDict(spots_dict)
    #for now, I'm assuming everything is 3 credits... will have to change that later
    creditsLeft = [0,12,12,12,12,12,12,12,12]
    semesterLists = [0,['AOI'],['AOI'],['AOI'],['AOI'],['AOI'],['AOI'],['AOI'],['AOI']]

    for course in spots_dict:
        j = 1
        while j <= 8: 
            if j in spots_dict[course]:
                i=1
                while i <= 8:
                    if creditsLeft[i] > dict_3[course]:  
                        good = True
                        for a in semesterLists[i]:
                            #if those aren't pre-reqs of course, continue
                            #if we move on to the next tier and a spot isn't filled, leave it empty 
                            if a in requirements[course] or i not in spots_dict[course]:
                                good = False
                        if good:
                            semesterLists[i].append(course)
                            creditsLeft[i] -= dict_3[course]
                            break
                    i += 1
                break
            j+=1
        else:
            print("ERROR")
            break
    
    #print("spots dict:")
    #print(spots_dict)
    #print("semester lists")
    #print(semesterLists)
    #print()

    return semesterLists

# dictionaries = createDictionaries("Actuarial Science")
# dict_1 = dictionaries[0]
# dict_2 = dictionaries[1]
# print(dict_2, "\n")
# print(placement_algorithm(dict_1, dict_2, dict_3, "Fall 2022"))