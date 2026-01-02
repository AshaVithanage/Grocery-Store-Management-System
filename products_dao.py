import mysql.connector

cnx = mysql.connector.connect(user='root', password='Asha@8141',
                              host='127.0.0.1',
                              database='grocery_store')

cursor = cnx.cursor()

cursor.execute(query)

cnx.close()