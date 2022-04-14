import mysql.connector as mysql
import os
from dotenv import load_dotenv

load_dotenv('credentials.env')

''' Environment Variables '''
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']

db = mysql.connect(
    host=db_host,
    user=db_user,
    password=db_pass,
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS Lab8;")

try:
    cursor.execute("""
    GRANT ALL PRIVILEGES ON Lab8.* TO 'sepehrpi'@'127.0.0.1';
  """)
except RuntimeError as err:
    print("runtime error: {0}".format(err))


cursor.execute("USE Lab8")

cursor.execute("DROP TABLE IF EXISTS objects;")
cursor.execute("""
    CREATE TABLE objects (
    id      INT AUTO_INCREMENT PRIMARY KEY,
    object_name    varchar(32) NOT NULL,
    color_range_upper    varchar(64) NOT NULL,
    color_range_lower    varchar(64) NOT NULL
    );
""")

cursor.execute("DROP TABLE IF EXISTS found_objects;")
cursor.execute("""
    CREATE TABLE found_objects (
    id      INT AUTO_INCREMENT PRIMARY KEY,
    object_name    varchar(32) NOT NULL,
    object_name_value INT NOT NULL,
    address    varchar(255) NOT NULL
    );
""")

db.commit()
