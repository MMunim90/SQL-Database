import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)

print(mydb)

db_name = "python_db"
mycursor = mydb.cursor()
query = "CREATE DATABASE " + db_name
mycursor.execute(query)