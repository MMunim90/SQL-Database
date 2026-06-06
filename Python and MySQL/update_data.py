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
        UPDATE Student
        SET Name = 'Hamid'
        WHERE Name = 'Karim'
        """

mycursor.execute(query)
mydb.commit()
print("Data updated successfully!")