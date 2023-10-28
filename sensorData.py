import time

class Actuate():

    BEHAVIOURS = None

    def __init__(self, bot, data):
        if Actuate.BEHAVIOURS==None:
            Actuate.BEHAVIOURS = RoombaMovements(bot)
        self.data = data
        self.newDirection = None            

    def response(self):
        if self._detect_wheelDrop():
            Actuate.BEHAVIOURS.stop()        
        elif self._detect_cliff():
            Actuate.BEHAVIOURS.reverse()
            Actuate.BEHAVIOURS.rotate()
        elif self._detect_hardBump():
            if self.newDirection=="reverse":
                Actuate.BEHAVIOURS.reverse()
                Actuate.BEHAVIOURS.rotate()
            else:    
                Actuate.BEHAVIOURS.rotate(self.newDirection)
        elif self._detect_lightBump():
            Actuate.BEHAVIOURS.rotate()
        else:
            Actuate.BEHAVIOURS.forward()

    def _detect_cliff(self):
        return self.data.cliff_left or self.data.cliff_front_left or self.data.cliff_front_right or self.data.cliff_right
    
    def _detect_wheelDrop(self):
        return self.data.bumps_wheeldrops.wheeldrop_left or self.data.bumps_wheeldrops.wheeldrop_right
    
    def _detect_lightBump(self):
        bump = self.data.light_bumper
        return bump.left or bump.front_left or bump.center_left or bump.center_right or bump.front_right or bump.right
    
    def _detect_hardBump(self):
        left = self.data.bumps_wheeldrops.bump_left 
        right = self.data.bumps_wheeldrops.bump_right

        self.newDirection = "reverse" if (right and left) else ("right" if right else "left")

        return left or right