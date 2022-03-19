# What is ROS
ROS - Robotic Operating System is an open-source framework which is usefull for creating robotics software.
Such a "framework" allows us to create workspace for our robot and to seperate robot functionalities into 
ROS packages.


Communication in ROS can be divided into 3 groups:

- Topics (Publishers, Subscriber) -> This type of messages  allows to send data asynchronously. Topics works simmilary to STM32 interruptions.  
- Service (Service Server, Service Client)  -> services allow to synchronously ask to do specyfic tasks. Client asks service for response and waits till 
  he doesnt get it. 
- Action (Action Server, Action Client) -> Actions are designed for performing long term tasks. For example if we want robot to move from point
A to point B. We may give him a list of waypoints and send this list of waypoints and wait till he doesnt execute it. Actions allow us to get
  task feedback to have information about current performance of an action.

When we are talking about ROS, there is few version of this "framework". We can use ROS2 which is the newest version or ROS1.
This versions have multiple distribions. Right now the version of ROS which will be used in Humanoid Robot project is Noetic. In the future
we may want to move to ROS2.
          
![img_3.png](ros_quintessence.png)

Image above is in my opinion a quintessence of ROS. Even though this image is captured from ROS2 documentation it shows how
ROS communication works.