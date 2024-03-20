from azuresqlconnector import *
conn = SQLConnection()
conn = conn.getConnection()
cursor = conn.cursor()

query = f"""
SELECT * FROM dbo.CLASSES;
"""
cursor.execute(query)
result = cursor.fetchall()
print("This is the classes table:")
for tup in result:
    print(tup)

print("\n")
query_2 = f"""
SELECT * FROM dbo.PICKONE
"""
cursor.execute(query_2)
result_2 = cursor.fetchall()
print("This is the pickone table:")
for tup in result_2:
    print(tup)


conn.commit()
cursor.close()