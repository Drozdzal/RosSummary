# ROS Services

Service is another way of communication which can be added to ROS node. 
In ROS1, services works synchronously. Let's say that t is stuck until the server responds (or fails).

Ros Service Client
---

There is 3 options to call service as a client:
1) Using prompt : <br />
You may do it using rosservice call "name of service" "request_message"
rosservice call /hardware_service 2
2) Using rqt

3) By asking ROSCORE and creating binding to the server. <br />
-check whether service is available -> rospy.wait_for_service("name_of_service")<br />
-make connection with serviceproxy -> rospy.ServiceProxy('name_of_service", "service") <br />
-create request message -> "service"Request()<br />
#Code example:


    import rospy
       from tescik_pierwszy_msgs.srv import hardware_connected, hardware_connectedRequest, hardware_connectedResponse
    
    class HardwareCheck():
        def __init__(self):
            print("I'm checking whether server is available")
            rospy.wait_for_service('hardware_service')
            print("Server is available")
            self.harware_server=rospy.ServiceProxy('hardware_service', hardware_connected)
    
        def ask_server(self):
            request=hardware_connectedRequest()
            request.test=5
            print(self.harware_server(request))
    
    
    if __name__ == '__main__':
        rospy.init_node("Ask_hardware")
        service_client=HardwareCheck()
        while 1:
            if int(input("will be asking serwer till you type 0")):
                service_client.ask_server()
---

All things which we need to create ros service is:
1) Creating node if it's not created yet
2) Defining ROSCORE to initialize server using rospy.Service()
3) At some moment in our code hold whole thread by using rospy.spin()

    
    
    import rospy
    from tescik_pierwszy_msgs.srv import hardware_connected, hardware_connectedRequest, hardware_connectedResponse
    
    class HardwareCheck():
        def __init__(self):
            self.harware_serwer=rospy.Service('hardware_service', hardware_connected,self.hardware_check)

        def hardware_check(self,request):
            print("Hardware is working")
            service_response=hardware_connectedResponse()
            service_response.is_hardware_working=True
            return service_response


    if __name__ == '__main__':
        rospy.init_node("Harware")
        serwer = HardwareCheck()
        rospy.spin()
