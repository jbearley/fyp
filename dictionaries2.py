from azuresqlconnector import *
conn = SQLConnection()
conn = conn.getConnection()
cursor = conn.cursor()


def createDictionaries(selectedMajor):
    #this will have to be done for all majors
    selectedMajor = "Actuarial Science" #get this from frontend
    if selectedMajor == "Actuarial Science":
        selectedMajor = "ACT_SCI_MAJOR"



    #dictionary with Class Id for the key, Prerequisites for the value
    query_1 = "SELECT CLASSES.ClassID, Prereqs FROM dbo.CLASSES, dbo." + selectedMajor + " WHERE CLASSES.ClassID =" + selectedMajor + ".ClassID"
    cursor.execute(query_1)
    dict_1 = {}
    result = cursor.fetchall()
    for tup in result:
        tup[1] = str(tup[1]).split(', ')
        for a in tup[1]:
            if a[0] == " ":
                a = a[1:]
        dict_1[tup[0]]=tup[1]
    dict_1["ACTS 140"] = ["ACTS 135"]

    #dictionary with ClassID for the key, value consists of a concatenated string of Fall (0 or 1) and Spring (0 or 1) value depending on whether the class is offered in the fall / spring or not
    query_2 = "SELECT CLASSES.ClassID, Fall, Spring FROM dbo.CLASSES, dbo." + selectedMajor + " WHERE CLASSES.ClassID =" + selectedMajor + ".ClassID"
    cursor.execute(query_2)
    dict_2 = {}
    result_2 = cursor.fetchall()
    for tup in result_2:
        dict_2[tup[0]]=str(tup[1])+str(tup[2])

    #dictionary with ClassID for the key, number of credits for the value
    query_3 = "SELECT CLASSES.ClassID, Credits FROM dbo.CLASSES, dbo." + selectedMajor + " WHERE CLASSES.ClassID =" + selectedMajor + ".ClassID"
    cursor.execute(query_3)
    dict_3 = {}
    result_3 = cursor.fetchall()
    for tup in result_3:
        dict_3[tup[0]]=tup[1]

    #dictionary with ClassID for the key, grade requirement for the value. If no grade requirement, than it has None.
    query_4 = "SELECT CLASSES.ClassID, GradeReq FROM dbo.CLASSES, dbo." + selectedMajor + " WHERE CLASSES.ClassID =" + selectedMajor + ".ClassID"
    cursor.execute(query_4)
    dict_4 = {}
    result_4 = cursor.fetchall()
    for tup in result_4:
        dict_4[tup[0]]=tup[1]

    #dictionary with ClassID for the key, corequisities for the value. If no corequisities, then the value is None.
    query_5 = "SELECT CLASSES.ClassID, Coreq FROM dbo.CLASSES, dbo." + selectedMajor + " WHERE CLASSES.ClassID =" + selectedMajor + ".ClassID"
    cursor.execute(query_5)
    dict_5 = {}
    result_5 = cursor.fetchall()
    for tup in result_5:
        dict_5[tup[0]]=tup[1]
        
    #dictionary with ClassID for the key, value consists of a concatenated string of Odd (0 or 1) and Even (0 or 1) value depending on whether the class is offered in odd / even years or not
    query_7 = "SELECT CLASSES.ClassID, Odd, Even FROM dbo.CLASSES, dbo." + selectedMajor + " WHERE CLASSES.ClassID =" + selectedMajor + ".ClassID"
    cursor.execute(query_7)
    dict_7 = {}
    result_7 = cursor.fetchall()
    for tup in result_7:
        dict_7[tup[0]]=str(tup[1])+str(tup[2])

    #dictionary with ClassID for the key, value is a list of courseId, course title, credits, and aoi attributes
    query_8 = "SELECT CLASSES.ClassID, Credits FROM dbo.CLASSES, dbo." + selectedMajor + " WHERE CLASSES.ClassID =" + selectedMajor + ".ClassID"
    cursor.execute(query_8)
    dict_8 = {}
    result_8 = cursor.fetchall()
    for tup in result_8:
        dict_8[tup[0]]=[tup[0], 'course title', tup[1], 'aoi attributes'] #update when DB has those capabilities
        
    conn.commit()
    cursor.close()
    return (dict_1, dict_2, dict_3, dict_4, dict_5, dict_7, dict_8)