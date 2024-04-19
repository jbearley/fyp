from azuresqlconnector import *
from OrRequirements import *
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

conn.commit()
cursor.close()
