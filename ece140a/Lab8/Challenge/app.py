from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response, FileResponse
import mysql.connector as mysql
from dotenv import load_dotenv
import os
from os.path import join, dirname
from challenge import *

# from challenge.py import *

dotenv_path = join(dirname(__file__), 'credentials.env')
load_dotenv(dotenv_path)

''' Environment Variables '''
db_host = os.environ.get('MYSQL_HOST')
db_user = os.environ.get('MYSQL_USER')
db_pass = os.environ.get('MYSQL_PASSWORD')
db_name = os.environ.get('MYSQL_DATABASE')

def get_object_name(req):
    # get the id from the request
    name = req.matchdict['object_name']
    print("name is : ",name)
    # connect to the database
    db = mysql.connect(host=db_host, user=db_user,
                       passwd=db_pass, database=db_name)
    cursor = db.cursor()
    cursor.execute(
        "SELECT id,color_range_upper,color_range_lower FROM objects WHERE object_name='%s';" %name)
    record = cursor.fetchone()

    obejctNameValue = 1
    # call function give them the color range(record[1], record[2])
    # the camera using PID and stepper looks for the object horizontally
    # once found we get object location using gps
    # we place the gps location and with the object name in to the table
    PID_fn(record[2], record[1])

    cursor.execute("SELECT * FROM found_objects WHERE object_name='%s';" % name)
    record = cursor.fetchall()
    if record is not None:
        obejctNameValue = obejctNameValue + 1
    #values = [name, obejctNameValue, gpslocation]

    query = "INSERT INTO found_objects (object_name, object_name_value) VALUES (%s, %s)"
    values = [name, obejctNameValue]
    cursor.executeone(query, values)
    # query the database with the id
    cursor.execute(
        "SELECT * FROM found_objects WHERE object_name='%s';" % name)
    record = cursor.fetchall()
    db.close()
    # if no record found, return error json
    if record is None:
        print("its empty")
    print("reponse is: ", record)



def index_page(req):
    return FileResponse("index.html")


if __name__ == '__main__':
    with Configurator() as config:

        config.add_route('objectName', '/objectName/{object_name}')
        config.add_view(get_object_name,
                        route_name='objectName', renderer='json')
        config.add_route('home', '/')
        config.add_view(index_page, route_name='home')
        config.add_static_view(name='/', path='./public', cache_max_age=3600)
        app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()


def get_home(req):
    return FileResponse("index.html")
