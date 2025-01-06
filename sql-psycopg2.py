import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of database
cursor = connection.cursor()


cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# fetch the results (multiple)
results = cursor.fetchall()

# close the connection
connection.close()

# print the results
for result in results:
    print(result)



