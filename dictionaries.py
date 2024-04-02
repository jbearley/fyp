from azuresqlconnector import *
conn = SQLConnection()
conn = conn.getConnection()
cursor = conn.cursor()
    

#dictionary with Class Id for the key, Prerequisites for the value
query_1 = f"""
SELECT ClassID, Prereqs FROM dbo.CLASSES;
"""
cursor.execute(query_1)
dict_1 = {}
result = cursor.fetchall()
for tup in result:
    tup[1] = str(tup[1]).split(',')
    dict_1[tup[0]]=tup[1]


#dictionary with ClassID for the key, value consists of a concatenated string of Fall (0 or 1) and Spring (0 or 1) value depending on whether the class is offered in the fall / spring or not
query_2 = f"""
SELECT ClassID, Fall, Spring FROM dbo.CLASSES;
"""
cursor.execute(query_2)
dict_2 = {}
result_2 = cursor.fetchall()
for tup in result_2:
    dict_2[tup[0]]=str(tup[1])+str(tup[2])

#dictionary with ClassID for the key, number of credits for the value
query_3 = f"""
SELECT ClassID, Credits FROM dbo.CLASSES;
"""
cursor.execute(query_3)
dict_3 = {}
result_3 = cursor.fetchall()
for tup in result_3:
    dict_3[tup[0]]=tup[1]

#dictionary with ClassID for the key, grade requirement for the value. If no grade requirement, than it has None.
query_4 = f"""
SELECT ClassID, GradeReq FROM dbo.CLASSES;
"""
cursor.execute(query_4)
dict_4 = {}
result_4 = cursor.fetchall()
for tup in result_4:
    dict_4[tup[0]]=tup[1]

#dictionary with ClassID for the key, corequisities for the value. If no corequisities, then the value is None.
query_5 = f"""
SELECT ClassID, Coreq FROM dbo.CLASSES;
"""
cursor.execute(query_5)
dict_5 = {}
result_5 = cursor.fetchall()
for tup in result_5:
    dict_5[tup[0]]=tup[1]

query_6 = f"""
SELECT ClassID, AOI FROM dbo.AOI
"""
cursor.execute(query_6)
dict_6 = {}
result_6 = cursor.fetchall()
for tup in result_6:
    dict_6[tup[0]]= tup[1]
print(dict_6)
conn.commit()
cursor.close()

#print(dict_1)
#print(dict_1['ACCT 42'])