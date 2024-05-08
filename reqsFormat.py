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


def getRequirementsForFrontEnd(selectedMajorList, selectedMinorList):
    conn = SQLConnection()
    conn = conn.getConnection()
    cursor = conn.cursor()


    #MAJORS --------------------------------------------------------------------------------------------------
    singlesTablesDict = {}
    pickTablesDict = {}
    majorRequirementsToFrontEnd = {}

    tableDict = {}
    tableDict["ACTUARIAL SCIENCE"] = ["ACT_SCI_MAJOR", "CHOOSE_TWO_ACT_SCI"]
    tableDict["ACCOUNTING"] = ["ACCOUNTING_MAJOR", "CHOOSE_TWO_ACC"]
    tableDict["ECONOMICS (BSBA)"] = ["ECON_MAJOR", "CHOOSE_FOUR_ECON"]
    tableDict["BUSINESS LAW"] = ["BLAW_MAJOR", "CHOOSE_THREE_BLAW"]
    tableDict["DATA ANALYTICS"] = ["DATA_ANALYTICS_MAJOR"]
    tableDict["FINANCE"] = ["FIN_MAJOR", "CHOOSE_THREE_FIN"]
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
            #tableName = tableName.replace("_", " ")
            #need to get rid of things after second word
            indexFirstSpace = tableName.index("_")
            temp = tableName[indexFirstSpace+1:]
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
            tableName = tableName[0:indexFirstSpace + 1] + str(number)
            tableName = tableName.lower()
            tableName2 = tableName.replace("_", " ")
            tableName = tableName + "_" + tableName2
            majorRequirementsToFrontEnd[major][tableName] = classList
            
            
    #MINORS ------------------------------------------------------------------------------------------------------------
    singlesTablesDict = {}
    pickTablesDict = {}
    minorRequirementsToFrontEnd = {}

    tableDict = {}
    tableDict["ACTUARIAL SCIENCE"] = ["ACT_SCI_MINOR"]
    tableDict["ACCOUNTING"] = ["ACCOUNTING_MINOR"]
    tableDict["ECONOMICS"] = ["ECON_MINOR", "PICK_FOUR_ECON_MINOR"]
    tableDict["BUSINESS LAW"] = ["BLAW_MINOR", "PICK_TWO_BLAW"]
    tableDict["DATA ANALYTICS"] = ["DATA_ANALYTICS_MINOR"]
    tableDict["MANAGEMENT"] = ["PICK_THREE_MANAGEMENT_MINOR"]

    for minor in selectedMinorList:
        singlesTables = []
        pickTables = []
        for value in tableDict[minor]:
            if "PICK" in value or "CHOOSE" in value:
                pickTables.append(value)
            else:
                singlesTables.append(value)
            minorRequirementsToFrontEnd[minor] = {}
        singlesTablesDict[minor] = singlesTables
        pickTablesDict[minor] = pickTables
        
        for key in singlesTablesDict[minor]:
            query_0r = "SELECT CLASSES.ClassID, CLASSES.ClassName FROM dbo.CLASSES, dbo.BUSINESS_CORE, dbo." + key + " WHERE CLASSES.ClassID =" + key + ".ClassID OR CLASSES.ClassID = BUSINESS_CORE.ClassID"
            cursor.execute(query_0r)
            classList = []
            result = cursor.fetchall()
            for tup in result:
                if tup[1] not in classList:
                    classList.append(tup[1])
            majorRequirementsToFrontEnd[minor] = {"singles": classList} #{"Individual Classes": classList}
            
        for tableName in pickTablesDict[minor]:
            query_1r = "SELECT CLASSES.ClassID, CLASSES.ClassName FROM dbo.CLASSES, dbo." + tableName + " WHERE CLASSES.ClassID =" + tableName + ".ClassID"
            cursor.execute(query_1r)
            classList = []
            result = cursor.fetchall()
            for tup in result:
                if tup[1] not in classList:
                    classList.append(tup[1])
            if "CHOOSE" in tableName:
                tableName = tableName.replace("CHOOSE", "PICK")
            #tableName = tableName.replace("_", " ")
            #need to get rid of things after second word
            indexFirstSpace = tableName.index("_")
            temp = tableName[indexFirstSpace+1:]
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
            tableName = tableName[0:indexFirstSpace + 1] + str(number)
            tableName = tableName.lower()
            tableName2 = tableName.replace("_", " ")
            tableName = tableName + "_" + tableName2
            minorRequirementsToFrontEnd[minor][tableName] = classList

    #PUT EVERYTHING TOGETHER ---------------------------------------------------------------------------------------
    
    requirementsToFrontEnd = {}
    requirementsToFrontEnd["total_credits"] = 120
    requirementsToFrontEnd.update(majorRequirementsToFrontEnd)
    requirementsToFrontEnd.update(minorRequirementsToFrontEnd)
    #requirementsToFrontEnd["equity_and_inclusion"] = {"pick_1": ['thing1', 'thing2']}
    #requirementsToFrontEnd["AOIs"] = {"pick_1_Artistic Literacy": ['class 1', 'class 2'], "pick_1_randomAOI": ['class 1', 'class 2']}
    requirementsToFrontEnd["AOIs"] = {'pick_1_Artistic Literacy': [],'pick_1_Critical Thinking': [],'pick_1_Engaged Citizen': [],'pick_1_Global & Cultural Understanding': [],'pick_2_Historical Foundations': [],'pick_1_Information Literacy': [],'pick_1_Quantitative Literacy': [],'pick_2_Scientific Literacy': [],'pick_1_Values and Ethics': [],'pick_1_Written Communication': []}
    conn.commit()
    cursor.close()
    print(requirementsToFrontEnd)
    return requirementsToFrontEnd
    
#getRequirementsForFrontEnd(["BUSINESS LAW", "ACCOUNTING"])