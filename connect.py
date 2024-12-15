# import MYSQL
import mysql.connector

# make connection
conn = mysql.connector.connect(host="localhost",
                               user = "root",
                               password = "Pause80lie!",
                               auth_plugin = "mysql_native_password")

# create cursor object
cur_obj = conn.cursor()

# create database schema
cur_obj.execute("CREATE SCHEMA FastFood;")

# confirm execution worked by printing result
cur_obj.execute("SHOW DATABASES;")
for row in cur_obj:
    print(row)

# print out connectoin to verify and close
print(conn)
conn.close()