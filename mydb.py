import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Welcome1234'
)


# Prepare a cursor object

cursorObject = dataBase.cursor()


#create database

cursorObject.execute("CREATE DATABASE zootime")

print("All Done!")