#https://www.red-gate.com/simple-talk/databases/mysql/retrieving-mysql-data-python/

# import the connect method
from mysql.connector import connect
 
# define a connection object
conn = connect(
      user = 'root',
      password = 'SqlPW_py@310!ab',
      host = 'localhost',
      database = 'travel')
 
print('A connection object has been created.')
 
# close the database connection
conn.close()


from mysql.connector import connect, Error
 
# try to run the block of code
try:
 
  # define a connection object
  conn = connect(option_files =
    '/users/mac3/documents/config/connectors.cnf')
 
  # open cursor, define and run query, fetch results
  cursor = conn.cursor()
  query = 'SELECT plane_id, plane, max_weight FROM airplanes'
  cursor.execute(query)
  result = cursor.fetchall()
 
  # print the results in each row
  for r in result:
    print(r)
 
  # close the cursor and database connection
  cursor.close()
  conn.close()
 
# catch exception and print error message
except Error as err:
  print('Error message: ' + err.msg)