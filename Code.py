import sqlite3 as db 


def init():
  '''
  Inititalize a new database to store the 
  expedenitures 
  '''
  connect = db.connect("spent.db") 
  cur = conn.cursor()
  sql = '''
  create table if not exists expenses (
  amount number, 
  category string, 
  date string
  )
  '''
  cur.execute(sql)
  conn.commit()
init()
