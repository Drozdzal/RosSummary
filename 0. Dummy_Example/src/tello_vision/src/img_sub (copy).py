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
'''
Due to the fact that drone will be flying in Poland i am using abs value (Exif gives error when i
'''


class RpiSub:
    def __init__(self):
        rospy.init_node('img_sub')
        self.client_ = actionlib.SimpleActionClient('name', MissionAction)
        self.client_.wait_for_server()
        print("widze")
        goal = MissionGoal()
        goal.number_of_waypoints = 8
        goal.list_of_waypoints = [50, 0, 0, 0,
                                  0, 0, 0, 90,
                                  50, 0, 0, 0,
                                  0, 0, 0, 90,
                                  50, 0, 0, 0,
                                  0, 0, 0, 90,
                                  50, 0, 0, 0,
                                  0, 0, 0, 90,
                                  ]
        self.client_.send_goal(goal)
        print("wyslane")
        result = self.client_.wait_for_result()

    def send_on_action(self):
        goal = MissionGoal()
        goal.number_of_waypoints = 8
        goal.list_of_waypoints = [50, 0, 0, 0,
                                  0, 0, 0, 90,
                                  50, 0, 0, 0,
                                  0, 0, 0, 90,
                                  50, 0, 0, 0,
                                  0, 0, 0, 90,
                                  50, 0, 0, 0,
                                  0, 0, 0, 90,
                                  ]
        self.client_.send_goal(goal)
        print("wyslane")
        result = self.client_.wait_for_result()
    def take_off(self):


    def img_callback(self, img_msg):
        cv_image = self.bridge.imgmsg_to_cv2(img_msg)
        imgHSV = cv2.cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
        lower_lemon = np.array([0, 202, 0])
        upper_lemon = np.array([28, 255, 255])
        lemon_threshold = 200000
        field_mask = cv2.inRange(imgHSV, lower_lemon, upper_lemon)
        if np.sum(field_mask)>lemon_threshold:
            self.send_on_action()
        lower_apple = np.array([0, 174, 0])
        upper_apple = np.array([12, 255, 55])
        apple_threshold = 100000
        if np.sum(field_mask)>lemon_threshold:
            self.self_takeoff()


if __name__ == '__main__':
    RpiSub()
    rospy.spin()
