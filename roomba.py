from pycreate2 import Create2
import time
import math

class Roomba():
    BOT = None
    SPEED = 100 #mm/s
    WHEEL_DIAMETER = 72 #mm

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

    def reverse(self):
        #NO SENSE FOR 0.2
        RoombaMovements.BOT.drive_direct(RoombaMovements.SPEED*(-1),RoombaMovements.SPEED)
        time.sleep(0.2)
        RoombaMovements.BOT.drive_stop()

    def stop(self):
        RoombaMovements.BOT.drive_stop()

    def rotate(self, direction="right", angle=90):
        dir_right = -1 if direction=="right" else 1
        dir_left = dir_right * (-1)

        time_to_spin = (abs(angle) / (360*RoombaMovements.SPEED/ (2*math.pi*RoombaMovements.WHEEL_DIAMETER/2)))

        RoombaMovements.BOT.drive_direct(dir_right*RoombaMovements.SPEED,dir_left*RoombaMovements.SPEED)
        time.sleep(time_to_spin)
        RoombaMovements.BOT.drive_stop()

    def forward(self):
        RoombaMovements.BOT.drive_direct(RoombaMovements.SPEED,RoombaMovements.SPEED)

