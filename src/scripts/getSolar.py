#!/usr/bin/env python
#import rospy
import minimalmodbus
import serial
from timeloop import Timeloop
import time
from datetime import timedelta
#from temphum.srv import getTandH,getTandHResponse
instr = minimalmodbus.Instrument('/dev/ttyUSB1', 5)
instr.serial.baudrate=9600
#instr.debug=True
instr.BYTEORDER_BIG=0
instr.mode= 'rtu'
instr.clear_buffers_before_each_transaction = True
instr.close_port_after_each_call=True
instr1 = minimalmodbus.Instrument('/dev/ttyUSB1', 1)
instr1.serial.baudrate=9600
instr1.serial.timeout =0.2
#instr1.debug=True
instr1.mode= 'rtu'
instr1.clear_buffers_before_each_transaction = True
#instr1.clear_buffers_before_each_transaction = True



def getSensorData():
    #rospy.init_node('get_solar')
    #//s = rospy.Service('getSolarData', getTandH, handle_getTempAndHumidity)
    #//rospy.spin()
    
    time.sleep(1)
    try:
         temperatura = instr1.read_register(registeraddress=1,functioncode=4,number_of_decimals=2 )
    except minimalmodbus.NoResponseError:
         time.sleep(2)
         temperatura = instr1.read_register(registeraddress=1,functioncode=4,number_of_decimals=2 )
    
    print('temperatura is: %.1f \r' % temperatura)
    try:
        solare = instr.read_register(registeraddress=0,functioncode=3,number_of_decimals=0 )
    except minimalmodbus.NoResponseError: 
        time.sleep(1)
        solare = instr.read_register(registeraddress=0,functioncode=3,number_of_decimals=0 )   
    print('Solare is: %.1f \r' % solare)
    time.sleep(1)
    try:
         umidita = instr1.read_register(registeraddress=2,functioncode=4,number_of_decimals=2 )
    except minimalmodbus.NoResponseError:
         time.sleep(2)
         umidita = instr1.read_register(registeraddress=2,functioncode=4,number_of_decimals=2 )
    
    print('umidita is: %.1f \r' % umidita)

if __name__ == "__main__":  #main loop
    getSensorData()
