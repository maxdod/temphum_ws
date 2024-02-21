# temphum_ws
Sarf service to get sensor data using temperature &amp; humidity SHT20 sensor modbus RTU
Added sensor for radiation
/getSensorData is the name of Service Server

returns temperatura and umidita


rosservice call /getSensorData
temperatura: 20.43
umidita: 54.91


requirements: pip install minimalmodbus 

to build : catkin_make on temphum_ws

to run: rosrun temphum scripts/getTempAndHumidity.py

Publish Data:
rosrun temphum send_sensor_data



default port /dev/ttyUSB0
change permissions : sudo chmod 777 /dev/ttyUSB0 or add user to dialout group
![image](https://user-images.githubusercontent.com/39596051/220868243-df5a2fbf-03ef-4b33-b51a-3704ec85ad41.png)
