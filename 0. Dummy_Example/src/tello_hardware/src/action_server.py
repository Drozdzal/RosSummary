import rospy

import actionlib

import actionlib_tutorials.msg
from tello_msgs.msg import MissionGoal, MissionAction, MissionResult, MissionFeedback
from tello_msgs.srv import Move, MoveRequest, MoveResponse
from tello_msgs.srv import Command, CommandRequest, CommandResponse
from time import sleep

class FibonacciAction(object):
    # create messages that are used to publish feedback/result
    _feedback = MissionFeedback()
    _result = MissionResult()

    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, MissionAction,
                                                execute_cb=self.execute_cb, auto_start=False)
        rospy.wait_for_service('move')
        self.ask_move=rospy.ServiceProxy('move', Move)
        rospy.wait_for_service('command')
        self.ask_command=rospy.ServiceProxy('command', Command)
        print("Server started")
        self._as.start()


    def execute_cb(self, goal):
        command_req = CommandRequest()
        command_req.message = 'start'
        self.ask_command(command_req)
        command_req = CommandRequest()
        command_req.message = 'take_off'
        self.ask_command(command_req)
        sleep(1)
        print("Received mission")
        # helper variables
        r = rospy.Rate(1)
        success = True

        # append the seeds for the fibonacci sequence
        self._feedback.waypoint=0

        # publish info to the console for the user
        rospy.loginfo('%s: Executing, creating fibonacci sequence of order %i with seed' % (
        self._action_name, goal.number_of_waypoints))
        r.sleep()
        # start executing the action
        for i in range(1, goal.number_of_waypoints):
            # check that preempt has not been requested by the client
            rospy.wait_for_service('move')
            move_req = MoveRequest()
            move_req.x=goal.list_of_waypoints[i*4]
            move_req.y=goal.list_of_waypoints[i*4+1]
            move_req.z=goal.list_of_waypoints[i*4+2]
            move_req.yaw=goal.list_of_waypoints[i*4+3]
            self.ask_move(move_req)

        if success:
            command_req = CommandRequest()
            command_req.message = 'land'
            self.ask_command(command_req)
            print("land")
            # helper variables
            r = rospy.Rate(1)
            success = True
            rospy.loginfo('%s: Succeeded' % self._action_name)
            self._as.set_succeeded(self._result)


if __name__ == '__main__':
    rospy.init_node('fibonacci')
    server = FibonacciAction('name')
    rospy.spin()