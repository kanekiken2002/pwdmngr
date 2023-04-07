import mysql.connector as con
from datetime import date
today = date.today()

mydb = con.connect(
  host="localhost",
  user="root",
  password="9560",
  database="lolzies"
)

cursor = mydb.cursor

if mydb.is_connected():
  print("Connection established successfully.")

def add_det(uname, pwd, website):
  query = "INSERT INTO pwdtable VALUES (%s, %s, %s, %s);"%(today, uname, pwd, website)
  cursor.execute(query)

def rem_det(column, value):
  query = "DELETE FROM pwdtable WHERE %s = '%s';" %(column, value)
  cursor.execute(query)

def show_pwd(column, value):
  query = "SELECT * FROM pwdtable WHERE %s = '%s';" %(column, value)
  cursor.execute(query)
