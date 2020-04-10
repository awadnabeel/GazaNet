import os

class Ping:

    def __init__(self,host):
        response = os.system("ping  " + host)
        if response == 0 :
            self.isReachable = True
        else :
            self.isReachable =  False

    def isReachable(self):
        return self.isReachable