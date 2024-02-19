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

for a in requirements["bus 195"]:
    print(a)

dict_postreq_values = {}
dict_postreq_list = {}
myList = []
for classToValue in requirements:
    myList = []
    for lvl1prereq in requirements: #level 1
        for a in requirements[lvl1prereq]:
            if a == classToValue:
                myList.append( [classToValue, lvl1prereq] )
                #print(myList)
                for lvl2prereq in requirements: #level 2
                    for b in requirements[lvl2prereq]:
                        if b == lvl1prereq:
                            if [classToValue, lvl1prereq] in myList:
                                myList.remove( [classToValue, lvl1prereq] )
                            myList.append( [classToValue, lvl1prereq, lvl2prereq] )
                            for lvl3prereq in requirements: #level 3
                                for c in requirements[lvl3prereq]:
                                    if c == lvl2prereq:
                                        if [classToValue, lvl1prereq, lvl2prereq] in myList:
                                            myList.remove( [classToValue, lvl1prereq, lvl2prereq] )
                                        myList.append( [classToValue, lvl1prereq, lvl2prereq, lvl3prereq] )
                                        for lvl4prereq in requirements: #level 4
                                            for d in requirements[lvl4prereq]:
                                                if d == lvl3prereq:
                                                    if [classToValue, lvl1prereq, lvl2prereq, lvl3prereq] in myList:
                                                        myList.remove( [classToValue, lvl1prereq, lvl2prereq, lvl3prereq] )
                                                    myList.append( [classToValue, lvl1prereq, lvl2prereq, lvl3prereq, lvl4prereq] )
                                                    for lvl5prereq in requirements: #level 5
                                                        for e in requirements[lvl5prereq]:
                                                            if e == lvl4prereq:
                                                                if [classToValue, lvl1prereq, lvl2prereq, lvl3prereq, lvl4prereq] in myList:
                                                                    myList.remove( [classToValue, lvl1prereq, lvl2prereq, lvl3prereq, lvl4prereq] )
                                                                myList.append( [classToValue, lvl1prereq, lvl2prereq, lvl3prereq, lvl4prereq, lvl5prereq] )
                                                                for lvl6prereq in requirements: #level 6
                                                                    for f in requirements[lvl6prereq]:
                                                                        if f == lvl5prereq:
                                                                            if [classToValue, lvl1prereq, lvl2prereq, lvl3prereq, lvl4prereq, lvl5prereq] in myList:
                                                                                myList.remove( [classToValue, lvl1prereq, lvl2prereq, lvl3prereq, lvl4prereq, lvl5prereq] )
                                                                            myList.append( [classToValue, lvl1prereq, lvl2prereq, lvl3prereq, lvl4prereq, lvl5prereq, lvl6prereq] )
                                                                            for lvl7prereq in requirements: #level 7
                                                                                for g in requirements[lvl7prereq]:
                                                                                    if g == lvl5prereq:
                                                                                        if [classToValue, lvl1prereq, lvl2prereq, lvl3prereq, lvl4prereq, lvl5prereq, lvl6prereq] in myList:
                                                                                            myList.remove( [classToValue, lvl1prereq, lvl2prereq, lvl3prereq, lvl4prereq, lvl5prereq, lvl6prereq] )
                                                                                        myList.append( [classToValue, lvl1prereq, lvl2prereq, lvl3prereq, lvl4prereq, lvl5prereq, lvl6prereq, lvl7prereq] )
    dict_postreq_list[classToValue] = myList

for A in dict_postreq_list:
    maxLength = 0
    #find max length string of classes
    for B in dict_postreq_list[A]:
        if len(B) > maxLength:
            maxLength = len(B)
    dict_postreq_values[A] = maxLength

print(dict_postreq_values)
    


