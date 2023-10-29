from pycreate2 import Create2
import time
import math

class Roomba():
    BOT = None
    SPEED = 200 #mm/s

    def __init__(self, port="COM5"):
        if Roomba.BOT==None:
            Roomba.BOT = self._setConnection(port)

    @staticmethod
    def _setConnection(port):
        bot = Create2(port)

        bot.start()
        bot.full()

        return bot

class RoombaMovements(Roomba):

    def __init__(self, bot):
        if RoombaMovements.BOT==None:
            RoombaMovements.BOT = bot

    def forward(self):
        RoombaMovements.BOT.drive_direct(RoombaMovements.SPEED,RoombaMovements.SPEED)

    def stop(self):
        RoombaMovements.BOT.drive_stop()    

    def reverse(self):
        RoombaMovements.BOT.drive_direct(RoombaMovements.SPEED*(-1),RoombaMovements.SPEED)
        time.sleep(0.2) #NO SENSE FOR 0.2
        RoombaMovements.BOT.drive_stop()

    def rotate(self, direction="right"):
        dir_right = -1 if direction=="right" else 1
        dir_left = dir_right * (-1)

        RoombaMovements.BOT.drive_direct(dir_right*RoombaMovements.SPEED,dir_left*RoombaMovements.SPEED)
        time.sleep(0.35)
        RoombaMovements.BOT.drive_stop()

    def rotateAngleDegrees(angle=90):
        ''' To rotate 360° the encoder counts should be around 1578 +/-10'''
        if RoombaMovements.SPEED>210:
            print("For this speed the function is disabled. The error when setting the angle is too big")
            RoombaMovements.BOT.drive_stop()
            return
        
        cmd = (RoombaMovements.SPEED, -RoombaMovements.SPEED) if angle > 0 else (-RoombaMovements.SPEED, RoombaMovements.SPEED)
        turn_angle = 0
        while abs(turn_angle) < abs(angle):
            RoombaMovements.BOT.drive_direct(*cmd)
            data = RoombaMovements.BOT.get_sensors()
            turn_angle += data.angle  # roomba only tracks the delta angle

        RoombaMovements.BOT.drive_stop()   

