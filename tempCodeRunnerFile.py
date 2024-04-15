query_9 = "SELECT CLASSES.ClassID, ClassName FROM dbo.CLASSES,dbo." + selectedMajor + "WHERE CLASSES.ClassID=" +selectedMajor + ".ClassID"
cursor.execute(query_9)
dict_9={}
result_9= cursor.fetchall()
print(result_9)