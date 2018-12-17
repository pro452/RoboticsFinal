#!/usr/bin/env python3
#programmed by Matthew Chabalowski
from ev3dev.ev3 import *
from time import sleep

#initialize motors
leftMoto = LargeMotor('outB')
rightMoto = LargeMotor('outC')

#initialize color sensor
colSen = ColorSensor('in4')

def find_line():
    rightMoto.move_to_rel_pos(position_sp=50, speed_sp=50, stop_action='brake')
    while rightMoto.is_running:
        if colSen.value() < 12:
            rightMoto.stop(stop_action='brake')
            return
    leftMoto.move_to_rel_pos(position_sp=100, speed_sp=50, stop_action='brake')
    while leftMoto.is_running:
        if colSen.value() < 12:
            leftMoto.stop(stop_action='brake')
            break

def move_foward():
    rightMoto.move_to_rel_pos(position_sp=200, speed_sp=100, stop_action='brake')
    leftMoto.move_to_rel_pos(position_sp=200, speed_sp=100, stop_action='brake')

    while rm.is_running:
        if colSen.value() > 30 and colSen.value() < 70:
            rightMoto.stop(stop_action='brake')
            leftMoto.stop(stop_action='brake')
            find_line()
            break

def moveStraightWithPercision() :
    #move straight roughly 7.5 inches
    rightMoto.run_to_rel_pos(position_sp=360, speed_sp=100, stop_action="hold")
    leftMoto.run_to_rel_pos(position_sp=360, speed_sp=100, stop_action="hold")
    sleep(5)
    
def turnRightWithPercision() :
    #half quarter turn right to cross the N/S line
    rightMoto.run_to_rel_pos(position_sp=-180, speed_sp=100, stop_action="hold")
    leftMoto.run_to_rel_pos(position_sp=180, speed_sp=100, stop_action="hold")
    
    #While the sensor is not on the W/E line, turn right stop when the sensor detects the line
        while colSen.Value() > 50 :
        rightMoto.run_to_rel_pos(position_sp=-180, speed_sp=100, stop_action="hold")
        leftMoto.run_to_rel_pos(position_sp=180, speed_sp=100, stop_action="hold")

def turnLeftWithPercision() :
    #half quarter turn left to cross the N/S line
    rightMoto.run_to_rel_pos(position_sp=180, speed_sp=100, stop_action="hold")
    leftMoto.run_to_rel_pos(position_sp=-180, speed_sp=100, stop_action="hold")
    
    #While the sensor is not on the W/E line, turn left stop when the sensor detects the line
        while colSen.Value() > 50 :
        rightMoto.run_to_rel_pos(position_sp=180, speed_sp=100, stop_action="hold")
        leftMoto.run_to_rel_pos(position_sp=-180, speed_sp=100, stop_action="hold")
