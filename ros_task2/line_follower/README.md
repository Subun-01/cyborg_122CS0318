
# ROS_task2

This package contains the necessary code and instructions to teleoperate a robot in Gazebo using ROS (Robot Operating System) and process images as well as follow the line.

##  Objectives

1) To Build a world as shown in the sample image using the arena image provided
2) Write a launch file so as to spawn the bot urdf (urdf provided in drive link) in the arena made.
3) Add differential drive plugin and try to teleop the bot 
4) Add camera plugin to the robot and write a ros script which subscribes to the image and display it using opencv. 
5)Add a script to follow the lines
## Prerequisites
ROS noetic  
Gazebo   
Python3  
OpenCV library


## Package ( line_follower ) contains

### launch
world.launch: : It's a launch file for the gazebo world,bot and required scripts.
### meshes
It contains the parts required for making the bot.          
### model
It contains the .sdf,.config,.material and texture file required to create the desired path in gazebo world.
### world
It contains the myworld.world file that describes the gazebo world along with the pre-designed bot.
### urdf
It contains the .urdf file to build the bot using meshes given.
### script 
It has a pyhton-script coded to display the image receiving from the bot cam.  
## Running the bot

(in terminal) Launching our world.launch file that contains the line_follower bot
```bash
~$ roslaunch line_follower world.launch
```



## Demo

[Screenshot](https://drive.google.com/file/d/1jgGNeQwhhFJM12g-FpKOI0k_bTGR7gB2/view?usp=drivesdk)



## Documentation

[Gazebo](https://classic.gazebosim.org/tutorials)
 
 (other support)
 
[Displaying the image](https://dhanuzch.medium.com/using-opencv-with-gazebo-in-robot-operating-system-ros-part-1-display-real-time-video-feed-a98c078c708b)
