# Hack the Truck : Platooners Team 13 🚚
A Connected Truck Service for Platooning where sensor data from the leader truck is used by the following trucks. This service keeps in mind **driving safety** in truck navigation which using multi-hop communication or cloud based services for communication using **Eclipse eCAL™** 

## Project Overview 
-  Real-time camera data is acessed via ethernet using middleware **Eclipse eCAL™**
- The camera topic is subscribed by our algorithm and then the each frame image data type is convered into opencv image 
- Object detection is done using Fast RCNN on each frame 
- Total objects detected per frame , per GPS location with Timestamp are published for the following truck of the platoon to subscribe
- Commmuncation can be done by **Eclipse eCAL™** UDP protocol where each truck route the messages around its range or messages can be send to cloud database through which all trucks connected to service can access via over the air 5G network. 
![Truck overview](img/truck_overview.jpg)

Everything in the truck is connected to some PCs we have in the back. The PCs are connected to each other with a regular ethernet switch. For unifying the communication, our middleware **Eclipse eCAL™** (which is open source) is used. So, for receiving sensor data in your application and controlling actuators you only need to **connect your notebook** to the same switch.

## To run the service
- git clone the repository 
- Install the requirements
- Intsall **Eclipse eCAL™**
- Run platoonsDetectionMain.py in project 

## Results Demo


# Contact Team PLATOONER 
1. Adarsh Kuzhipathalil (Email : adarsh.kuzhipathalil@gmail.com)
https://www.linkedin.com/in/adarsh-kuzhipathalil/
2. Reshma Vasan R (Email : reshmavasan14@gmail.com)
https://www.linkedin.com/in/reshma-vasan/
3. Shubham Gupta (Email : st173207@stud.uni-stuttgart.de)
https://www.linkedin.com/in/shubg1994/
