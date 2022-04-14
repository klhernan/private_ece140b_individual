from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response, FileResponse
import mysql.connector as mysql
from dotenv import load_dotenv
import os
from os.path import join, dirname

geisel_photos = [
   {"id": 1, "img_src": "images/Arizona_47.jpg"},
    {"id": 2, "img_src": "images/Contrast.jpg"},
    {"id": 3, "img_src": "images/Delaware_Plate.png"}
]

dotenv_path = join(dirname(__file__), 'credentials.env')
load_dotenv(dotenv_path)

''' Environment Variables '''
db_host = os.environ.get('MYSQL_HOST')
db_user = os.environ.get('MYSQL_USER')
db_pass = os.environ.get('MYSQL_PASSWORD')
db_name = os.environ.get('MYSQL_DATABASE')

def time_to_string(records):
    days, seconds = records.days, records.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    theTime = f'{hours}:{minutes}:{seconds}'
    return theTime

def get_image_id(req):
    # get the id from the request
    id = req.matchdict['image_id']

    # connect to the database
    db = mysql.connect(host=db_host, user=db_user,
                       passwd=db_pass, database=db_name)
    cursor = db.cursor()

    # query the database with the id
    cursor.execute(
        "SELECT id,name,value,created_at FROM licensePlate WHERE id='%s';" % id)
    record = cursor.fetchone()
    db.close()
    print("id is : ",  id)
    # if no record found, return error json
    if record is None:
        return {
            'error': "No data was found for the given ID",
            'id': "",
            'name': "",
            'value': "",
            'created_at': ""
        }
    print("reponse is: ", record)
    print("the time is:", record[3])
    print("the image name is: ",geisel_photos[record[0]-1].get('img_src'))
    # populate json with values
    response = {
        'name':         geisel_photos[record[0]-1].get('img_src'),
        'value':  record[2],
        'created_at':        time_to_string(record[3])
    }
    print(record[2], time_to_string(record[3]))
    return response



def index_page(req):
    return FileResponse("index.html")

if __name__ == '__main__':
    with Configurator() as config:
        
        config.add_route('imageIds', '/imageIds/{image_id}')
        config.add_view(get_image_id, route_name='imageIds', renderer='json')
        config.add_route('home', '/')
        config.add_view(index_page, route_name='home')
        config.add_static_view(name='/', path='./public', cache_max_age=3600)
        app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()

def get_home(req):
    return FileResponse("index.html")
