from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response, FileResponse

# This is used to render response through a JSON to the front-end
from pyramid.renderers import render_to_response

import mysql.connector as mysql
import os
from dotenv import load_dotenv
import json
# The python file that manages RasberryPi & Hardware components
from sensorCom import *

"""
------------------------------------------------------------------------
GOAL
------------------------------------------------------------------------
REST-server app file, to render databases directly 

1. /sensor : displays a list of the sensor readings given a filtering criteria, 
             using route and view functions w/names 
            - "get_ultrasonic" and "get_ultrasonic()"
            - "get_joystick" and "get_joystick()"

2. /sensor/{reading_range} : returns a JSON with the sensor readings given a filtering      
                            criteria, using route and view functions w/names 
                            - "get_ultrasonic" and "get_ultrasonic()"
                            - "get_joystick" and "get_joystick()"

"""


# Environment variables
# dotenv_path = os.path.join(os.path.dirname(__file__), 'credentials.env')

# dotenv_path = 'credentialsUsr.env'
# load_dotenv(dotenv_path)
# load_dotenv()

# db_host = os.environ['MYSQL_HOST']
# db_user = os.environ['MYSQL_USER']
# db_pass = os.environ['MYSQL_PASSWORD']
# db_name = os.environ['MYSQL_DATABASE']

# db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
# cursor = db.cursor()
 
# cursor.execute("DROP TABLE IF EXISTS PiSensors;")

# try:
#     cursor.execute("""
#         CREATE TABLE PiSensors (
#         id          INT AUTO_INCREMENT PRIMARY KEY,
#         distance    DECIMAL(100,2) NOT NULL,
#         xAngle       INT NOT NULL,
#         yAngle       INT NOT NULL,
#         created_at  TIMESTAMP
#         );
#     """)

# except RuntimeError as err:
#     print("runtime error: {0}".format(err))


# def get_ultrasonic(req):
#     """
#     1. Ultrasonic sensor :  Readings will be return/displayed by options from 
#     - Min: 0-254
#     - Max: 1-255 
#     """

#     dist = req.matchdict['distance']
#     xAx = req.matchdict['xAxis']
#     yAx = req.matchdict['yAxis' 

#     db = mysql.connect(host=db_host, database=db_name, 
#                         user=db_user, passwd=db_pass)

#     cursor = db.cursor()


#     # query the database with the id
#     cursor.execute("select * from students where id='%s';" % the_id)

    
#     cursor.execute(
#         "SELECT id,name,designation,email FROM TeachingStaff WHERE id='%s';" % id)
#     record = cursor.fetchone()
#     db.close()

#     # if no record found, return error json
#     if record is None:
#         return {
#             'error': "No data was found for the given ID",
#             'id': "",
#             'name': "",
#             'designation': "",
#             'email': ""
#         }

#     # populate json with values
#     response = {
#         'id':           record[0],
#         'name':         record[1],
#         'designation':  record[2],
#         'email':        record[3]
#     }

#     return response


# def get_joystick(req):
#     """
#     Joystick sensor :  Readings will be return/displayed by options from drop down menu
#     Filter ranges from drop down menu: (measurements between 0-255)
#     - None
#     - 0:0 (first quadrant diagional 45degrees)
#     - 51:102
#     - 102:153
#     - 153:204
#     - 204:255

#     """


''' Route Configurations '''
if __name__ == '__main__':

  with Configurator() as config:
        
    # Create a route called home
    config.add_route('home', '/')

    # Bind the view (defined by index_page) to the route named ‘home’
    config.add_view(index_page, route_name='home')

    # to use Jinja2 to render the template! 
    config.include('pyramid_jinja2')
    config.add_jinja2_renderer('.html')

    config.add_route('get_ledStatus', '/sensorReadings')
    config.add_view(get_ledStatus, route_name='get_ledStatus', renderer='json')

    config.add_route('get_readings_table', '/sensorReadings')
    config.add_view(get_readings_table, route_name='get_readings_table', renderer='json')

    config.add_route('get_readings_json', '/sensorReadings/{ranges}')
    config.add_view(get_readings_json, route_name='get_readings_json', renderer='json')

    # For our static assets!
    config.add_static_view(name='/', path='./public', cache_max_age=3600)

    app = config.make_wsgi_app()

server = make_server('0.0.0.0', 6543, app)
print('Web server started on: http://0.0.0.0:6543')
server.serve_forever()



def index_page(req):
    return FileResponse("index.html")

def get_ledStatus(req): {
    if 
    ledOn()
}


def get_readings_table(req):

    #get the id from the request
    # dist_id = req.matchdict['distance']
    # x_id = req.matchdict['xAngle']
    # y_id = req.matchdict['yAngle']

    min_distance = req.matchdict['min_dist']
    max_distance = req.matchdict['max_dist']
    max_xAxis = req.matchdict['joy_max_x']
    min_yAxis = req.matchdict['joy_min_x']
    max_yAxis = req.matchdict['joy_max_y']
    min_xAxis = req.matchdict['joy_min_y']

    #connect to the database
    db = mysql.connect(host=db_host, user=db_user, passwd=db_pass, database=db_name)
    # cursor = db.cursor()
    cursor = db.cursor(dictionary=True)

    #query the database with the id
    select_query = "select * from PiSensors where distance between = %s and %s or xAngle between = %s and %s or yAngle between = %s and %s or"
                    # > then self.cursor.execute(sql, (min_distance, max_distance, 
                    # max_xAxis, min_yAxis, max_yAxis, min_xAxis))

    cursor.execute(select_query, (min_distance, max_distance, max_xAxis, min_yAxis, max_yAxis, min_xAxis))
    
    #if no record found, return error json
    if sensorReadings is None:
        return {
            'error' : "No data was found for the given ID",
            'id': "",
            'distance' : "",
            'xAngle': "",
            'yAngle': ""
        }
        db.close()

    row_headers=[r[0] for r in cursor.description] 
    sensorReadings = cursor.fetchall()
    jsonResponse = []
    for result in sensorReadings:
        jsonResponse.append(dict(zip(row_headers,result)))

    db.close()

    data = {"sensorReadings": jsonResponse, "page_name": "Sensor Ranges"}
    return render_to_response('index.html', data, request=req)



def get_readings_json(req):
    # #get the id from the request
    # dist_id = req.matchdict['distance']
    # x_id = req.matchdict['xAngle']
    # y_id = req.matchdict['yAngle']

    # #connect to the database
    # db = mysql.connect(host=db_host, user=db_user, passwd=db_pass, database=db_name)
    # # cursor = db.cursor()
    # cursor = db.cursor(dictionary=True)

    # #query the database with the id
    # select_query = "SELECT id, name,designation,email FROM TeachingStaff WHERE id='%s';"

    # cursor.execute(select_query %id)
    min_distance = req.matchdict['min_dist']
    max_distance = req.matchdict['max_dist']
    max_xAxis = req.matchdict['joy_max_x']
    min_yAxis = req.matchdict['joy_min_x']
    max_yAxis = req.matchdict['joy_max_y']
    min_xAxis = req.matchdict['joy_min_y']

    #connect to the database
    db = mysql.connect(host=db_host, user=db_user, passwd=db_pass, database=db_name)
    # cursor = db.cursor()
    cursor = db.cursor(dictionary=True)

    #query the database with the id
    select_query = "select * from PiSensors where distance between = %s and %s or xAngle between = %s and %s or yAngle between = %s and %s or"
                    # > then self.cursor.execute(sql, (min_distance, max_distance, 
                    # max_xAxis, min_yAxis, max_yAxis, min_xAxis))

    cursor.execute(select_query, (min_distance, max_distance, max_xAxis, min_yAxis, max_yAxis, min_xAxis))
    
    #if no record found, return error json
    if sensorReadings is None:
        return {
            'error' : "No data was found for the given ID",
            'id': "",
            'distance' : "",
            'xAngle': "",
            'yAngle': ""
        }
        db.close()


    row_headers=[r[0] for r in cursor.description] 
    sensorReadings = cursor.fetchall() 
    jsonResponse = []
    for result in sensorReadings:
        jsonResponse.append(dict(zip(row_headers,result)))

    db.close()
    return json.dumps(jsonResponse)
