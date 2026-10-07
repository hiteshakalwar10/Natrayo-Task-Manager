import mysql.connector


def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="#sqlpass1010",
        database="natrayo_db"
    )

    return connection

if __name__ == "__main__":
    connection = get_connection()
    print("MySQL connection successful!")
    connection.close()
