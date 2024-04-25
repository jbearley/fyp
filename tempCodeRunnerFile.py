from azuresqlconnector import *
conn = SQLConnection()
conn = conn.getConnection()
cursor = conn.cursor()

print("\n")
query_17 = f"""
SELECT * FROM dbo.ACT_SCI_MINOR
"""
cursor.execute(query_17)
result_17 = cursor.fetchall()
print("This is the Actuarial science minor table:")
for tup in result_17:
    print(tup)

conn.commit()
cursor.close()