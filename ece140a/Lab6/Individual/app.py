from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response, FileResponse

# This is used to render response through a JSON to the front-end
from pyramid.renderers import render_to_response

import mysql.connector as mysql
import os
from dotenv import load_dotenv

# Environment variables
dotenv_path = join(dirname(__file__), 'credentials.env')
# dotenv_path = 'credentialsUsr.env'

load_dotenv(dotenv_path)
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']


def get_sensor_readings(req):

    dist = req.matchdict['distance']
    xAx = req.matchdict['xAxis']
    yAx = req.matchdict['yAxis']

    db = mysql.connect(host=db_host, database=db_name, 
                        user=db_user, passwd=db_pass)

    cursor = db.cursor()

    # query the database with the id
    cursor.execute("select * from students where id='%s';" % the_id)


    cursor.execute(
        "SELECT id,name,designation,email FROM TeachingStaff WHERE id='%s';" % id)
    record = cursor.fetchone()
    db.close()

    # if no record found, return error json
    if record is None:
        return {
            'error': "No data was found for the given ID",
            'id': "",
            'name': "",
            'designation': "",
            'email': ""
        }

    # populate json with values
    response = {
        'id':           record[0],
        'name':         record[1],
        'designation':  record[2],
        'email':        record[3]
    }

    return response


load_dotenv('credentials.env')

''' Environment Variables '''
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']


def get_home(req):
    return FileResponse("index.html")


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('get_staff_member', '/staff/{staff_id}')
        config.add_view(get_staff_member,
                        route_name='get_staff_member', renderer='json')
        config.add_route('home', '/')
        config.add_view(get_home, route_name='home')
        config.add_static_view(name='/', path='./public', cache_max_age=3600)

        app = config.make_wsgi_app()

server = make_server('0.0.0.0', 6543, app)
print('Web server started on: http://0.0.0.0:6543')
server.serve_forever()
