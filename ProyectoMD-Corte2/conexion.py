#pip install mysql-connector-python
import mysql.connector


try:
    cnx=connection=mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='',
        db='webscraping'
    )
    cur = cnx.cursor()

    if connection.is_connected():
        print("Conexion exitosa") 
except Exception as ex:
    print(ex)