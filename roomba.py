from pycreate2 import Create2

class Roomba():
    BOT = None
    VELOCITY = 300

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
        RoombaMovements.BOT.drive_direct(RoombaMovements.VELOCITY*(-1),RoombaMovements.VELOCITY)
        time.sleep(0.2)
        RoombaMovements.BOT.drive_stop()

    def stop(self):
        RoombaMovements.BOT.drive_stop()

    def rotate(self, direction="right"):
        dir_right = -1 if direction=="right" else 1
        dir_left = dir_right * (-1)
        RoombaMovements.BOT.drive_direct(dir_right*RoombaMovements.VELOCITY,dir_left*RoombaMovements.VELOCITY)
        time.sleep(0.5)
        RoombaMovements.BOT.drive_stop()

    def forward(self):
        RoombaMovements.BOT.drive_direct(RoombaMovements.VELOCITY,RoombaMovements.VELOCITY)

