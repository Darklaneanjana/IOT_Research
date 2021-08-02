import mysql.connector

mydb = mysql.connector.connect(
  host="remotemysql.com",
  user="WsuipEe2II",
  password="WL0WXtXAdL",
  database="WsuipEe2II"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM shop")


myresult = mycursor.fetchall()

for x in myresult:
  print(x)