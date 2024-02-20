#include "ros/ros.h"
#include "temphum/getTandH.h"
#include "temphum/getTandHResponse.h"
#include <cstdlib>
#include <sensor_msgs/NavSatFix.h>
#include <sensor_msgs/NavSatStatus.h>
using namespace sensor_msgs;
double lon=0.0, lat=0.0;
void callback(const NavSatFixConstPtr &fix) {

  if (fix->status.status == NavSatStatus::STATUS_NO_FIX) {
    std::cout << "Unable to get a fix on the location." << std::endl;
    return;
  }
  lon = fix->longitude;
  lat = fix->latitude;
//  std::cout << "Current Latitude: " << lat << std::endl;
//  std::cout << "Current Longitude " << lon << std::endl;

}
ros::ServiceClient client; 
void timerCallback(const ros::TimerEvent& t)
{
  char comando[255];
  temphum::getTandH srv;
   std::cout << "Timer" << std::endl;
  if (client.call(srv))
  {
 //   ROS_INFO("Sum: %f", srv.response.temperatura);
     sprintf(comando,"curl --data \"node=sensori&data={temperatura:%f,umidita:%f,radiazione:%f,latitudine:%f,longitudine:%f}&apikey=ff441103cdd16ec18708b09efebd5578\" \"https://emoncms.org/input/post\"",srv.response.temperatura,srv.response.umidita,srv.response.radiazione,lat,lon);
    system(comando);

  }
  else
  {
    ROS_ERROR("Failed to call service ");
    return ;
  }
}
int main(int argc, char **argv)
{
  ros::init(argc, argv, "Sensori");

  ros::NodeHandle n;
  client = n.serviceClient<temphum::getTandH>("getSensorData");
  ros::Subscriber gps_sub = n.subscribe("/sensors/gps_0/fix", 1, callback);
  ros::Timer timer = n.createTimer(ros::Duration(10.0), timerCallback);
  ros::spin();
  return 0;
}


