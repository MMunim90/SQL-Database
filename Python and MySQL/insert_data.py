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
        INSERT INTO Student(Roll, Name)
        VALUES(101, 'MMunim'),
        (102, 'Rahim'),
        (103, 'Karim')
        """

mycursor.execute(query)
mydb.commit()
print("Data inserted successfully!")