import sqlite3

def dict_factory(cursor, row):
  d = {}
  for idx, col in enumerate(cursor.description):
    d[col[0]] = row[idx]
  return d

connection = sqlite3.connect("./data/exported/db.sqlite")
connection.row_factory = dict_factory

cursor = connection.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
for table_name in tables:
  print(table_name['name'])
  
  conn = sqlite3.connect("./data/exported/db.sqlite")
  conn.row_factory = dict_factory
  
  cur1 = conn.cursor()
  
  cur1.execute("SELECT * FROM " + table_name['name'])
  
  results = cur1.fetchall()
  
  with open(table_name['name'] + '.json', 'a') as the_file:
    the_file.write(format(results).replace(" u'", "'").replace("'", "\""))

connection.close()
