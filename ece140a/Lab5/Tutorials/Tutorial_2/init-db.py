from tabnanny import verbose
import mysql.connector as mysql # Allows us to run SQL commands in Python
import os                       # Used to import environment data
# import dote
from dotenv import load_dotenv  # Used to load data from .env file

import os
os.getenv("ACCESS_KEY")
# Loads all details from the "credentials.env"
load_dotenv('credentials.env', verbose=True) 

''' Environment Variables '''
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
# db_host = os.environ['localhost']
# db_user = os.environ['root']
# db_pass = os.environ['Hdzmkl1!Sql']

# Now we can connect to the server
db = mysql.connect(
  host= db_host,
  user=db_user,
  password=db_pass,
)

# Generate a cursor for accesing mysql 
cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS Lab5;")
cursor.execute("USE Lab5")

# CREATE TABLE
cursor.execute(
    """CREATE TABLE students(
    id integer NOT NULL AUTO_INCREMENT primary key,
    name varchar(32),
    email varchar(32),
    password varchar(32),
    age int,
    created_at  TIMESTAMP
    );
""")

cursor.execute("SHOW TABLES")
my_result = cursor.fetchall()
for x in my_result:
  print(x)

#INSERT VALUES
query = 'INSERT INTO students (name, email, password, age, created_at) VALUES (%s, %s, %s, %s, %s)'
values = [('Bart', 'bart@fox.com', 'bartman', '10',  '2022-02-11 12:36:09'),
         ('Lisa', 'lisa@fox.com', 'vegan', '8',  '2022-02-01 04:23:00'),
         ('Mona', 'mona@vox.com', 'Start#*up', '78', '2022-02-01 04:41:00')
         ]
cursor.executemany(query,values)
db.commit()

print('---INSERT---')
print(cursor.rowcount, "record(s) inserted")

# BASIC SELECT
cursor.execute('SELECT * from students ORDER BY age;')
my_result = cursor.fetchall()
print('---SELECT---')
[print(x) for x in my_result]
 
# BASIC UPDATE
sql = "UPDATE students SET age = 39 WHERE name = 'Bart';"
cursor.execute(sql)
print(cursor.rowcount, "record(s) affected")
db.commit()
result = cursor.fetchall()
print('---SELECT---')
[print(x) for x in result]
