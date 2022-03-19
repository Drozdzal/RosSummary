from xmlrpclib import ServerProxy
import os
master = ServerProxy(os.environ['ROS_MASTER_URI'])
master.getSystemState('/')

from xmlrpclib import ServerProxy
import os
ps = ServerProxy(os.environ['ROS_MASTER_URI'])
ps.getParam('/','name of param')