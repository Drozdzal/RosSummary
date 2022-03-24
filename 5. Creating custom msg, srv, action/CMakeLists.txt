cmake_minimum_required(VERSION 3.0.2)
project(tello_msgs)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)


find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
   actionlib
)

#It must be called before generate messages
catkin_python_setup()

add_message_files(
  FILES
  image_msg.msg
  servo_vals.msg
)

add_service_files(
    FILES
    Command.srv
    Move.srv
)

add_action_files(
        DIRECTORY action
        FILES
        Mission.action

)

generate_messages(
  DEPENDENCIES
  std_msgs
  actionlib_msgs
)

catkin_package(
  CATKIN_DEPENDS roscpp rospy std_msgs message_runtime
)
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)



