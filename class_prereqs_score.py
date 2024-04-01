from dictionaries import *

def class_prereqs_score(requirements):
    dict_prereq_values = {}
    dict_prereq_list = {}
    myList2 = []
    print("!!!! reqs:", requirements)
    for classValue in requirements: 
        myList2 = []
        if requirements[classValue] != ['None']: #level 1
            for lvl1prereq in requirements[classValue]:
                myList2.append([lvl1prereq, classValue])
                print("!!!! classValue:", classValue)
                print("!!!! lvl1prereqs:", requirements[classValue])
                if requirements[lvl1prereq] != ['None']: #level 2
                    print("!!!! class value:", classValue)
                    for lvl2prereq in requirements[lvl1prereq]:
                        if [lvl1prereq, classValue] in myList2:
                            myList2.remove([lvl1prereq,classValue])
                        myList2.append([lvl2prereq, lvl1prereq, classValue])
                    
                        if requirements[lvl2prereq] != ['None']: #level 3
                            for lvl3prereq in requirements[lvl2prereq]:
                                if [lvl2prereq, lvl1prereq, classValue] in myList2:
                                    myList2.remove([lvl2prereq, lvl1prereq,classValue])
                                myList2.append([lvl3prereq, lvl2prereq, lvl1prereq, classValue])
                                
                                if requirements[lvl3prereq] != ['None']: #level 4
                                    for lvl4prereq in requirements[lvl3prereq]:
                                        if [lvl3prereq, lvl2prereq, lvl1prereq, classValue] in myList2:
                                            myList2.remove([lvl3prereq, lvl2prereq, lvl1prereq,classValue])
                                        myList2.append([lvl4prereq, lvl3prereq, lvl2prereq, lvl1prereq, classValue])
                                        
                                        if requirements[lvl4prereq] != ['None']: #level 5
                                            for lvl5prereq in requirements[lvl4prereq]:
                                                if [lvl4prereq, lvl3prereq, lvl2prereq, lvl1prereq, classValue] in myList2:
                                                    myList2.remove([lvl4prereq, lvl3prereq, lvl2prereq, lvl1prereq,classValue])
                                                myList2.append([lvl5prereq, lvl4prereq, lvl3prereq, lvl2prereq, lvl1prereq, classValue])
                                                
                                                if requirements[lvl5prereq] != ['None']: #level 6
                                                    for lvl6prereq in requirements[lvl5prereq]:
                                                        if [lvl5prereq, lvl4prereq, lvl3prereq, lvl2prereq, lvl1prereq, classValue] in myList2:
                                                            myList2.remove([lvl5prereq, lvl4prereq, lvl3prereq, lvl2prereq, lvl1prereq,classValue])
                                                        myList2.append([lvl6prereq, lvl5prereq, lvl4prereq, lvl3prereq, lvl2prereq, lvl1prereq, classValue])
                                                        
                                                        if requirements[lvl6prereq] != ['None']: #level 7
                                                            for lvl7prereq in requirements[lvl6prereq]:
                                                                if [lvl6prereq, lvl5prereq, lvl4prereq, lvl3prereq, lvl2prereq, lvl1prereq, classValue] in myList2:
                                                                    myList2.remove([lvl6prereq, lvl5prereq, lvl4prereq, lvl3prereq, lvl2prereq, lvl1prereq,classValue])
                                                                myList2.append([lvl7prereq, lvl6prereq, lvl5prereq, lvl4prereq, lvl3prereq, lvl2prereq, lvl1prereq, classValue])


        if len(myList2) == 0:
            myList2.append([classValue])
        #print(myList2)
        
        dict_prereq_list[classValue] = myList2
        
    #print(dict_prereq_list)

    for C in dict_prereq_list:
        maxLength = 0
        #find max length string of classes
        for D in dict_prereq_list[C]:
            if len(D) > maxLength:
                maxLength = len(D)
        dict_prereq_values[C] = maxLength
        
    #print(dict_prereq_values)
    return dict_prereq_values

#class_prereqs_score(dict_1)


#print(dict_1)