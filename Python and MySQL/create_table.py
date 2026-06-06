import mysql.connector

db_name = "python_db"

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = db_name
)

mycursor = mydb.cursor()
query = """
        CREATE TABLE Student
        (
            Roll INT PRIMARY KEY,
            Name VARCHAR(50)
        )
        """

mycursor.execute(query)