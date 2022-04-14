import mysql.connector as mysql
import os
from dotenv import load_dotenv  

load_dotenv('credentialsRoot.env')  

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

cursor.execute("CREATE DATABASE IF NOT EXISTS Lab6;")

try:
    cursor.execute("""
    GRANT ALL PRIVILEGES ON Lab6.* TO 'sepehrpi'@'127.0.0.1';
  """)
except RuntimeError as err:
    print("runtime error: {0}".format(err))


cursor.execute("USE Lab6")

cursor.execute("DROP TABLE IF EXISTS PiSensors;")
cursor.execute("""
    CREATE TABLE PiSensors (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    distance    DOUBLE(8,2) NOT NULL,
    xAxis       INT NOT NULL,
    yAxis       INT NOT NULL,
    created_at  TIME
    );
""")

db.commit()

