
from unittest import FunctionTestCase
import mysql.connector as mysql
import os
from datetime import datetime
import timeit
from dotenv import load_dotenv 
from detector import *
import time

load_dotenv('credentials.env')
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER_PI']
db_pass = os.environ['MYSQL_PASSWORD_PI']
db_name = os.environ['MYSQL_DATABASE']

db = mysql.connect(user=db_user, password=db_pass,
                   host=db_host, database=db_name)

cursor = db.cursor()

try:
    cursor.execute("DROP TABLE IF EXISTS licensePlate;")
    cursor.execute("""
        CREATE TABLE licensePlate (
        id      INT AUTO_INCREMENT PRIMARY KEY,
        name    varchar(32) NOT NULL,
        value  varchar(10) NOT NULL,
        created_at  time
        );
""")
except RuntimeError as err:
    print("runtime error: {0}".format(err))
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
for i in range(3):
    query = "INSERT INTO licensePlate (name, value, created_at) VALUES (%s, %s, %s)"
    values = [(giveFilename(i),getImagetoText(i), current_time)]
    cursor.executemany(query, values)
    db.commit()
    time.sleep(1) 
    i += 1 