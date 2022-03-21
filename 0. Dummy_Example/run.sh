source ./devel/setup.bash
gnome-terminal --window-with-profile=kss -e 'roscore'
sleep 3
gnome-terminal --window-with-profile=kss -e 'rosrun tello_hardware position.py'
gnome-terminal --window-with-profile=kss -e 'rosrun tello_hardware action_server.py'
sleep 2
gnome-terminal --window-with-profile=kss -e 'rosrun tello_vision img_pub.py'
gnome-terminal --window-with-profile=kss -e 'rosrun tello_vision img_sub.py'



