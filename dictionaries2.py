from azuresqlconnector import *
from OrRequirements import *
import random


def createDictionaries(selectedMajorList, selectedMinorList):
    conn = SQLConnection()
    conn = conn.getConnection()
    cursor = conn.cursor()
    tableList = []
    pickTables = []
    #selectedMajor1 = selectedMajorList[0]
    if "ACTUARIAL SCIENCE" in selectedMajorList:
        tableList.append("ACT_SCI_MAJOR")
        tableList.append("CHOOSE_TWO_ACT_SCI")
    if "ACCOUNTING" in selectedMajorList:
        tableList.append("ACCOUNTING_MAJOR")
        tableList.append("CHOOSE_TWO_ACC")
    if "ECONOMICS (BSBA)" in selectedMajorList:
        tableList.append("ECON_MAJOR")
        tableList.append("CHOOSE_FOUR_ECON")
    if "BUSINESS LAW" in selectedMajorList:
        tableList.append("BLAW_MAJOR")
        tableList.append("CHOOSE_THREE_BLAW")
    if "DATA ANALYTICS" in selectedMajorList:
        tableList.append("DATA_ANALYTICS_MAJOR")
    if "FINANCE" in selectedMajorList:
        tableList.append("FIN_MAJOR")
        tableList.append("CHOOSE_THREE_FIN")
    if "MANAGEMENT" in selectedMajorList:
        tableList.append("MANAGEMENT_MAJOR")
    #Minors
    if "ACCOUNTING" in selectedMinorList:
        tableList.append("ACCOUNTING_MINOR")
    if "ACTUARIAL SCIENCE" in selectedMinorList:
        tableList.append("ACT_SCI_MINOR")
    if "BUSINESS LAW" in selectedMinorList:
        tableList.append("BLAW_MINOR")
        tableList.append("PICK_TWO_BLAW_MINOR")
    if "DATA ANALYTICS" in selectedMinorList:
        tableList.append("DATA_ANALYTICS_MINOR")
    if "ECONOMICS" in selectedMinorList:
        tableList.append("ECON_MINOR")
        tableList.append("PICK_THREE_ECON_MINOR")
    if "FINANCE" in selectedMinorList:
        tableList.append("ACCOUNTING_MINOR")
    if "INFORMATION SYSTEMS" in selectedMinorList:
        tableList.append("INFO_SYSTEMS_MINOR")
    if "MANAGEMENT" in selectedMinorList:
        tableList.append("MANAGEMENT_MINOR")
        tableList.append("PICK_THREE_MAANGEMENT_MINOR")
        
        
    for a in tableList:
        if "MAJOR" not in a and "MINOR" not in a:
            tableList.remove(a) #pick tables for majors
            pickTables.append(a)
        if "MINOR" in a and "PICK" in a:
            tableList.remove(a) #pick tables for minors
            pickTables.append(a)
            
    print(tableList)
            
    if len(tableList) == 1:
        query_1 = "SELECT CLASSES.ClassID, Prereqs FROM dbo.CLASSES, dbo.BUSINESS_CORE, dbo." + tableList[0] + " WHERE CLASSES.ClassID =" + tableList[0] + ".ClassID OR CLASSES.ClassID = BUSINESS_CORE.ClassID"
    elif len(tableList) == 2:
        query_1 = "SELECT CLASSES.ClassID, Prereqs FROM dbo.CLASSES, dbo.BUSINESS_CORE, dbo." + tableList[0] + ",dbo." + tableList[1] + " WHERE CLASSES.ClassID =" + tableList[0] + ".ClassID OR CLASSES.ClassID =" + tableList[1] + ".ClassID OR CLASSES.ClassID = BUSINESS_CORE.ClassID"
    elif len(tableList) == 3:
        query_1 = "SELECT CLASSES.ClassID, Prereqs FROM dbo.CLASSES, dbo.BUSINESS_CORE, dbo." + tableList[0] + ",dbo." + tableList[1] + ",dbo." + tableList[2] + " WHERE CLASSES.ClassID =" + tableList[0] + ".ClassID OR CLASSES.ClassID =" + tableList[1] + ".ClassID OR CLASSES.ClassID =" + tableList[2] + ".ClassID OR CLASSES.ClassID = BUSINESS_CORE.ClassID"
    elif len(tableList) == 4:
        query_1 = "SELECT CLASSES.ClassID, Prereqs FROM dbo.CLASSES, dbo.BUSINESS_CORE, dbo." + tableList[0] + ",dbo." + tableList[1] + ",dbo." + tableList[2] + ",dbo." + tableList[3] + " WHERE CLASSES.ClassID =" + tableList[0] + ".ClassID OR CLASSES.ClassID =" + tableList[1] + ".ClassID OR CLASSES.ClassID =" + tableList[2] + ".ClassID OR CLASSES.ClassID =" + tableList[3] + ".ClassID OR CLASSES.ClassID = BUSINESS_CORE.ClassID"
    elif len(tableList) == 5:
        query_1 = "SELECT CLASSES.ClassID, Prereqs FROM dbo.CLASSES, dbo.BUSINESS_CORE, dbo." + tableList[0] + ",dbo." + tableList[1] + ",dbo." + tableList[2] + ",dbo." + tableList[3] + ",dbo." + tableList[4] + " WHERE CLASSES.ClassID =" + tableList[0] + ".ClassID OR CLASSES.ClassID =" + tableList[1] + ".ClassID OR CLASSES.ClassID =" + tableList[2] + ".ClassID OR CLASSES.ClassID =" + tableList[3] + ".ClassID OR CLASSES.ClassID =" + tableList[4] + ".ClassID OR CLASSES.ClassID = BUSINESS_CORE.ClassID"
    else:
        query_1 = "SELECT CLASSES.ClassID, Prereqs FROM dbo.CLASSES, dbo.BUSINESS_CORE, dbo." + tableList[0] + ",dbo." + tableList[1] + ",dbo." + tableList[2] + ",dbo." + tableList[3] + ",dbo." + tableList[4] + ",dbo." + tableList[5] + " WHERE CLASSES.ClassID =" + tableList[0] + ".ClassID OR CLASSES.ClassID =" + tableList[1] + ".ClassID OR CLASSES.ClassID =" + tableList[2] + ".ClassID OR CLASSES.ClassID =" + tableList[3] + ".ClassID OR CLASSES.ClassID =" + tableList[4] + ".ClassID OR CLASSES.ClassID =" + tableList[5] + ".ClassID OR CLASSES.ClassID = BUSINESS_CORE.ClassID"
    
    cursor.execute(query_1)
    dict_1 = {}
    result = cursor.fetchall()
    for tup in result:
        tup[1] = str(tup[1]).split(', ')
        for a in tup[1]:
            if a[0] == " ":
                a = a[1:]
        dict_1[tup[0]]=tup[1]
    
    for pick_table in pickTables:
        #query the database to get courses from pick table
        query_1b = "SELECT dbo." + pick_table + ".ClassID FROM dbo." + pick_table
        cursor.execute(query_1b)
        #store courseIDs in a list
        list1 = []
        result = cursor.fetchall()
        for tup in result:
            list1.append(tup[0])
        #temp fix - remove any classes with pre-reqs not involved in major/minor
        if "STAT 172" in list1:
            list1.remove("STAT 172")
        if "FIN" in pick_table:
            for a in ["CS 167", "ACCT 120", "ACCT 175", "AACT 165", "ACCT 166"]:
                if a in list1:
                    list1.remove(a)
        if "ECON" in pick_table:
            if "ECON 198" in list1:
                list1.remove("ECON 198")
        if "BLAW" in pick_table:
            if "ENTR 150" in list1:
                list1.remove("ENTR 150")
        #figure out, from table name, how many X is
        indexFirstSpace = pick_table.index("_")
        temp = pick_table[indexFirstSpace+1:]
        indexSecondSpace = temp.index("_")
        number = temp[:indexSecondSpace]
        if number.lower() == "one":
            number = 1
        elif number.lower() == "two":
            number = 2
        elif number.lower() == "three":
            number = 3
        elif number.lower() == "four":
            number = 4
        elif number.lower() == "five":
            number = 5
        #pick X random courses from the list, put in list2
        list2 = []
        if "ACC" in pick_table:
            randomNum1 = random.randrange(0,2)
            list2.append(list1[randomNum1])
            while number != 1:
                randomNum2 = random.randrange(2,len(list1))
                list2.append(list1[randomNum2])
                list1.remove(list1[randomNum2])
                number -= 1
        else:
            list2 = random.sample(list1, number)
        print("!!!", pick_table, list2)
        #query the CLASSES table with where courseID IN list2
        strList2 = "('" + list2[0]
        for item in list2:
            if item != list2[0]:
                strList2 += "', '" + str(item)
        strList2 += "')"
        print(strList2)
        query_1c = query_1 = "SELECT CLASSES.ClassID, Prereqs FROM dbo.CLASSES WHERE CLASSES.ClassID IN " + strList2
        #add new values to dict_1
        cursor.execute(query_1c)
        result = cursor.fetchall()
        for tup in result:
            tup[1] = str(tup[1]).split(', ')
            for a in tup[1]:
                if a[0] == " ":
                    a = a[1:]
            dict_1[tup[0]]=tup[1]
    
    if "FIN 101" in dict_1:
        dict_1["FIN 101"] = ["ACCT 42", "IS 44", "ECON 02", "STAT 71/STAT 130/ACTS 131"]
    if "MGMT 120" in dict_1:
        dict_1["MGMT 120"] = ["STAT 72/ACTS 135"]
    if "STAT 172" in dict_1:
        dict_1["STAT 172"] = ['STAT 130/ACTS 131', 'STAT 40', 'STAT 170', 'MATH 70']
    if "ECON 190" in dict_1:
        dict_1["ECON 190"] = ["ECON 170/STAT 170"]
    dict_1 = dealWithOrReqs(dict_1)
    if "ACTS 140" in dict_1 and "ACT 135" in dict_1["ACTS 140"]:
        dict_1["ACTS 140"].remove("ACT 135")
        dict_1["ACTS 140"].append("ACTS 135") 
    if "ECON 170" in dict_1 and "MATH 28" in dict_1["ECON 170"]:
        dict_1["ECON 170"].remove("MATH 28")
    if "ECON 105" in dict_1 and "MATH 28" in dict_1["ECON 105"]:
        dict_1["ECON 105"].remove("MATH 28")
    if "ECON 109" in dict_1 and "MATH 28" in dict_1["ECON 109"]:
        dict_1["ECON 109"].remove("MATH 28")
    if "ECON 115" in dict_1 and "MATH 28" in dict_1["ECON 115"]:
        dict_1["ECON 115"].remove("MATH 28")
    if "ECON 120" in dict_1 and "MATH 28" in dict_1["ECON 120"]:
        dict_1["ECON 120"].remove("MATH 28")
    if "ECON 130" in dict_1 and "MATH 28" in dict_1["ECON 130"]:
        dict_1["ECON 130"].remove("MATH 28")
    if "ECON 135" in dict_1 and "MATH 28" in dict_1["ECON 135"]:
        dict_1["ECON 135"].remove("MATH 28")
    if "ECON 174" in dict_1 and "MATH 28" in dict_1["ECON 174"]:
        dict_1["ECON 174"].remove("MATH 28")
    if "ECON 131" in dict_1 and "MATH 28" in dict_1["ECON 131"]:
        dict_1["ECON 131"].remove("MATH 28")
    if "CS 65" in dict_1 and "MATH 20" in dict_1["CS 65"]:
        dict_1["CS 65"].remove("MATH 20")
    if "ECON 108" in dict_1 and "MATH 17" in dict_1["ECON 108"]:
        dict_1["ECON 108"].remove("MATH 17")
    if "ECON 135" in dict_1 and "MATH 17" in dict_1["ECON 135"]:
        dict_1["ECON 135"].remove("MATH 17")
    if "BUS 70" in dict_1 and "BUS 70" in dict_1["BUS 70"]:
        dict_1["BUS 70"].append('None')
        dict_1["BUS 70"].remove("BUS 70")
    #print("major:", selectedMajor)
    #print(dict_1, "\n\n")
    
    #dictionary with ClassID for the key, value consists of a concatenated string of Fall (0 or 1) and Spring (0 or 1) value depending on whether the class is offered in the fall / spring or not
    query_2 = "SELECT CLASSES.ClassID, Fall, Spring FROM dbo.CLASSES"#, dbo." + selectedMajor + " WHERE CLASSES.ClassID =" + selectedMajor + ".ClassID"
    cursor.execute(query_2)
    dict_2 = {}
    result_2 = cursor.fetchall()
    for tup in result_2:
        dict_2[tup[0]]=str(tup[1])+str(tup[2])
    #print(dict_2)

    #dictionary with ClassID for the key, number of credits for the value
    query_3 = "SELECT CLASSES.ClassID, Credits FROM dbo.CLASSES"#, dbo." + selectedMajor + " WHERE CLASSES.ClassID =" + selectedMajor + ".ClassID"
    cursor.execute(query_3)
    dict_3 = {}
    result_3 = cursor.fetchall()
    for tup in result_3:
        dict_3[tup[0]]=tup[1]
        
    #dictionary with ClassID for the key, grade requirement for the value. If no grade requirement, than it has None.
    query_4 = "SELECT CLASSES.ClassID, GradeReq FROM dbo.CLASSES"#, dbo." + selectedMajor + " WHERE CLASSES.ClassID =" + selectedMajor + ".ClassID"
    cursor.execute(query_4)
    dict_4 = {}
    result_4 = cursor.fetchall()
    for tup in result_4:
        dict_4[tup[0]]=tup[1]

    #dictionary with ClassID for the key, corequisities for the value. If no corequisities, then the value is None.
    query_5 = "SELECT CLASSES.ClassID, Coreq FROM dbo.CLASSES"#, dbo." + selectedMajor + " WHERE CLASSES.ClassID =" + selectedMajor + ".ClassID"
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
                popped_classes[dict_5[key]]=key
                if "ACTS 120L" in popped_classes:
                    del popped_classes["ACTS 120L"]
                dict_1.pop(key)
    if "ACTS 120" in dict_1 or "ACTS 120L" in dict_1:
        popped_classes["ACTS 120"] = "ACTS 120L"
    if "ACTS 120L" in dict_1:
        dict_1.pop("ACTS 120L")
                
    
    for key in popped_classes:
        if key in dict_3:
            dict_3[key] = float(dict_3[key]) + .5
        
    query_6 = f"""
    SELECT CLASSES.ClassID, AOI FROM dbo.AOI, dbo.CLASSES WHERE dbo.CLASSES.ClassID = dbo.AOI.ClassID
    """
    cursor.execute(query_6)
    dict_6 = {}
    result_6 = cursor.fetchall()
    for tup in result_6:
        dict_6[tup[0]]= tup[1] 
        
    #dictionary with ClassID for the key, value consists of a concatenated string of Odd (0 or 1) and Even (0 or 1) value depending on whether the class is offered in odd / even years or not
    query_7 = "SELECT CLASSES.ClassID, Odd, Even FROM dbo.CLASSES"#, dbo." + selectedMajor + " WHERE CLASSES.ClassID =" + selectedMajor + ".ClassID"
    cursor.execute(query_7)
    dict_7 = {}
    result_7 = cursor.fetchall()
    for tup in result_7:
        dict_7[tup[0]]=str(tup[1])+str(tup[2])

    #dictionary with ClassID for the key, value is a list of courseId, course title, credits, and aoi attributes
    query_8 = "SELECT CLASSES.ClassID, Credits FROM dbo.CLASSES"#, dbo." + selectedMajor + " WHERE CLASSES.ClassID =" + selectedMajor + ".ClassID"
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
    query_9 = "SELECT CLASSES.ClassID, CLASSES.ClassName FROM dbo.CLASSES"#, dbo." + selectedMajor + " WHERE CLASSES.ClassID =" + selectedMajor + ".ClassID"
    cursor.execute(query_9)
    dict_9={}
    result_9= cursor.fetchall()
    for tup in result_9:
        dict_9[tup[0]]= tup[1]

        
    conn.commit()
    cursor.close()
    return (dict_1, dict_2, dict_3, dict_4, dict_5, dict_6, dict_7, dict_8, dict_9, popped_classes)


#print(createDictionaries("Economics"))