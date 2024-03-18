requirements = { "acct 41": [], 
                "acct 42": ["acct 41"], 
                "fin 101": ["acct 42", "is 44", "econ 2", "acts 131"], 
                "bus 195": ["senior", "fin 101", "mktg 101", "mgmt 110", "mgmt 120"],
                "acts 131": ["math 70"],
                "acts 135": ["acts 131"],
                "stat 170": ["stat 40", "acts 135"],
                "acts 150": ["acts 120", "acts 131"],
                "mgmt 120": ["acts 135"],
                "acts 161": ["acts 131"]
}

def class_is_prereq_score(requirements):
    dict_postreq_values = {}
    dict_postreq_list = {}
    myList = []
    for classToValue in requirements:
        myList = []
        for lvl1postreq in requirements: #level 1
            for a in requirements[lvl1postreq]:
                if a == classToValue:
                    myList.append( [classToValue, lvl1postreq] )
                    for lvl2postreq in requirements: #level 2
                        for b in requirements[lvl2postreq]:
                            if b == lvl1postreq:
                                if [classToValue, lvl1postreq] in myList:
                                    myList.remove( [classToValue, lvl1postreq] )
                                myList.append( [classToValue, lvl1postreq, lvl2postreq] )
                                for lvl3postreq in requirements: #level 3
                                    for c in requirements[lvl3postreq]:
                                        if c == lvl2postreq:
                                            if [classToValue, lvl1postreq, lvl2postreq] in myList:
                                                myList.remove( [classToValue, lvl1postreq, lvl2postreq] )
                                            myList.append( [classToValue, lvl1postreq, lvl2postreq, lvl3postreq] )
                                            for lvl4postreq in requirements: #level 4
                                                for d in requirements[lvl4postreq]:
                                                    if d == lvl3postreq:
                                                        if [classToValue, lvl1postreq, lvl2postreq, lvl3postreq] in myList:
                                                            myList.remove( [classToValue, lvl1postreq, lvl2postreq, lvl3postreq] )
                                                        myList.append( [classToValue, lvl1postreq, lvl2postreq, lvl3postreq, lvl4postreq] )
                                                        for lvl5postreq in requirements: #level 5
                                                            for e in requirements[lvl5postreq]:
                                                                if e == lvl4postreq:
                                                                    if [classToValue, lvl1postreq, lvl2postreq, lvl3postreq, lvl4postreq] in myList:
                                                                        myList.remove( [classToValue, lvl1postreq, lvl2postreq, lvl3postreq, lvl4postreq] )
                                                                    myList.append( [classToValue, lvl1postreq, lvl2postreq, lvl3postreq, lvl4postreq, lvl5postreq] )
                                                                    for lvl6postreq in requirements: #level 6
                                                                        for f in requirements[lvl6postreq]:
                                                                            if f == lvl5postreq:
                                                                                if [classToValue, lvl1postreq, lvl2postreq, lvl3postreq, lvl4postreq, lvl5postreq] in myList:
                                                                                    myList.remove( [classToValue, lvl1postreq, lvl2postreq, lvl3postreq, lvl4postreq, lvl5postreq] )
                                                                                myList.append( [classToValue, lvl1postreq, lvl2postreq, lvl3postreq, lvl4postreq, lvl5postreq, lvl6postreq] )
                                                                                for lvl7postreq in requirements: #level 7
                                                                                    for g in requirements[lvl7postreq]:
                                                                                        if g == lvl5postreq:
                                                                                            if [classToValue, lvl1postreq, lvl2postreq, lvl3postreq, lvl4postreq, lvl5postreq, lvl6postreq] in myList:
                                                                                                myList.remove( [classToValue, lvl1postreq, lvl2postreq, lvl3postreq, lvl4postreq, lvl5postreq, lvl6postreq] )
                                                                                            myList.append( [classToValue, lvl1postreq, lvl2postreq, lvl3postreq, lvl4postreq, lvl5postreq, lvl6postreq, lvl7postreq] )
        dict_postreq_list[classToValue] = myList

    print(dict_postreq_list)
    for A in dict_postreq_list:
        maxLength = 1
        #find max length string of classes
        for B in dict_postreq_list[A]:
            if len(B) > maxLength:
                maxLength = len(B)
        dict_postreq_values[A] = maxLength

    #print(dict_postreq_values)
    return dict_postreq_values, dict_postreq_list

class_is_prereq_score(requirements)