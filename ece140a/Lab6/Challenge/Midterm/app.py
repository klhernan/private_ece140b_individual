from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response, FileResponse
import mysql.connector as mysql
from dotenv import load_dotenv
import os
from os.path import join, dirname
import RPi.GPIO as GPIO
from flask import Flask, jsonify
ledPin = 40 
def setup():
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(ledPin, GPIO.OUT) 
    GPIO.output(ledPin, GPIO.LOW) 
def destroy():
    GPIO.cleanup() 

dotenv_path = join(dirname(__file__), 'credentialsUsr.env')
load_dotenv(dotenv_path)

''' Environment Variables '''
db_host = os.environ.get('MYSQL_HOST')
db_user = os.environ.get('MYSQL_USER')
db_pass = os.environ.get('MYSQL_PASSWORD')
db_name = os.environ.get('MYSQL_DATABASE')

def time_to_string(records):
    days, seconds = records[3].days, records[3].seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    theTime = f'{hours}:{minutes}:{seconds}'
    return theTime

def get_sensor_data(req):
    """ Returns an image and author from the DB based on height and/or age arguments. """
    distance = req.matchdict['distance']
    xAxis = req.matchdict['xAxis']
    yAxis = req.matchdict['yAxis']
    #we have a pre recorded table
    db = mysql.connect(host=db_host, user=db_user,
                       passwd=db_pass, database=db_name)
    cursor = db.cursor()

    # set min and max ranges
    if distance != 'None':
        [min_distance, max_distance] = distance.split('-')
    if xAxis != 'None':
        [min_xAxis, max_xAxis] = xAxis.split('-')
    if yAxis != 'None':
        [min_yAxis, max_yAxis] = yAxis.split('-')

    # conditional search based on value for age and height
    #since there can be none values the query won't respond well so we need to create various cases for each combination of input values
    if distance == 'None' and (xAxis != 'None' and yAxis != 'None'):
        cursor.execute(
            "SELECT distance,xAxis,yAxis,created_at FROM PiSensors WHERE ((xAxis BETWEEN %s AND %s) AND (yAxis BETWEEN %s AND %s));", (min_xAxis, max_xAxis, min_yAxis, max_yAxis))
    elif xAxis == 'None' and yAxis == 'None':
        cursor.execute(
            "SELECT distance,xAxis,yAxis,created_at FROM PiSensors WHERE (distance BETWEEN %s AND %s);", (min_distance, max_distance))
    elif distance == 'None' and yAxis == 'None':
        cursor.execute(
            "SELECT distance,xAxis,yAxis,created_at FROM PiSensors WHERE (xAxis BETWEEN %s AND %s);", (min_xAxis, max_xAxis))
    elif xAxis == 'None' and distance == 'None':
        cursor.execute(
            "SELECT distance,xAxis,yAxis,created_at FROM PiSensors WHERE (yAxis BETWEEN %s AND %s);", (min_yAxis, max_yAxis))
    elif xAxis == 'None' and (distance != 'None' and yAxis != 'None'):
        cursor.execute(
            "SELECT distance,xAxis,yAxis,created_at FROM PiSensors WHERE ((distance BETWEEN %s AND %s) AND (yAxis BETWEEN %s AND %s));", (min_distance, max_distance, min_yAxis, max_yAxis))
    elif yAxis == 'None' and (distance != 'None' and xAxis != 'None'):
        cursor.execute(
            "SELECT distance,xAxis,yAxis,created_at FROM PiSensors WHERE ((distance BETWEEN %s AND %s) AND (xAxis BETWEEN %s AND %s));", (min_distance, max_distance, min_xAxis, max_xAxis))
    elif yAxis == 'None' and xAxis == 'None' and distance == 'None':
        return {
            'error': "No data was found for the given ID",
            'distance': "",
            'xAxis': "",
            'yAxis': "",
            
        }
    else:
        cursor.execute(
            "SELECT distance,xAxis,yAxis,created_at FROM PiSensors WHERE ((distance BETWEEN %s AND %s) AND (xAxis BETWEEN %s AND %s) AND (yAxis BETWEEN %s AND %s));", (min_distance, max_distance, min_xAxis, max_xAxis, min_yAxis, max_yAxis))
    records = cursor.fetchall()
    db.close()

    print(type(records[1]))
    if not records:
        return {
            'error': "No data was found for the given ID",
            'distance': "",
            'xAxis': "",
            'yAxis': "",
            'created_at':""
        }
    allData = []
    #place query list of tuppels in list of dictionaries
    for row in records:
        data= {"distance":row[0], "xAxis":row[1], "yAxis Name":row[2], "created_at":time_to_string(row)}
        allData.append(data)

    return allData


  


def get_led(req):
    #hanlds LED light with GPIO library
    ledState = req.matchdict['ledSwitch']
    print(ledState)
    if ledState == "ON":
        print("led is on")
        GPIO.output(ledPin, GPIO.HIGH)
        return {
            "switch" : "OFF"
        }
    else:
        print("led is off")
        GPIO.output(ledPin, GPIO.LOW)
        return {
            "switch" : "ON"
        }
def index_page(req):
    return FileResponse("index.html")


if __name__ == '__main__':
    with Configurator() as config:
        setup()
        config.add_route('home', '/')
        config.add_view(index_page, route_name='home')
        config.add_route('ranges', '/ranges/{distance}/{xAxis}/{yAxis}/{created_at}')
        config.add_view(get_sensor_data, route_name='ranges', renderer='json')
        config.add_route('ledswitch', 'ledswitch/{ledSwitch}')
        config.add_view(get_led, route_name= 'ledswitch', renderer='json')
        config.add_static_view(name='/', path='./public', cache_max_age=3600)
        app = config.make_wsgi_app()
server = make_server('0.0.0.0', 6542, app)
server.serve_forever()
if KeyboardInterrupt:
    GPIO.output(ledPin, GPIO.LOW)
    destroy()
