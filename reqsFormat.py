"""{
    "major_1": {
        "singles": [
            "class_key_1",
            "class_key_2",
            ...
        ],
        "pick_1_description1": [
            "class_key_3",
            "class_key_4",
            ...
        ],
        "pick_1_description2": [
            "class_key_5",
            "class_key_6",
            ...
        ],
        "pick_2_description3": [
            "class_key_7",
            "class_key_8",
            "class_key_9",
            "class_key_10",
            ...
        ],
    },
    "major_2": <major 2 requirements, similar to above>,
    "AOIs": <requirements, similarly indicating any pick-1s, etc.>,
    "total_credits": <min # of credits for graduation>
} """

from azuresqlconnector import *
from OrRequirements import *


def getRequirementsForFrontEnd(selectedMajorList):
    conn = SQLConnection()
    conn = conn.getConnection()
    cursor = conn.cursor()

    singlesTablesDict = {}
    pickTablesDict = {}
    majorRequirementsToFrontEnd = {}

    tableDict = {}
    tableDict["ACTUARIAL SCIENCE"] = ["ACT_SCI_MAJOR", "PICK_TWO_ACT_SCI"]
    tableDict["ACCOUNTING"] = ["ACCOUNTING_MAJOR", "PICK_TWO_ACC"]
    tableDict["ECONOMICS"] = ["ECON_MAJOR", "CHOOSE_FOUR_ECON"]
    tableDict["BUSINESS LAW"] = ["BLAW_MAJOR", "CHOOSE_THREE_BLAW"]
    tableDict["DATA ANALYTICS"] = ["DATA_ANALYTICS_MAJOR"]
    tableDict["FINANCE"] = ["FIN_MAJOR", "PICK_THREE_FIN"]
    tableDict["MANAGEMENT"] = ["MANAGEMENT_MAJOR"]

    for major in selectedMajorList:
        singlesTables = []
        pickTables = []
        for value in tableDict[major]:
            if "MAJOR" in value:
                singlesTables.append(value)
            else:
                pickTables.append(value)
            majorRequirementsToFrontEnd[major] = {}
        singlesTablesDict[major] = singlesTables
        pickTablesDict[major] = pickTables
        
        for key in singlesTablesDict[major]:
            query_0r = "SELECT CLASSES.ClassID, CLASSES.ClassName FROM dbo.CLASSES, dbo.BUSINESS_CORE, dbo." + key + " WHERE CLASSES.ClassID =" + key + ".ClassID OR CLASSES.ClassID = BUSINESS_CORE.ClassID"
            cursor.execute(query_0r)
            classList = []
            result = cursor.fetchall()
            for tup in result:
                if tup[1] not in classList:
                    classList.append(tup[1])
            majorRequirementsToFrontEnd[major] = {"singles": classList} #{"Individual Classes": classList}
            
        for tableName in pickTablesDict[major]:
            query_1r = "SELECT CLASSES.ClassID, CLASSES.ClassName FROM dbo.CLASSES, dbo." + tableName + " WHERE CLASSES.ClassID =" + tableName + ".ClassID"
            cursor.execute(query_1r)
            classList = []
            result = cursor.fetchall()
            for tup in result:
                if tup[1] not in classList:
                    classList.append(tup[1])
            if "CHOOSE" in tableName:
                tableName = tableName.replace("CHOOSE", "PICK")
            tableName = tableName.replace("_", " ")
            #need to get rid of things after second word
            indexFirstSpace = tableName.index(" ")
            temp = tableName[indexFirstSpace+1:]
            indexSecondSpace = temp.index(" ")
            tableName = tableName[0:indexSecondSpace + indexFirstSpace + 1]
            tableName = tableName.capitalize()
            majorRequirementsToFrontEnd[major][tableName] = classList
        
    requirementsToFrontEnd = {}
    requirementsToFrontEnd["majors"] = majorRequirementsToFrontEnd
    requirementsToFrontEnd["AOIs"] = {"pick_1_artistic_literacy": ['class 1', 'class 2'], "pick_1_randomAOI": ['class 1', 'class 2']}
    requirementsToFrontEnd["equity_and_inclusion"] = {"pick 1": ['thing1', 'thing2']}
    requirementsToFrontEnd["total credits"] = 120
    conn.commit()
    cursor.close()
    print(requirementsToFrontEnd)
    return requirementsToFrontEnd
    
getRequirementsForFrontEnd(["BUSINESS LAW", "ACCOUNTING"])