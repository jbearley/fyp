from azuresqlconnector import *
conn = SQLConnection()
conn = conn.getConnection()
cursor = conn.cursor()


def elective_dictionary(choose_table):
    if choose_table=="Actuarial Science":
        choose_table="PICK_TWO_ACT_SCI"
    if choose_table == "Accounting":
        choose_table="PICK_TWO_ACC"
    elif choose_table=="Business Law First":
        choose_table= "FIRST_BL_PICK_ONE"
    elif choose_table == "Business Law Second":
        choose_table= "SECOND_BL_PICK_ONE"
    elif choose_table== "Business Law Third":
        choose_table= "CHOOSE_THREE_BLAW"
    elif choose_table=="Economics":
        choose_table="CHOOSE_FOUR_ECON"
    

    #dictionary with Class Id for the key, Prerequisites for the value
    query_1 = "SELECT CLASSES.ClassID, Prereqs FROM dbo.CLASSES, dbo." + choose_table + " WHERE CLASSES.ClassID =" + choose_table + ".ClassID"
    cursor.execute(query_1)
    dict_1 = {}
    result = cursor.fetchall()
    for tup in result:
        tup[1] = str(tup[1]).split(', ')
        for a in tup[1]:
            if a[0] == " ":
                a = a[1:]
        dict_1[tup[0]]=tup[1]



    #dictionary with ClassID for the key, value consists of a concatenated string of Fall (0 or 1) and Spring (0 or 1) value depending on whether the class is offered in the fall / spring or not
    query_2 = "SELECT CLASSES.ClassID, Fall, Spring FROM dbo.CLASSES, dbo." + choose_table + " WHERE CLASSES.ClassID =" + choose_table + ".ClassID"
    cursor.execute(query_2)
    dict_2 = {}
    result_2 = cursor.fetchall()
    for tup in result_2:
        dict_2[tup[0]]=str(tup[1])+str(tup[2])
    #print(dict_2)

    #dictionary with ClassID for the key, number of credits for the value
    query_3 = "SELECT CLASSES.ClassID, Credits FROM dbo.CLASSES, dbo." + choose_table + " WHERE CLASSES.ClassID =" + choose_table + ".ClassID"
    cursor.execute(query_3)
    dict_3 = {}
    result_3 = cursor.fetchall()
    for tup in result_3:
        dict_3[tup[0]]=tup[1]

    #dictionary with ClassID for the key, grade requirement for the value. If no grade requirement, than it has None.
    query_4 = "SELECT CLASSES.ClassID, GradeReq FROM dbo.CLASSES, dbo." + choose_table + " WHERE CLASSES.ClassID =" + choose_table + ".ClassID"
    cursor.execute(query_4)
    dict_4 = {}
    result_4 = cursor.fetchall()
    for tup in result_4:
        dict_4[tup[0]]=tup[1]

    #dictionary with ClassID for the key, corequisities for the value. If no corequisities, then the value is None.
    query_5 = "SELECT CLASSES.ClassID, Coreq FROM dbo.CLASSES, dbo." + choose_table + " WHERE CLASSES.ClassID =" + choose_table + ".ClassID"
    cursor.execute(query_5)
    dict_5 = {}
    result_5 = cursor.fetchall()
    for tup in result_5:
        dict_5[tup[0]]=tup[1]
        
    # This takes the list of corequisites from dictionary 5, checks which of them are none, and then pops the ones that are not from dictionary 1.
    # dict1 maps class: prerequisitiees, dict5 maps class to coreq (if class has corequisites), if it is in the list of prerequisites as well, remove it
    # left with a list of classes that
    #If the class has corequisites, then remove it from the list of classes that have prereqs
    popped_classes = {}
    for key in dict_5:
        if dict_5[key]!=None:
            if key in dict_1 and key[-1] == "L":
                popped_classes[key]=dict_5[key]
                dict_1.pop(key)

    query_6 = f"""
    SELECT ClassID, AOI FROM dbo.AOI
    """
    cursor.execute(query_6)
    dict_6 = {}
    result_6 = cursor.fetchall()
    for tup in result_6:
        dict_6[tup[0]]= tup[1] 
        

        
    #dictionary with ClassID for the key, value consists of a concatenated string of Odd (0 or 1) and Even (0 or 1) value depending on whether the class is offered in odd / even years or not
    query_7 = "SELECT CLASSES.ClassID, Odd, Even FROM dbo.CLASSES, dbo." + choose_table + " WHERE CLASSES.ClassID =" + choose_table + ".ClassID"
    cursor.execute(query_7)
    dict_7 = {}
    result_7 = cursor.fetchall()
    for tup in result_7:
        dict_7[tup[0]]=str(tup[1])+str(tup[2])

    
            #dictionary with ClassID for the key, value consists of a concatenated string of Fall (0 or 1) and Spring (0 or 1) value depending on whether the class is offered in the fall / spring or not


    #dictionary with ClassID for the key, value is a list of courseId, course title, credits, and aoi attributes
    query_8 = "SELECT CLASSES.ClassID, Credits FROM dbo.CLASSES, dbo." + choose_table + " WHERE CLASSES.ClassID =" + choose_table + ".ClassID"
    cursor.execute(query_8)
    dict_8 = {}
    result_8 = cursor.fetchall()
    for tup in result_8:
        try:
            aois = dict_6[tup[0]]
        except:
            aois = 'None'
        dict_8[tup[0]]=[tup[0], 'course title', float(tup[1]), aois] #update when DB has those capabilities
    #dictionary with ClassID for the key, value is the class Name
    query_9 = "SELECT CLASSES.ClassID, CLASSES.ClassName FROM dbo.CLASSES, dbo." + choose_table + " WHERE CLASSES.ClassID =" + choose_table + ".ClassID"
    cursor.execute(query_9)
    dict_9={}
    result_9= cursor.fetchall()
    for tup in result_9:
        dict_9[tup[0]]= tup[1]
   


    return (dict_1, dict_2,dict_3, dict_4, dict_5, dict_7, dict_8, dict_9)    
  
    



def get_electives(major):
    if major =="Accounting":
        dict = elective_dictionary("Accounting")
    elif major == "Actuarial Science":
        dict = elective_dictionary("Actuarial Science")
    elif major == "Business Law":
        dict = []
        dict.append(elective_dictionary("Business Law First"))
        dict.append(elective_dictionary("Business Law Second"))
        dict.append(elective_dictionary("Business Law Third"))
    elif major == "Economics":
        dict = elective_dictionary("Economics")
    return dict



#get electives returns the list of tables with all its attributes for a specific major.
#For the Accounting major, it returns the specifics regarding the Pick two accounting table where the student can pick two classes from it.

#For the Actuarial science major, it returns the specifics regarding Pick two actuarial science table where the student can pick  two classes

#For the Business Law major, it returns a list of three different tables (can be accessed with list indices). The index of 0 represents the First Business Law Pick one table
#where the student can pick one class. The index of 1 represents the Second Business Law Pick one table where the student can pick one class from that list as well.
#Lastly, the index of 2 represents the Business Law pick three table where the student must pick three classes from this table.

#For the Economics major, it returns a dictionary from the Choose four econ table, where the student must pick 4 classes from it.
print(get_electives("Actuarial Science"))
