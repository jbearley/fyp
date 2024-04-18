def dealWithOrReqs(dict_1):
    new_dict_1 = {}
    
    for key in dict_1:
        for prereq in dict_1[key]:
            if "/" in prereq:
                new_dict_1[key] = dict_1[key]
                
    #new_dict_1 now only has classes with / requirements
    for key in new_dict_1:
        for prereq in dict_1[key]:
            if "/" in prereq:
                #these are the sets we need to deal with
                #print(prereq, "\n")
                #we need to look at the two distinct class keys, yay subsets
                slash1Index = prereq.index("/")
                course1 = prereq[:slash1Index]
                course2 = prereq[slash1Index+1:]
                course3 = 0
                course4 = 0
                if "/" in course2:
                    slash2Index = course2.index("/")
                    course3 = course2[slash2Index+1:]
                    course2 = course2[:slash2Index]
                    if "/" in course3:
                        slash3Index = course3.index("/")
                        course4 = course2[slash3Index+1:]
                        course3 = course2[:slash3Index]
                courseOptions = []
                for course in [course1,course2,course3,course4]:
                    if course != 0:
                        courseOptions.append(course)
                #we now have the courses separated and in an array
                unsatisfied = True
                goodOption = "no"
                while unsatisfied:
                    for option in courseOptions:
                        try:
                            dict_1[option]
                            unsatisfied = False
                            goodOption = option
                            break
                        except:
                            continue
                    if unsatisfied:
                        print(key, prereq, "\n\n\n")
                        break
                new_dict_1[key].remove(prereq) 
                new_dict_1[key].append(goodOption)
                
    for key in dict_1:
        for prereq in dict_1[key]:
            if "/" not in prereq:
                new_dict_1[key] = dict_1[key]
    return new_dict_1
