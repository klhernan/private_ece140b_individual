# ECE 140A - Lab 8

- **Winter 2022**

- ** March 17th, 2022**

## Partners

- **Karen Hernandez**

  - A16118872

- **Sepehr Bostan**
  - A16062097

# Tutorials

!['Test image'](Tutorials/Tutorial_1/test.jpg)

## Tutorial 1 - Introduction to CAD

Using the knowledge from ECE 5, we designed a mount for the camera. The measurements were given to us. This will be used to connect the camera to the stepper motor.

### Our design

The design was done in SolidWorks. Our final design is as follows:

**Top view**
!['Camera Mount CAD '](Images/Tutorials/cad-top-view.jpg)

**Isometric view**
!['Camera Mount CAD '](Images/Tutorials/cad-iso-view.jpg)

**Side view**
!['Camera Mount CAD '](Images/Tutorials/cad-side-view.jpg)

## Tutorial 2 - Introduction to GPS

The goal for tutorial 2 was to teach us how to use the GPS with the RaspberryPi. We also soldered header pins to the GSP. This is to be able to connect the GPS to the Pi.

The configuration of the RaspberryPi settings had to be modified in order to be able to accept the data from the GPS through the serial port. Then, we installed the _Minicom_ library which will make the reading from the data manageable. After the setting up process, we use the followig command to get data from the GPS directly:

> cat /dev/ttyAMA0

Note that the first time to obtain data, the GPS takes about 15-30 to initialize.

We also included a code given to us, which will take in a reading of data and then it extracts the required fields to and the output of the GPS is a link to Google Maps with the current location of the GPS.

> Tutorials/GPS.py

## Tutorial 3 - Color Segmentation

In this tutorail we learned about color segmentation and color tracking. We learned about HSV space which is less error prone to change in lighting, and we learned how to convert colors in to HSV. We used color ranges to look for a specific color in an image, in this case we were looking for red color and since red color requires two color ranges (it is at the beginning and end of color spectrum angle range (in first and fourth quadrant)). After color range filtering, we denoised an image in case the color is in darker shade, using other image processing methods claled opening which is erosion followed with dialation (closing is revered). Then we used connected component labeling which breaks the objects that are connected into differnet segments and labels them. when the largest object of that color is found only that object is set to be true and visible and finally we set horizontal distance from the middle. Anything to the right of the middle point is positive value and to left will be negative value. Finally we used a red object to test and confirm that this function is working.

## Tutorial 4 - Stepper Motors

In this tutorial we learned how to setup and connect a stepper motor in a circuit. We wrote a python script to use a stepper motor and rotate its rotor for an amount of degrees based on the number of steps that we may need in either direction. As far as I know a full step is a rotation with change of angle twice as much as a half step. In half step mode stepper motor will take twice more so theres more stops which gives it more accuracy. I also noticed that half step has less torque but full step has more torque which makes sense since it just needs to move furthur. InitDelay initializes a delay after GPI is initialized and before motor is moved which gives some time for initialization and "wait (0.002)" is the amount of delay betweent each step. I noticed with 0.001 the motor couldn't rotate the camera anymore but it was fine with higher steps which was weird. but generally when its higher it will take more time to reach a set number of steps.

## Tutorial 5 - PID Controller

In this tutorial we learned what closed loop systems are and how to deal with residual momentum before and after we start. We learned about PID (proportional integral derivative) which is a control loop mechanism that creates a feedback for our use for stepper motor and the camera. We learned individually about proportioanl gain Kp(changes input based on the amount of error proportioanlly), derivative gain Kd(saves hange of error), and integral gain Ki(adds up all the error). Next we used a python script to implement the closed loop system for stepper motor control for tracking. We started with initial minimum step time and some PID values to be tweeked if needed. We calculated speed controll, then we checked if the speed value is below zero to know if we need to rotate. we try to make sure that the object we are tracking is in the middle of the screen and not off by more than 20 pixels.

# Challenges

## Challenge 1: ECE 140a final boss

https://youtu.be/evNxebSdrfM
