import mysql.connector as mydb


def get_connection():
    connection = mydb.connect(host="localhost",
                          port=3306,
                          user="root",
                          password="password",
                          database="sakila")
    print("Is connection not none ", connection)
    return connection


def close_connection(connection):
    if connection is not None:
        connection.close()
    print("Connection is closed")
