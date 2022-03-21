import rospy
from tello_msgs.srv import Move, MoveRequest, MoveResponse
from tello_msgs.srv import Command, CommandRequest, CommandResponse

'''
Script for checking whether drone knows how to move in local or not it needs server to work (move_tmotor.py)
'''

def move():
        rospy.init_node('move_xy_pub', anonymous=True)
        rate = rospy.Rate(1)  # 1Hz

        while not rospy.is_shutdown():
                rate.sleep()
                rospy.wait_for_service('move')
                ask_to_move= rospy.ServiceProxy('move', Move)
                req=MoveRequest()
                req.x=float(input("o ile x"))
                req.y=float(input("o ile y"))
                ask_to_move(req)




if __name__ == '__main__':
    try:
        rospy.wait_for_service('command')
        ask_command = rospy.ServiceProxy('command', Command)
        req = CommandRequest()
        req.message='start'
        ask_command(req)
        rospy.wait_for_service('command')
        req.message = 'take_off'
        ask_command(req)
        move()
    except rospy.ROSInterruptException:
        pass
