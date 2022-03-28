# ROS Actions

Action Server
---

To create action server firstly we need to import actionlib library, and created by us action messages.

Steps to do:
1) Creating node if it's not created yet
2) Defining ROSCORE to create a action_server with args : name of server, imported action, and function which will be executed during call-> rospy.Publisher("our_topic","type_of_msg",queue_size=10)
3) Rxecute_cb_closure is needed or you will not be able to add goal to receiving state.
4) During execute_cb_closure set new goal to True and envoke self.execute_cb
5) In self.execute_cb accept goal and do some tasks


    import rospy
    import actionlib
    from tescik_pierwszy_msgs.msg import move_servosGoal, move_servosAction, move_servosResult, move_servosFeedback
    
    class SimpleAction():
        _feedback = move_servosFeedback()
        _result = move_servosResult()
    
        def __init__(self, name):
            self._action_name = name
            print(self._action_name)
            def execute_cb_closure(goal):
                self._action_server.new_goal=True
                self.execute_cb(goal)
            self._action_server = actionlib.SimpleActionServer(self._action_name, move_servosAction,
                                                    execute_cb=execute_cb_closure, auto_start=False)
    
            self._action_server.start()
            print("Started action server")
            rospy.spin()
    
        def execute_cb(self, goal):
            print("received goal")
            self._action_server.accept_new_goal()
            print(goal)
            for i in range(1, goal.number_of_steps):
                # check that preempt has not been requested by the client
                print(f"left_arm={goal.servo_values.left_arm_servo}")
                print(f"right_arm={goal.servo_values.right_arm_servo}")
                print(f"head_arm={goal.servo_values.head_servo}")
                print(f"leg_servo={goal.servo_values.leg_servo}")
                print(f"right_servo={goal.servo_values.right_servo}")
                self._action_server.publish_feedback(move_servosFeedback(i))
    
            self._result.finished_move=True
            self._action_server.set_succeeded(self._result)
    
    if __name__ == '__main__':
        rospy.init_node("action_server")
        SimpleAction("move_servos")
        rospy.spin()

Action Client
---

Steps to do:
1) Creating node if it's not created yet
2) Defining ROSCORE to create a action_client with args : name of server, imported action
3) Create goal message which will be sent by envoking move_servosGoal
4) Send goal and wait for response. Examples of responses:
- returned 2 -> GOAL PREMPTEED
- returned 3 -> GOAL SUCCESS
- returned 4 -> GOAL ABORTED


    import rospy
    import actionlib
    import actionlib_tutorials.msg
    from tescik_pierwszy_msgs.msg import move_servosGoal, move_servosAction, move_servosResult, move_servosFeedback
    from tescik_pierwszy_msgs.msg import humanoid_servos
    
    def send_on_action():
        rospy.init_node('action_client')
        client_ = actionlib.SimpleActionClient('move_servos', move_servosAction)
        client_.wait_for_server()
        goal = move_servosGoal()
        goal.number_of_steps= 8
        servo_val=humanoid_servos()
        servo_val.left_arm_servo=2
        servo_val.right_arm_servo = 2
        servo_val.head_servo = 2
        servo_val.leg_servo = 2
        servo_val.right_servo = 2
        goal.servo_values=servo_val
        result=client_.send_goal_and_wait(goal)
        print("Sent goal")
        print(result)
    
    if __name__ == "__main__":
        send_on_action()
    



