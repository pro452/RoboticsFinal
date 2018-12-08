#!/usr/bin/env python3
#programmed by Matthew Chabalowski
from ev3dev.ev3 import *
from time import sleep

lm = LargeMotor('outB')
rm = LargeMotor('outC')

def moveStraightWithPercision() :
    #move straight roughly 7.5 inches
    rm.run_to_rel_pos(position_sp=360, speed_sp=100, stop_action="hold")
    lm.run_to_rel_pos(position_sp=360, speed_sp=100, stop_action="hold")
    sleep(5)
def turnRightWithPercision() :
    #quarter turn right
    rm.run_to_rel_pos(position_sp=-180, speed_sp=100, stop_action="hold")
    lm.run_to_rel_pos(position_sp=180, speed_sp=100, stop_action="hold")
def turnLeftWithPercision() :
    #quarter turn right
    rm.run_to_rel_pos(position_sp=-180, speed_sp=100, stop_action="hold")
    lm.run_to_rel_pos(position_sp=180, speed_sp=100, stop_action="hold")