#!/usr/bin/env python
#import rospy
import minimalmodbus
import serial
from timeloop import Timeloop
import time
from datetime import timedelta
#from temphum.srv import getTandH,getTandHResponse
instr = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
instr.serial.baudrate=9600
instr.debug=True
instr.BYTEORDER_BIG=0
instr.mode= 'rtu'
instr.clear_buffers_before_each_transaction = True
#instr.close_port_after_each_call=True




if __name__ == "__main__":  #main loop
   instr.write_register(0x07D0,5,functioncode=6)
