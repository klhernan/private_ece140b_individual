from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

# This is used to render response through a JSON to the front-end
from pyramid.renderers import render_to_response

import mysql.connector as mysql
import os
from dotenv import load_dotenv


# --------------------------------------
# Rendering Data as JSON
# --------------------------------------

    ''' Instance Route to GET Student '''
def get_student(req):
    # Retrieve the route argument (this is not GET/POST data!)
    the_id = req.matchdict['student_id']

    # Connect to the database and retrieve the student
    db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
    cursor = db.cursor()
    cursor.execute("select * from students where id='%s';" % the_id)
    record = cursor.fetchone()
    db.close()
    if record is None:
        return ""

    # Format the result as key-value pairs
    response = {
        'id':     	record[0],
        'name':   	record[1],
        'email':  	record[2],
        'password':   record[3],
        'age':    	record[4],
        'datetime':   record[5].isoformat()
    }
    return response

    # Original function from video tutorial 

    response = {}
    for index, row in enumerate(record):
        response[index] = {
            "id": row[0],
            "first_name": row[1],
            "last_name": row[2], 
            "email": row[3],
            "age": row[2]
           }

    return response


# ----------------------------------------
# Rendering Data on the Web Page Directly
# ----------------------------------------

''' Collection Route to GET Students '''
def get_students(req):
    db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
    cursor = db.cursor()
    cursor.execute("select id, name, email, password, age from students;")
    records = cursor.fetchall()
    db.close()

    data = {"students": records, "page_name": "Student Roster"}
    return render_to_response('index.html', data, request=req)




''' Route Configurations '''
if __name__ == '__main__':

    with Configurator() as config:

        # to use Jinja2 to render the template! 
        config.include('pyramid_jinja2')
        config.add_jinja2_renderer('.html')

        # Data retrival only, for adding a page the FN would be defined and render to that page
        config.add_route('get_students', '/students')
        config.add_view(get_students, route_name='get_students', renderer='json')

        config.add_route('get_student', '/student/{student_id}')
        config.add_view(get_student, route_name='get_student', renderer='json')

        # For our static assets!
        config.add_static_view(name='/', path='./public', cache_max_age=3600)

        app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 6543, app)
    print('Web server started on: http://0.0.0.0:6543')
    server.serve_forever()


