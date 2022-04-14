from unittest import FunctionTestCase
import mysql.connector as mysql
import os
from datetime import datetime
import timeit
from dotenv import load_dotenv  # only required if using dotenv for creds

from sensorCom import *


load_dotenv('credentialsUsr.env')
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']

db = mysql.connect(user=db_user, password=db_pass,
                   host=db_host, database=db_name)

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS PiSensors;")


try:
    cursor.execute("""
    CREATE TABLE PiSensors (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    distance    DOUBLE(8,2) NOT NULL,
    xAxis       INT NOT NULL,
    yAxis       INT NOT NULL,
    created_at  TIME
    );
  """)
  
except RuntimeError as err:
    print("runtime error: {0}".format(err))

# Server starts -> setup + timer begins
# ----------------------------
# Set up server
# ----------------------------


print('Program is starting...')
setup()

# time_count = time.clock
try: 
  while(True):
      query = "INSERT INTO PiSensors (distance, xAxis, yAxis, created_at) VALUES (%s, %s, %s, %s)"
      now = datetime.now()
      current_time = now.strftime("%H:%M:%S")
      values = [getSonar(), joystick(0), joystick(1), current_time]
      print(values)
      cursor.execute(query, values)
      time.sleep(1) 
except KeyboardInterrupt:
  GPIO.cleanup()
  db.commit()

#db.commit()