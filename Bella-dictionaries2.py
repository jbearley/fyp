from azuresqlconnector import *
from OrRequirements import *

def createDictionaries(selectedMajor1):
    conn = SQLConnection()
    conn = conn.getConnection()
    cursor = conn.cursor()
    #this will have to be done for all majors
    if selectedMajor1 == "ACTUARIAL SCIENCE":
        selectedMajor = "ACT_SCI_MAJOR"
    elif selectedMajor1 == "ACCOUNTING":
        selectedMajor = "ACCOUNTING_MAJOR"
    elif selectedMajor1 == "ECONOMICS":
        selectedMajor = "ECON_MAJOR"
    elif selectedMajor1 == "BUSINESS LAW":
        selectedMajor = "BLAW_MAJOR"

    #dictionary with Class Id for the key, Prerequisites for the value
    query_1 = "SELECT CLASSES.ClassID, Prereqs FROM dbo.CLASSES, dbo.BUSINESS_CORE, dbo." + selectedMajor + " WHERE CLASSES.ClassID =" + selectedMajor + ".ClassID OR CLASSES.ClassID = BUSINESS_CORE.ClassID"
    cursor.execute(query_1)
    dict_1 = {}
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
    if "ECON 190" in dict_1:
        dict_1["ECON 190"] = ["ECON 170/STAT 170"]
    dict_1 = dealWithOrReqs(dict_1)
    if "ACTS 140" in dict_1 and "ACT 135" in dict_1["ACTS 140"]:
        dict_1["ACTS 140"].remove("ACT 135")
        dict_1["ACTS 140"].append("ACTS 135") 
    if "ECON 170" in dict_1 and "MATH 28" in dict_1["ECON 170"]:
        dict_1["ECON 170"].remove("MATH 28") #what curriculum is the econ major stuff from?
    #print("major:", selectedMajor)
    #(dict_1, "\n\n")

    #dictionary with ClassID for the key, value consists of a concatenated string of Fall (0 or 1) and Spring (0 or 1) value depending on whether the class is offered in the fall / spring or not
    query_2 = "SELECT CLASSES.ClassID, Fall, Spring FROM dbo.CLASSES"#, dbo.BUSINESS_CORE, dbo." + selectedMajor + " WHERE CLASSES.ClassID =" + selectedMajor + ".ClassID OR CLASSES.ClassID = BUSINESS_CORE.ClassID"
    cursor.execute(query_2)
    dict_2 = {}
    result_2 = cursor.fetchall()
    for tup in result_2:
        dict_2[tup[0]]=str(tup[1])+str(tup[2])
    #print(dict_2)

    #dictionary with ClassID for the key, number of credits for the value
    query_3 = "SELECT CLASSES.ClassID, Credits FROM dbo.CLASSES"# , dbo.BUSINESS_CORE, dbo." + selectedMajor + " WHERE CLASSES.ClassID =" + selectedMajor + ".ClassID OR CLASSES.ClassID = BUSINESS_CORE.ClassID"
    cursor.execute(query_3)
    dict_3 = {}
    result_3 = cursor.fetchall()
    for tup in result_3:
        dict_3[tup[0]]=tup[1]

    #dictionary with ClassID for the key, grade requirement for the value. If no grade requirement, than it has None.
    query_4 = "SELECT CLASSES.ClassID, GradeReq FROM dbo.CLASSES"#, dbo.BUSINESS_CORE, dbo." + selectedMajor + " WHERE CLASSES.ClassID =" + selectedMajor + ".ClassID OR CLASSES.ClassID = BUSINESS_CORE.ClassID"

    cursor.execute(query_4)
    dict_4 = {}
    result_4 = cursor.fetchall()
    for tup in result_4:
        dict_4[tup[0]]=tup[1]

    #dictionary with ClassID for the key, corequisities for the value. If no corequisities, then the value is None.
    query_5 = "SELECT CLASSES.ClassID, Coreq FROM dbo.CLASSES"#, dbo.BUSINESS_CORE, dbo." + selectedMajor + " WHERE CLASSES.ClassID =" + selectedMajor + ".ClassID OR CLASSES.ClassID = BUSINESS_CORE.ClassID"
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
    query_7 = "SELECT CLASSES.ClassID, Odd, Even FROM dbo.CLASSES"#, dbo.BUSINESS_CORE, dbo." + selectedMajor + " WHERE CLASSES.ClassID =" + selectedMajor + ".ClassID OR CLASSES.ClassID = BUSINESS_CORE.ClassID"
    cursor.execute(query_7)
    dict_7 = {}
    result_7 = cursor.fetchall()
    for tup in result_7:
        dict_7[tup[0]]=str(tup[1])+str(tup[2])

    #dictionary with ClassID for the key, value is a list of courseId, course title, credits, and aoi attributes
    query_8 = "SELECT CLASSES.ClassID, Credits FROM dbo.CLASSES"#, dbo.BUSINESS_CORE, dbo." + selectedMajor + " WHERE CLASSES.ClassID =" + selectedMajor + ".ClassID OR CLASSES.ClassID = BUSINESS_CORE.ClassID"
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
    query_9 = "SELECT CLASSES.ClassID, CLASSES.ClassName FROM dbo.CLASSES"#, dbo.BUSINESS_CORE, dbo." + selectedMajor + " WHERE CLASSES.ClassID =" + selectedMajor + ".ClassID OR CLASSES.ClassID = BUSINESS_CORE.ClassID"
    cursor.execute(query_9)
    dict_9={}
    result_9= cursor.fetchall()
    for tup in result_9:
        dict_9[tup[0]]= tup[1]

    conn.commit()
    cursor.close()
    return (dict_1, dict_2, dict_3, dict_4, dict_5, dict_6, dict_7, dict_8, dict_9)


#print(createDictionaries("Actuarial Science"))