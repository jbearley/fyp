from azuresqlconnector import *
conn = SQLConnection()
conn = conn.getConnection()
cursor = conn.cursor()

query_1 = f"""
SELECT ClassID, Prereqs FROM dbo.CLASSES;
"""
cursor.execute(query_1)
dict_1 = {}
result = cursor.fetchall()
for tup in result:
    dict_1[tup[0]]=tup[1]
print(result)

query_2 = f"""
SELECT ClassID, Fall, Spring FROM dbo.CLASSES;
"""
cursor.execute(query_2)
dict_2 = {}
result_2 = cursor.fetchall()
for tup in result_2:
    dict_2[tup[0]]=str(tup[1])+str(tup[2])

query_3 = f"""
SELECT ClassID, Credits FROM dbo.CLASSES;
"""
cursor.execute(query_3)
dict_3 = {}
result_3 = cursor.fetchall()
for tup in result_3:
    dict_3[tup[0]]=tup[1]



conn.commit()
cursor.close()