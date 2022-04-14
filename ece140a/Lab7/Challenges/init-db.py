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

cursor.execute("CREATE DATABASE IF NOT EXISTS Lab7;")

try:
    cursor.execute("""
    GRANT ALL PRIVILEGES ON Lab7.* TO 'sepehrpi'@'127.0.0.1';
  """)
except RuntimeError as err:
    print("runtime error: {0}".format(err))


cursor.execute("USE Lab7")

cursor.execute("DROP TABLE IF EXISTS licensePlate;")
cursor.execute("""
    CREATE TABLE licensePlate (
    id      INT AUTO_INCREMENT PRIMARY KEY,
    name    varchar(32) NOT NULL,
    value  varchar(10) NOT NULL,
    created_at  TIME
    );
""")

db.commit()

