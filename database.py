import mysql.connector

def get_db():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="my-secret-pw",
        database="mydb"
    )
