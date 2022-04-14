import mysql.connector as mysql
import os
from dotenv import load_dotenv  

load_dotenv('credentialsRoot.env')  

''' Environment Variables '''
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']

db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS Lab6;")
cursor.execute("USE Lab6")

try:
    cursor.execute(
    """
    GRANT ALL PRIVILEGES ON Lab6.* TO 'sepehrpi'@'127.0.0.1';
    """
    )
except RuntimeError as err:
    print("runtime error: {0}".format(err))

db.commit()

cursor.execute("DROP TABLE IF EXISTS PiSensors;")

try:
    cursor.execute("""
        CREATE TABLE PiSensors (
        id          INT AUTO_INCREMENT PRIMARY KEY,
        distance    DECIMAL(100,2) NOT NULL,
        xAngle       INT NOT NULL,
        yAngle       INT NOT NULL,
        created_at  TIMESTAMP
        );
    """)
except RuntimeError as err:
    print("runtime error: {0}".format(err))

