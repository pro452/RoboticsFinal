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
    rightMoto.run_to_rel_pos(position_sp=100, speed_sp=50, stop_action='brake')
    leftMoto.run_to_rel_pos(position_sp=-100, speed_sp=50, stop_action='brake')
    while rightMoto.is_running:
        if colSen.value() < 12:
            leftMoto.stop(stop_action='brake')
            rightMoto.stop(stop_action='brake')
            return
    leftMoto.run_forever(speed_sp=100)
    rightMoto.run_forever(speed_sp=-100)
    while leftMoto.is_running:
        if colSen.value() < 12:
            rightMoto.stop(stop_action='brake')
            leftMoto.stop(stop_action='brake')
            break

def move_foward():
    rightMoto.run_to_rel_pos(position_sp=390, speed_sp=50, stop_action='brake')
    leftMoto.run_to_rel_pos(position_sp=390, speed_sp=50, stop_action='brake')

    while rightMoto.is_running:
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
    rightMoto.run_to_rel_pos(position_sp=-10, speed_sp=100, stop_action='brake')
    leftMoto.run_to_rel_pos(position_sp=-10, speed_sp=100, stop_action='brake')
    sleep(2)
    #half quarter turn right to cross the N/S line
    rightMoto.run_to_rel_pos(position_sp=-190, speed_sp=100, stop_action="hold")
    leftMoto.run_to_rel_pos(position_sp=190, speed_sp=100, stop_action="hold")
    sleep(4)
    #While the sensor is not on the W/E line, turn right stop when the sensor detects the line
    while colSen.value() > 15 :
        rightMoto.run_forever(speed_sp=100)
        leftMoto.run_forever(speed_sp=-100)
    rightMoto.stop()
    leftMoto.stop()


def turnLeftWithPercision() :
    rightMoto.run_to_rel_pos(position_sp=-20, speed_sp=100, stop_action='brake')
    leftMoto.run_to_rel_pos(position_sp=-20, speed_sp=100, stop_action='brake')
    sleep(2)
    #half quarter turn left to cross the N/S line
    rightMoto.run_to_rel_pos(position_sp=170, speed_sp=100, stop_action="hold")
    leftMoto.run_to_rel_pos(position_sp=-170, speed_sp=100, stop_action="hold")
    sleep(4)
    #While the sensor is not on the W/E line, turn left stop when the sensor detects the line
    while colSen.value() > 15 :
        rightMoto.run_forever(speed_sp=100)
        leftMoto.run_forever(speed_sp=-100)
    rightMoto.stop()
    leftMoto.stop()
