#!/usr/bin/env python
import rospy
import minimalmodbus
import serial
import time
from datetime import timedelta
from temphum.srv import getTandH,getTandHResponse
instr = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
instr.serial.baudrate=9600
instr.debug=False
instr.mode= 'rtu'
#instr.close_port_after_each_call=True


def handle_getTempAndHumidity(req):
    
    
    
    umidita = instr.read_register(registeraddress=2,functioncode=4,number_of_decimals=2 )
   
    print (umidita)
    time.sleep(1)
    temperatura = instr.read_register(registeraddress=1,functioncode=4,number_of_decimals=2 )
    print (temperatura)
    return getTandHResponse(temperatura,umidita)

def getSensorData():
    rospy.init_node('get_sensor_data_server')
    s = rospy.Service('getSensorData', getTandH, handle_getTempAndHumidity)
    print("Ready to return temperature & humidity")
    rospy.spin()


if __name__ == "__main__":  #main loop
    getSensorData()
