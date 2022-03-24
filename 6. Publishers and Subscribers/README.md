# Publishers and Subscribers
To familarize yourself with ROS, I think that it will be the best to use language which you know the best.
You may write you're code in different languages. Howevever, I will write code in Python because this language will enable me to present it most clearly.
Subscribing a topic works in background of the code. We're just going into callback function when we receive messages.
Publishers can send message whenever they want. 

Publisher
---

As it was said before ros creates nodes. Each node can communicate with each other using topics, services or actions.
In node we can PUBLISH messages on some topic. we 

Steps to do:
1) Creating node if it's not created yet
2) Defining ROSCORE to create a topic which this publisher will be sending on by typing -> rospy.Publisher("our_topic","type_of_msg",queue_size=10)
3) Define rosp.Rate(val) -> value in Hz
4) Create while in which node will be checking whether roscore is finished or not
5) Send data on topic using publisher method which takes message as an argument-> publisher.publish(message)


#Example code
    import rospy
    from tescik_pierwszy_msgs.msg import humanoid_servos
    
    class Publisher():
        def __init__(self):
            self.publisher=rospy.Publisher("our_topic",humanoid_servos,queue_size=10)
            self.rate = rospy.Rate(1)
            while 1:
                self.rate.sleep()
                message=humanoid_servos()
                message.left_arm_servo=1
                message.right_arm_servo=1
                message.head_servo=1
                message.leg_servo=1
                message.right_servo=2
                self.publisher.publish(message)
    
    
    if __name__ == '__main__':
        rospy.init_node("Harware")
        Publisher()


Subscriber
---

Okay we've created one node which is sending data on topic. But what can we do with this data?
Each node can subscribe a topic. This means that each time when the data will be send on topic our node will receive this data and execute something which we've
told it to do in our callback function. Code bellow will be written as an object. When we want to use callback functions in classes we have to write callback closures or we will get an error.

Steps to do:
1) Creating node if it's not created yet
2) Make subcription to topic using : rospy.Subscriber('our_topic', humanoid_servos, self.move_servo)
3) Define callback fuction which will be executed each time when message is sent on topic.

#Example code:
    import rospy
    from tescik_pierwszy_msgs.msg import humanoid_servos
    
    class Subscriber():
            def __init__(self):
                rospy.init_node('img_sub')
                def move_servo_closur(message):
                    self.move_servo(message)
                rospy.Subscriber('our_topic', humanoid_servos, self.move_servo)
                self.move_finished = True
                rospy.spin()
    
            def move_servo(self,message):
                print(f"left_arm={message.left_arm_servo  }")
                print(f"right_arm={message.right_arm_servo}")
                print(f"head_arm={message.head_servo }")
                print(f"leg_servo={message.leg_servo}")
                print(f"right_servo={message.right_servo}")
    
    
    
    if __name__ == "__main__":
        Subscriber()


