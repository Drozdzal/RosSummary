# Publishers and Subscribers
To familarize yourself with ROS, I think that it will be the best to use language which you know the best.
You may write you're code in different languages. Howevever, I will write code in Python because this language will enable me to present it most clearly.
Subscribing a topic works in background of the code. We're just going into callback function when we receive messages.
Publishers can send message whenever they want. 

Publisher
---

As it was said before ros creates nodes. Each node can communicate with each other using topics, services or actions.
In node we can PUBLISH messages on some topic. we 

    #Importing ros library. This library enables us to create nodes, adding publishers, subscribers, services ect
    import rospy
    #This import allows us to send Image message, there isnt image message in ros msgs this is why we have to import it 
    from sensor_msgs.msg import Image
    #If you want to work with images remeber to firstly import cv2 then cv_brige or you man encourage an error.
    import cv2
    from cv_bridge import CvBridge, CvBridgeError
        def image_publisher():
            # HERE IS SOME CODE WHICH ALLOWS TO SEND IMAGE MESSAGES
            vid = VideoCapture()
            bridge = CvBridge()

            #Here we initializing NODE. If we want to add publishers, subscribers or service servers or cliencts etc we firstly have to create a node.
            rospy.init_node('rpicam_pub', anonymous=True)

            # Here we're saying to ROSCORE create rpicam topic, this topic wants Image msg and we allow 10 queue_size 
            pub = rospy.Publisher('rpicam', Image, queue_size=10)

            #ROS enables to say how long will sleep take. Here we're saying that if rate.sleep() will be typed it will wait 1 sec
            rate = rospy.Rate(1)  # 1Hz
    
        
            while not rospy.is_shutdown():
                frame = vid.read()
                ros_frame=bridge.cv2_to_imgmsg(frame)
                #Publisher object will send a messages ros_frame
                pub.publish(ros_frame)

                # Node waits time specified in rospy.Rate(x)
                rate.sleep()
        
        
        if __name__ == '__main__':
            try:
                image_publisher()
            except rospy.ROSInterruptException:
                pass


Subscriber
---

Okay we've created one node which is sending data on topic. But what can we do with this data?
Each node can subscribe a topic. This means that each time when the data will be send on topic our node will receive this data and execute something which we've
told it to do in our callback function. Code bellow will be written as an object. When we want to use callback functions in classes we have to write callback closures or we will get an error.

        
    class Controller:
        def __init__(self):
            self.bridge = CvBridge()
            self.move_finished = True
            
            #This callback fuction is needed due to the fact that methods take self args
            def img_callback_closure(img_msg):
                self.img_callback(img_msg)
            
            # OUR NODE SUBSCRIBES TO rpicam topic, Image -> message which is being sent by this topic, last arg is callback function which will be executed while receiving message
            rospy.Subscriber('rpicam', Image, img_callback_closure)
            
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

            rospy.init_node('img_sub')
            Controller()
            rospy.spin()

