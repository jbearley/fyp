from azuresqlconnector import *
conn = SQLConnection()
conn = conn.getConnection()
cursor = conn.cursor()

query_6 = f"""
SELECT * FROM dbo.ACT_SCI_MAJOR
"""
cursor.execute(query_6)
result_6 = cursor.fetchall()
print("This is the actuarial science major table:")
for tup in result_6:
    print(tup)

    
conn.commit()
cursor.close()
    