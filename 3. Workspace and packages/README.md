# Workspace and packages
ROS enables us to create Worspaces -> which are lets say projects a
- Worspaces -> which are let's say projects
- Packages -> which are part of a project.  
For clarity of the code I would recomment do divide each of robot functionalities into different packages.
As an example I will use humanioid robot. Our repo may be divided into:
- humanoid_bringup
- humanoid_footbal_core
- humanoid_hardware
- humanoid_inverse_kinematics
- humanoid_msgs
- humanoid_particle_filter
- humanoid_vision  
Each of these packages contains functionality of named directory.
![img.png](img.png)
  
Script create_workspace.sh creates us whole workspace with packages listed above. And also creates a link between
humanoid_msgs package and other packages. It was designed this way because same messages may be the same for all of the packages.
