project_name=$1
mkdir ${project_name}
cd ${project_name}
mkdir src
catkin_make
cd src
catkin_create_pkg ${project_name}_bringup std_msgs rospy roscpp
catkin_create_pkg ${project_name}_hardware std_msgs rospy roscpp
catkin_create_pkg ${project_name}_msgs std_msgs rospy roscpp
catkin_create_pkg ${project_name}_vision std_msgs rospy roscpp
cd ${project_name}_msgs
mkdir srv
mkdir action
mkdir msg
cd

cp setup.py ${project_name}/src/${project_name}_bringup/setup.py
cp setup.py ${project_name}/src/${project_name}_hardware/setup.py 
cp setup.py ${project_name}/src/${project_name}_msgs/setup.py
cp setup.py ${project_name}/src/${project_name}_vision/setup.py

 
