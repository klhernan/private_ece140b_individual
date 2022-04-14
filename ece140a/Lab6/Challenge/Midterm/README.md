Sepehr Bostanb A16062097
Karen Hernandez A16118872

Tutorial1:
In this tutorial we learned how to boot up a rsapberryPi, install the sd Card with proper user settings, and setp up the environment.
we also learned how to interact with the linux os interface and setup and run mysql using mariadbd. we redid tutorial 1 and 3 of lab 5 successfully and moved on to tutorial 2.

Tutorail2:
In this tutrial we leanred how to build circuits and interact with them with raspberryPi and python using VSCode. First we setup ultrasound sensor and received the readings from it and then we setup the noise sensor that indicates when the ultrasound sensor is reading and when it is not reading. Additionally we attached the joystick after some debugging we were able to get the readings from the joystick as well.

Challenge 1:
after confirming with the TAs we decided to record and save the sensor readings into the sql database table before website launch mainly for better performance. We input the sonar distance reading along wiht x and y direction of the joystick and we save the timestamp of each reading per second. next using a restful server we used user interaction with different ranges of the sensor reading to display the sensor the recorded data for the requested ranges. 