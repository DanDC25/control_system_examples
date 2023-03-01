import math
import random
from vexcode_vr import *

# Brain should be defined by default
brain=Brain()

drivetrain = Drivetrain("drivetrain", 0)
pen = Pen("pen", 8)
pen.set_pen_width(THIN)
left_bumper = Bumper("leftBumper", 2)
right_bumper = Bumper("rightBumper", 3)
front_eye = EyeSensor("frontEye", 4)
down_eye = EyeSensor("downEye", 5)
front_distance = Distance("frontdistance", 6)
distance = front_distance
magnet = Electromagnet("magnet", 7)
location = Location("location", 9)

def driveXDistance(setpoint,duration):
    # reset the timer
    brain.timer_reset()
    TOLERANCE = 10
    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        # CREDIT: MOTORIZED ARM SIMULATION FROM P5JS https://editor.p5js.org/dcan25/sketches/SpawXnZyI
        robot_Xlocation = location.position(X, MM)
        k = 2
        error = setpoint - robot_Xlocation
        output = k*error
        #Here, my output is the velocity the robot will run at. This will make the robot run faster, and smoother.
        if(output > 100):
            output = 100
        if(output < -100):
            output = 0
        drivetrain.set_drive_velocity(output,PERCENT)
        if(robot_Xlocation < setpoint - TOLERANCE):
            drivetrain.drive(FORWARD)
        elif(robot_Xlocation > setpoint + TOLERANCE):
            drivetrain.drive(REVERSE)
        else:
            drivetrain.stop()
        










        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    drivetrain.stop()

def driveYDistance(setpoint,duration):
    # reset the timer
    brain.timer_reset()
    TOLERANCE = 10
    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        # Your code goes here!
        robot_Ylocation = location.position(Y, MM)
        k = 2
        error = setpoint - robot_Ylocation
        output = k*error
        #Here, my output will determine the velocity my robot will run at. This will make the robot run faster, and smoother. This will make the robot faster when it's not at the setpoint and inturn stop it when it goes past.
        if(output > 100):
            output = 100
        if(output < -100):
            output = 0
        drivetrain.set_drive_velocity(output,PERCENT)
        if(robot_Ylocation < setpoint - TOLERANCE):
            drivetrain.drive(FORWARD)
        elif(robot_Ylocation > setpoint + TOLERANCE):
            drivetrain.drive(REVERSE)
        else:
            drivetrain.stop()







        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    drivetrain.stop()


def driveDiagDistance(setpoint,duration):
    # reset the timer
    brain.timer_reset()
    TOLERANCE = 10
    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        # Your code goes here!
        robot_Ylocation = location.position(Y, MM)
        k = 2
        error = setpoint - robot_Ylocation
        output = k*error
        #Here, my output is the velocity the robot will run at. This will make the robot run faster, and smoother.
        if(output > 100):
            output = 100
        if(output < -100):
            output = 0
        drivetrain.set_drive_velocity(output,PERCENT)
        if(robot_Ylocation < setpoint - TOLERANCE):
            drivetrain.drive(FORWARD)
        elif(robot_Ylocation > setpoint + TOLERANCE):
            drivetrain.drive(REVERSE)
        else:
            drivetrain.stop()










        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    drivetrain.stop()

# Add project code in "main"
def main():
    pen.set_pen_color(BLACK)
    pen.move(DOWN)
    drivetrain.turn_to_heading(90,DEGREES,wait=True)
    driveXDistance(0,3)
    drivetrain.set_drive_velocity(100,PERCENT)
    drivetrain.turn_to_heading(0,DEGREES,wait=True)
    driveYDistance(0,3)
    drivetrain.turn_to_heading(45,DEGREES,wait=True)
    driveDiagDistance(400,4)
# VR threads — Do not delete
vr_thread(main())
