import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError
from datetime import datetime
import rospy
import math
from tello_msgs.msg import MissionGoal, MissionAction, MissionResult, MissionFeedback
import actionlib
import numpy as np
from tello_msgs.srv import Command, CommandRequest, CommandResponse
from time import sleep
'''
Due to the fact that drone will be flying in Poland i am using abs value (Exif gives error when i
'''


class Controller:
    def __init__(self):
        rospy.init_node('img_sub')
        self.client_ = actionlib.SimpleActionClient('name', MissionAction)
        self.client_.wait_for_server()
        self.bridge = CvBridge()
        self.ask_command = rospy.ServiceProxy('command', Command)
        self.move_finished = True
        def img_callback_closure(img_msg):
            self.img_callback(img_msg)

        rospy.Subscriber('rpicam', Image, img_callback_closure)

    def send_on_action(self):
        print("found lemon")
        goal = MissionGoal()
        goal.number_of_waypoints = 8
        goal.list_of_waypoints = [30, 0, 0, 0,
                                  30, 0, 0, 0,
                                  0, 0, 0, 90,
                                  0, 0, 0, 90,
                                  30, 0, 0, 0,
                                  30, 0, 0, 0,
                                  0, 0, 0, 90,
                                  0, 0, 0, 90,
                                  ]
        self.client_.send_goal(goal)
        print("wyslane")
        result = self.client_.wait_for_result()
        self.move_finished = True

    def take_off(self):
        print("found roller")
        command_req = CommandRequest()
        command_req.message = 'start'
        self.ask_command(command_req)
        command_req = CommandRequest()
        command_req.message = 'take_off'
        sleep(1)
        self.ask_command(command_req)
        command_req = CommandRequest()
        command_req.message = 'land'
        self.ask_command(command_req)
        self.move_finished = True
        sleep(1)

    def img_callback(self,img_msg):
        if self.move_finished==True:
            cv_image = self.bridge.imgmsg_to_cv2(img_msg)
            imgHSV = cv2.cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
            lower_lemon = np.array([0, 202, 0])
            upper_lemon = np.array([28, 255, 255])
            lemon_threshold = 200000
            field_mask = cv2.inRange(imgHSV, lower_lemon, upper_lemon)
            if np.sum(field_mask) > lemon_threshold:
                self.move_finished = False
                self.send_on_action()
            lower_roller = np.array([85, 161, 0])
            upper_roller = np.array([110, 255, 255])
            field_mask=0
            roller_threshold = 2000000
            field_mask = cv2.inRange(imgHSV, lower_roller, upper_roller)
            if np.sum(field_mask) > roller_threshold:
                self.move_finished = False
                self.take_off()
        else:
            pass


if __name__ == '__main__':
    Controller()
    rospy.spin()
