# Hack the Truck : Platooners Team 13 🚚
A Connected Truck Service for Platooning where sensor data from the leader truck is used by the following trucks. This service keeps in mind safety in truck navigation which using multi-hop communication or cloud based services for communication.
![Truck overview](img/truck_overview.jpg)

Everything in the truck is connected to some PCs we have in the back. The PCs are connected to each other with a regular ethernet switch. For unifying the communication, our middleware **Eclipse eCAL™** (which is open source) is used. So, for receiving sensor data in your application and controlling actuators you only need to **connect your notebook** to the same switch.
