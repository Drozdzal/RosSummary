import rospy
from tello_msgs.srv import Move, MoveRequest, MoveResponse
from tello_msgs.srv import Command, CommandRequest, CommandResponse
from djitellopy import tello
from time import sleep


class Motion():
    def __init__(self):
        self.drone=tello.Tello()
        rospy.init_node('move_tello')
        self.ask_move=rospy.Service('move', Move,self.position)
        print("Ready to move")
        self.ask_command=rospy.Service('command', Command, self.information)
        rospy.spin()


    def position(self,req):
        print("no wchodze")
        if req.x>0:
            self.drone.move_forward(req.x)
        if req.y > 0:
            self.drone.move_right(req.y)
        if req.z > 0:
            self.drone.move_up(req.z)
        if req.yaw > 0:
            self.drone.rotate_clockwise(req.yaw)
        return True

    def information(self,req):
        if req.message=='start':
            self.drone.connect()
            self.drone.streamon()
            sleep(1)
            resp=CommandResponse()
            resp.is_sent=True
            return resp
        if req.message == 'take_off':
            self.drone.takeoff()
            sleep(1)
            resp = CommandResponse()
            resp.is_sent = True
            return resp
        if req.message == 'land':
            self.drone.land()
            return True
        if req.message=='start_takeoff':
            self.drone.connect()
            self.drone.streamon()
            self.drone.takeoff()
            sleep(1)
            resp=CommandResponse()
            resp.is_sent=True
            return resp
if __name__ == "__main__":
    Motion()
