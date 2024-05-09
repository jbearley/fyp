# from azuresqlconnector import *
# conn = SQLConnection()
# conn = conn.getConnection()
# cursor = conn.cursor()

# # query = f"""
# # SELECT * FROM dbo.CLASSES;
# # """

# print("\n")
# query_22 = f"""
# SELECT * FROM dbo.PICK_TWO_BLAW_MINOR
# """
# cursor.execute(query_22)
# result_22 = cursor.fetchall()
# print("This is the business law minor pick two table:")
# for tup in result_22:
#     print(tup)
    
# conn.commit()
# cursor.close()

import random

print(random.randrange(0,2))