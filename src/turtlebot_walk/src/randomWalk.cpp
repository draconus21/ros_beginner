#include "ros/ros.h"
#include "geometry_msgs/Twist.h"
#include "sensor_msgs/LaserScan.h"
#include <cmath>
#include <iostream>
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>

int closeToObst = 0;
float action_duration = 0.25;
float movement_speed = 0.25;
float turn_speed = 0.5;
float min_turn_duration = 3.5;
float max_turn_duration = 10.5;
float min_wall_distance = 0.8;

//Callback will be called when there is a message on the subscribed topic. Here topic is "/scan"
void scannerCallback (const sensor_msgs::LaserScan::ConstPtr& scan)
{
	//scan->ranges gives the ranges scanned from the laser.
	// This is a vector of float representing the distance of the robot from the obstacle.
	// Choosing only three beams to decide wheter to turn or keep walking staright.
	// Leftmost Beam : a[0], Central Beam 
	std::vector<float> a = scan->ranges;
	ROS_INFO("The Range in the front = %f",a[(int)a.size()/2]);
	if((a[0] < min_wall_distance)||(a[(int)a.size()/2] < min_wall_distance)||(a[a.size()-1] < min_wall_distance))
	{
		//Close to Obstacle
		closeToObst=1;
	}
	else
	{
		//Still Far from Obstacle
		closeToObst=0;
	}
	
}

//Method to generate a random duration to turn
float random_duration()
{
	/* initialize random seed: */
	srand (time(NULL));
	/* generate random number between 1 and 10*/
	float random = rand() % 10 + 1;
	float duration = min_turn_duration + random * (max_turn_duration - min_turn_duration);
	return duration/10;
}

//Method to turn in place for the given duration
void turn(ros::Publisher cmd_pub,float duration, float turn_speed)
{
	geometry_msgs::Twist vel;
	//ros::Time::now().toSec() : gives the current time in seconds.
	//stopTime here indicated the duration for the robot to keep turning
	double stopTime = ros::Time::now().toSec() + duration;
	while(ros::Time::now().toSec() < stopTime)
	{
		ROS_INFO("Turning for %f seconds",duration);
		vel.linear.x = 0.0; vel.linear.y = 0.0; vel.linear.z = 0.0;
		vel.angular.x = 0.0; vel.angular.y = 0.0; vel.angular.z = turn_speed;
		cmd_pub.publish(vel);
		ros::Duration(action_duration).sleep(); //Helps in maintaining the message publishing rate.
	}
}

int main(int argc, char **argv)
{
	ros::init(argc, argv, "randomWalk");
	ros::NodeHandle n;
	//Topic : /cmd_vel_mux/input/navi takes the command for controlling the turtlebot's navigation
	ros::Publisher cmd_pub = n.advertise<geometry_msgs::Twist>("/cmd_vel_mux/input/navi", 1000);
	//Topic : /scan provides the laser scan messages.
	ros::Subscriber sub = n.subscribe("/scan", 1000, scannerCallback);

	geometry_msgs::Twist vel;
	while (ros::ok())
	{
		if (closeToObst == 1)
		{
			//If the Obstacle is close then turn for a random duration
			ROS_INFO("Very Close to Obstacle. Turning for a Random duration.");
			float duration = random_duration();
			turn(cmd_pub, duration, turn_speed);
		}
		else
		{
			//If the Obstacle is far then keep walking straight
			ROS_INFO("Moving straight ahead");
			vel.linear.x = movement_speed; vel.linear.y = 0.0; vel.linear.z = 0.0;
			vel.angular.x = 0.0; vel.angular.y = 0.0; vel.angular.z = 0.0;
			cmd_pub.publish(vel);
			ros::Duration(action_duration).sleep();
		}
		ros::spinOnce();
	}
	return 0;
}
