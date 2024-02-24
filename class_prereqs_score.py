requirements = { "acct 41": [], 
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
                "mktg 101": [],
                "mgmt 110": [],
                "mgmt 120": [],
                "math 70": [],
                "stat 40": [],
                "acts 120": []
}

dict_prereq_values = {}
dict_prereq_list = {}
myList2 = []

#for classValue in requirements:
#    myList2 = []
 #   for lvl1prereq in requirements: #level 1
#        for A in requirements[lvl1prereq]:
#            if A == classValue:
#                myList2.append( [classValue, lvl1prereq] )
                
for classValue in requirements: 
    myList2 = []
    if len(requirements[classValue]) > 0: #level 1
        for lvl1prereq in requirements[classValue]:
            myList2.append([lvl1prereq, classValue])
            
            if len(requirements[lvl1prereq]) > 0: #level 2
                for lvl2prereq in requirements[lvl1prereq]:
                    if [lvl1prereq, classValue] in myList2:
                        myList2.remove([lvl1prereq,classValue])
                    myList2.append([lvl2prereq, lvl1prereq, classValue])
                
                    if len(requirements[lvl2prereq]) > 0: #level 3
                        for lvl3prereq in requirements[lvl2prereq]:
                            if [lvl2prereq, lvl1prereq, classValue] in myList2:
                                myList2.remove([lvl2prereq, lvl1prereq,classValue])
                            myList2.append([lvl3prereq, lvl2prereq, lvl1prereq, classValue])
                            
                            if len(requirements[lvl3prereq]) > 0: #level 4
                                for lvl4prereq in requirements[lvl3prereq]:
                                    if [lvl3prereq, lvl2prereq, lvl1prereq, classValue] in myList2:
                                        myList2.remove([lvl3prereq, lvl2prereq, lvl1prereq,classValue])
                                    myList2.append([lvl4prereq, lvl3prereq, lvl2prereq, lvl1prereq, classValue])
                                    
                                    if len(requirements[lvl4prereq]) > 0: #level 5
                                        for lvl5prereq in requirements[lvl4prereq]:
                                            if [lvl4prereq, lvl3prereq, lvl2prereq, lvl1prereq, classValue] in myList2:
                                                myList2.remove([lvl4prereq, lvl3prereq, lvl2prereq, lvl1prereq,classValue])
                                            myList2.append([lvl5prereq, lvl4prereq, lvl3prereq, lvl2prereq, lvl1prereq, classValue])
                                            
                                            if len(requirements[lvl5prereq]) > 0: #level 6
                                                for lvl6prereq in requirements[lvl5prereq]:
                                                    if [lvl5prereq, lvl4prereq, lvl3prereq, lvl2prereq, lvl1prereq, classValue] in myList2:
                                                        myList2.remove([lvl5prereq, lvl4prereq, lvl3prereq, lvl2prereq, lvl1prereq,classValue])
                                                    myList2.append([lvl6prereq, lvl5prereq, lvl4prereq, lvl3prereq, lvl2prereq, lvl1prereq, classValue])
                                                    
                                                    if len(requirements[lvl6prereq]) > 0: #level 7
                                                        for lvl7prereq in requirements[lvl6prereq]:
                                                            if [lvl6prereq, lvl5prereq, lvl4prereq, lvl3prereq, lvl2prereq, lvl1prereq, classValue] in myList2:
                                                                myList2.remove([lvl6prereq, lvl5prereq, lvl4prereq, lvl3prereq, lvl2prereq, lvl1prereq,classValue])
                                                            myList2.append([lvl7prereq, lvl6prereq, lvl5prereq, lvl4prereq, lvl3prereq, lvl2prereq, lvl1prereq, classValue])


    if len(myList2) == 0:
        myList2.append([classValue])
    #print(myList2)
    
    dict_prereq_list[classValue] = myList2
    
print(dict_prereq_list)

for C in dict_prereq_list:
    maxLength = 0
    #find max length string of classes
    for D in dict_prereq_list[C]:
        if len(D) > maxLength:
            maxLength = len(D)
    dict_prereq_values[C] = maxLength
    
print(dict_prereq_values)