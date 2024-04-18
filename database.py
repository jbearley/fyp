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
SELECT * FROM dbo.BUSINESS_CORE
"""
cursor.execute(query_2)
result_2 = cursor.fetchall()
print("This is the business core table:")
for tup in result_2:
    print(tup)

print("\n")
query_3 = f"""
SELECT * FROM dbo.ACCOUNTING_MAJOR
"""
cursor.execute(query_3)
result_3 = cursor.fetchall()
print("This is the accounting major table:")
for tup in result_3:
    print(tup)

print("\n")
query_4 = f"""
SELECT * FROM dbo.PICK_TWO_ACC
"""
cursor.execute(query_4)
result_4 = cursor.fetchall()
print("This is the pick two accounting table:")
for tup in result_4:
    print(tup)

print("\n")
query_5 = f"""
SELECT * FROM dbo.ACT_SCI_MAJOR
"""
cursor.execute(query_5)
result_5 = cursor.fetchall()
print("This is the actuarial science major table:")
for tup in result_5:
    print(tup)

print("\n")
query_6 = f"""
SELECT * FROM dbo.PICK_TWO_ACT_SCI
"""
cursor.execute(query_6)
result_6 = cursor.fetchall()
print("This is the pick two actuarial science table:")
for tup in result_6:
    print(tup)

print("\n")
query_7 = f"""
SELECT * FROM dbo.BLAW_MAJOR
"""
cursor.execute(query_7)
result_7 = cursor.fetchall()
print("This is the business law major table:")
for tup in result_7:
    print(tup)

print("\n")
query_8 = f"""
SELECT * FROM dbo.CHOOSE_THREE_BLAW
"""
cursor.execute(query_8)
result_8 = cursor.fetchall()
print("This is the choose three business law table:")
for tup in result_8:
    print(tup)


print("\n")
query_9 = f"""
SELECT * FROM dbo.ECON_MAJOR
"""
cursor.execute(query_9)
result_9 = cursor.fetchall()
print("This is the econ major table:")
for tup in result_9:
    print(tup)

print("\n")
query_10 = f"""
SELECT * FROM dbo.CHOOSE_FOUR_ECON
"""
cursor.execute(query_10)
result_10 = cursor.fetchall()
print("This is the choose four econ table:")
for tup in result_10:
    print(tup)

print("\n")
query_11 = f"""
SELECT * FROM dbo.DATA_ANALYTICS_MAJOR
"""
cursor.execute(query_11)
result_11 = cursor.fetchall()
print("This is the Data Analytics major table:")
for tup in result_11:
    print(tup)

print("\n")
query_12 = f"""
SELECT * FROM dbo.FIN_MAJOR
"""
cursor.execute(query_12)
result_12 = cursor.fetchall()
print("This is the Finance major table:")
for tup in result_12:
    print(tup)

print("\n")
query_13 = f"""
SELECT * FROM dbo.PICK_THREE_FIN
"""
cursor.execute(query_13)
result_13 = cursor.fetchall()
print("This is the Pick three finance table:")
for tup in result_13:
    print(tup)

print("\n")
query_14 = f"""
SELECT * FROM dbo.MANAGEMENT_MAJOR
"""
cursor.execute(query_14)
result_14 = cursor.fetchall()
print("This is the Management major table:")
for tup in result_14:
    print(tup)


print("\n")
query_15 = f"""
SELECT * FROM dbo.AOI
"""
cursor.execute(query_15)
result_15 = cursor.fetchall()
print("This is the AOI table:")
for tup in result_15:
    print(tup)









conn.commit()
cursor.close()