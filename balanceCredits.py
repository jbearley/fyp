def loadBalance(credits_left, semester_lists, spots_dict, dict_3, counter, new):
    credits_left2 = []
    for a in credits_left:
        credits_left2.append(credits_left[a])

    counter2 = counter
    if new == False:
        while counter2 != 0:
            #remove min value; replace w avg to not set off alarms
            index = credits_left2.index(min(credits_left2))
            credits_left2[index] = sum(credits_left2)/len(credits_left2)
            counter2 -= 1
    
    new = False
    #print(credits_left2)
    
    fullSemester = credits_left2.index(min(credits_left2)) + 1
    emptySemester = credits_left2.index(max(credits_left2)) + 1
            
    #print(emptySemester, fullSemester)
    for course in semester_lists[fullSemester]:
        if "Elective" not in course:
            if 8 in spots_dict[course]: #ensure no classes go after it
                if emptySemester in spots_dict[course]: #ensure its offered that semester
                    #move it to that semester
                    semester_lists[fullSemester].remove(course)
                    semester_lists[emptySemester].append(course)
                    #fix credit counts
                    credits_left[fullSemester] += float(dict_3[course])
                    credits_left[emptySemester] -= float(dict_3[course])
                    new = True
    
    #print(credits_left)
    counter += 1
    return credits_left, semester_lists, counter, new


