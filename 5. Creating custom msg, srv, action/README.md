# Creating custom msg, srv, action
ROS enables us to create custom message, service and action files. Process of creating such a simmilar for all of these ways of communication. We have to write file which consist all data, then add it to CMakeList of our package and type catkin_make in root of our workspace.

Creating custom message:
---
Create .msg file. For example, lets say that our robot has 3 servos. We may create a messages like servo_vals:

float32 left_arm
float32 right_arm
float32 head

We can use standard messages to create our message or we may use messages from different packages to create a new one.
As an example we may create message which include I

When we've created such a file we have to add it to the CMakeList.txt then we need to catkin_make in root of the workspace.
Remember also to type source ./devel/setup.bash. Or add to XX FILE TO EXECUTE IT WHEN NEW prompt is created.

Creating custom service
---
Adding new service. Adding new service is very similar to creating ros msg. But let's say that service needs "two messages". All service needs defined request and responce even if they're empty.
EXAMPLE:

int32 x
int32 y
int32 z
int32 yaw
---
bool is_moved

Our request takes 3 floats. These floats are named x,y and z.
Our response is a bool msg which is named is_moved.
Messages created also can be used in request or response of our server.

Response is divided from request by ---.So each of services is created as :

request_messages

--- 
response messages

Creating custom action
---
When we want to create action we need to add actionlib in our CMakeList.txt file.
For action messages it's best to create additional file let's name it action. 

#goal definition
uint8 number_of_waypoints
uint8[] list_of_waypoints
---
#result definition
bool finished_move
---
#feedback definition
int32 waypoint
