# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python 

import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = '0022'
	)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE Profile")

print("All Done!")
