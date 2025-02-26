#design a class called Time
'''
data fields hour minute second
constructor
getters
setTime(elapseTime) >> determines elapsed time since previous

'''

import datetime

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def getHour(self):
        return self.hour

    def getMinute(self):
        return self.minute

    def getSecond(self):
        return self.second

    # // <-- integer devision
    def setTime(self, elapseTime):
        return "WIP"



