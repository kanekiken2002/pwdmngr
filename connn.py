import mysql.connector as con
from datetime import date

today = date.today()

class dfunc: 
  today = date.today()
    
  mydb = con.connect(
    host="localhost",
    user="root",
    password="9560",
    database="lolzies"
  )

  if mydb.is_connected():
    print("Connection established successfully.")

  def add_det(self, uname, pwd, website):
    query = "INSERT INTO pwdtable VALUES (%s, %s, %s, %s);"%(today, uname, pwd, website)
    self.mydb.cursor().execute(query)

  def rem_det(self, column, value):
    query = "DELETE FROM pwdtable WHERE %s = '%s';" %(column, value)
    self.mydb.cursor().execute(query)

  def show_pwd(self, column, value):
    query = "SELECT * FROM pwdtable WHERE %s = '%s';" %(column, value)
    self.mydb.cursor().execute(query)
