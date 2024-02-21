#!/usr/bin/env python
import rospy
import minimalmodbus
import serial
from timeloop import Timeloop
import time
from datetime import timedelta
from temphum.srv import getTandH,getTandHResponse

#instr.close_port_after_each_call=True


def handle_getTempAndHumidity(req):
    
    
    #time.sleep(2) # sleep 1 secondo 
    try:
         umidita = instr.read_register(registeraddress=2,functioncode=4,number_of_decimals=2 )
    except minimalmodbus.NoResponseError:
         time.sleep(2)
         umidita = instr.read_register(registeraddress=2,functioncode=4,number_of_decimals=2 )
    
   
    try:
        solare = instr.read_register(registeraddress=0,functioncode=3,number_of_decimals=0 )
    except minimalmodbus.NoResponseError: 
        time.sleep(1)
        solare = instr.read_register(registeraddress=0,functioncode=3,number_of_decimals=0 )   
        #print('Solare is: %.1f \r' % solare)
        #time.sleep(1)
    
    time.sleep(1)
    try:
        temperatura = instr.read_register(registeraddress=1,functioncode=4,number_of_decimals=2 )
    except minimalmodbus.NoResponseError: 
        time.sleep(1)
        temperatura = instr.read_register(registeraddress=1,functioncode=4,number_of_decimals=2 )   
        #print (temperatura)
    return getTandHResponse(temperatura,umidita,solare)

def getSensorData():
    device = rospy.get_param('/get_sensor_data_server/port')
    try:
    	instr = minimalmodbus.Instrument(device, 1)
    	instr.serial.baudrate=9600
    	instr.debug=True
   	instr.mode= 'rtu'
    	instr.clear_buffers_before_each_transaction = True
    except Exception as error:
                print "[!] Exception occurred: ", error
		exit
    else:
                
        rospy.init_node('get_sensor_data_server')
        s = rospy.Service('getSensorData', getTandH, handle_getTempAndHumidity)
        print("Ready to get temperature and humidity")
        rospy.spin()


if __name__ == "__main__":  #main loop
    
    getSensorData()
