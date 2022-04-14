
from unittest import FunctionTestCase
import mysql.connector as mysql
import os
from datetime import datetime
import timeit
from dotenv import load_dotenv
import time

load_dotenv('credentials.env')
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER_PI']
db_pass = os.environ['MYSQL_PASSWORD_PI']
db_name = os.environ['MYSQL_DATABASE']

db = mysql.connect(user=db_user, password=db_pass,
                   host=db_host, database=db_name)

cursor = db.cursor()


cursor.execute("DROP TABLE IF EXISTS objects;")
cursor.execute("""
CREATE TABLE objects (
id      INT AUTO_INCREMENT PRIMARY KEY,
object_name    varchar(32) NOT NULL,
color_range_upper    varchar(64) NOT NULL,
color_range_lower    varchar(64) NOT NULL
);
""")
query = 'INSERT INTO objects (object_name, color_range_upper, color_range_lower) VALUES (%s, %s, %s)'
values = [('Trashcan', '140,255,255', '100,150,0'),
          ('Blues', '140,255,255', '100,150,0'),
          ('Chair', '75,255,255', '25,100,50')
          ]
cursor.executemany(query, values)
db.commit()
