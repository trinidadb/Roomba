def setConnection(port="COM5"):
    bot = Create2(port)

    bot.start()
    bot.full()

    return bot

class Roomba:
    def __init__(self):
        self.is_driving = False
        self.is_rotating = False
        self.is_stopped = True

    def drive_forward(self):
        if not self.is_driving:
            print("Driving forward")
            # Implement the code to drive the robot forward here
            self.is_driving = True

    def rotate(self):
        if not self.is_rotating:
            print("Rotating")
            # Implement the code to rotate the robot here
            self.is_rotating = True

    def stop(self):
        if not self.is_stopped:
            print("Stopping")
            # Implement the code to stop the robot here
            self.is_driving = False
            self.is_rotating = False
            self.is_stopped = True