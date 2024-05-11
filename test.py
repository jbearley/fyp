from azuresqlconnector import *
conn = SQLConnection()
conn = conn.getConnection()
cursor = conn.cursor()

print("\n")
query_23 = f"""
SELECT * FROM dbo.MANAGEMENT_MINOR
"""
cursor.execute(query_23)
result_23 = cursor.fetchall()
print("This is the management minor table:")
for tup in result_23:
    print(tup)

conn.commit()
cursor.close()