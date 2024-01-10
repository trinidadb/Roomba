from pycreate2 import Create2
import time
import math

class Roomba():
    BOT = None
    SPEED = 200 #mm/s

    def __init__(self, port="COM5"):
        if Roomba.BOT==None:
            Roomba.BOT = self._setConnection(port)

    def _setConnection(self, port):
        bot = Create2(port)

        bot.start()
        bot.full()

        return bot
    
    def playSong(self):
        songNum = 0
        song = [76, 12, 76, 12, 20, 12, 76, 12, 20, 12, 72, 12, 76, 12, 20, 12, 79, 12, 20, 36, 67, 12, 20, 36]
        Roomba.BOT.createSong(songNum, song)
        time.sleep(0.1)
        how_long = Roomba.BOT.playSong(songNum)
        time.sleep(how_long)

class RoombaMovements(Roomba):

    def __init__(self, bot):
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
        time.sleep(0.47)
        RoombaMovements.BOT.drive_stop()