import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import numpy as np
import cv2
import time

def read_bounds(strIn):
    list = []
    vals = str(strIn)
    vals = vals.split(',')
    for val in vals:
        list.append(int(val)) 

    return np.array(list)

# lower = read_bounds(lowerStr)
# upper = read_bounds(upperStr)
# print(lower.shape)

def PID_fn(lowerStr, upperStr):
    """
    ---------------------------------------------------------
    """
    #video capture likely to be 0 or 1
    cap=cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    #Stepper Motor Setup
    GpioPins = [18, 23, 24, 25]

    # Declare a named instance of class pass a name and motor type
    mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")
    #min time between motor steps (ie max speed)
    step_time = .002

    #PID Gain Values (these are just starter values)
    Kp = 0.003
    Kd = 0.0001
    Ki = 0.0001

    #error values
    d_error = 0
    last_error = 0
    sum_error = 0
    while(1):
        _,frame=cap.read()

        #convert to hsv deals better with lighting
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        #masks input image with upper and lower red ranges

        lower = read_bounds(lowerStr)
        upper = read_bounds(upperStr)

        color_only = cv2.inRange(hsv, lower, upper)
    
        mask=np.ones((5,5),np.uint8)
        
        #run an opening to get rid of any noise
        opening=cv2.morphologyEx(color_only,cv2.MORPH_OPEN,mask)
        # cv2.imshow('Masked image', opening)

        #run connected components algo to return all objects it sees.        
        num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(opening,4, cv2.CV_32S)
        b=np.matrix(labels)
        if num_labels > 1:
            start = time.time()
            #extracts the label of the largest none background component and displays distance from center and image.
            max_label, max_size = max([(i, stats[i, cv2.CC_STAT_AREA]) for i in range(1, num_labels)], key = lambda x: x[1])
            Obj = b == max_label
            Obj = np.uint8(Obj)
            Obj[Obj > 0] = 255
            # cv2.imshow('largest object', Obj)
            
            #calculate error from center column of masked image
            error = -1 * (320 - centroids[max_label][0])
            #speed gain calculated from PID gain values
            speed = Kp * error + Ki * sum_error + Kd * d_error
            
            #if negative speed change direction
            if speed < 0:
                direction = False
            else:
                direction = True
            
            #inverse speed set for multiplying step time (lower step time = faster speed)
            speed_inv = abs(1/(speed))
            
            #get delta time between loops
            delta_t = time.time() - start
            #calculate derivative error
            d_error = (error - last_error)/delta_t
            #integrated error
            sum_error += (error * delta_t)
            last_error = error
            
            #buffer of 20 only runs within 20
            if abs(error) > 20:
                mymotortest.motor_run(GpioPins , speed_inv * step_time, 1, direction, False, "full", .05)
            else:
                #run 0 steps if within an error of 20
                mymotortest.motor_run(GpioPins , step_time, 0, direction, False, "full", .05)
            
        else:
            print('no object in view')
            

        # k=cv2.waitKey(5)
        # if k==27:
        #     break

    cv2.destroyAllWindows()
    GPIO.cleanup()

"""
GPS Section
---------------------------------------------------------
# """
# def GPS():