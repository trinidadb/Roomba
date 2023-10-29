import math

MAX_COUNT_ENCODER = 65536
COUNTS_IN_REVOLUTION = 508.8
WHEEL_DIAMETER = 72
WHEEL_DISTANCE = 235
COUNTS_IN_MM = COUNTS_IN_REVOLUTION/(math.pi*WHEEL_DIAMETER)

class Locate():

    def __init__(self):
        self.xPos = 0
        self.yPos = 0
        self.thetaRad = 0
        self.dist = 0
        self.leftEnc_old = 0
        self.rightEnc_old = 0
        self.firstRun = True

    def updatePosition(self, data):
        leftEnc = data.encoder_counts_left
        rightEnc = data.encoder_counts_right

        if self.firstRun:
            self.leftEnc_old, self.rightEnc_old = leftEnc, rightEnc
            self.firstRun = False
            return
        
        deltaLeft = self._getEncoderCountDelta(leftEnc, self.leftEnc_old)
        deltaRight = self._getEncoderCountDelta(rightEnc, self.rightEnc_oldEnc_old)

        distLeft = self._getDistanceFromCounts(deltaLeft) ##mm
        distRight = self._getDistanceFromCounts(deltaRight) ##mm

        avgDistance = (distLeft + distRight)/2
        deltaThetaRad = (distRight-distLeft)/WHEEL_DISTANCE
    
        # deltaThetaRad *= ANGULAR_ERROR
        self.thetaRad += deltaThetaRad
        
        if self.thetaRad > 2*math.pi:
            self.thetaRad -= 2*math.pi
        elif self.thetaRad < -2*math.pi:
            self.thetaRad += 2*math.pi

        self.xPos += avgDistance * math.cos(self.thetaRad)
        self.yPos += avgDistance * math.sin(self.thetaRad)

        self.leftEncoder_old = leftEnc
        self.rightEncoder_old = rightEnc        


    def _getEncoderCountDelta(self, newCount, oldCount):
        delta = newCount-oldCount
        thresholdRollOver = MAX_COUNT_ENCODER/2
        if delta< -thresholdRollOver:
            delta = (newCount + MAX_COUNT_ENCODER)-oldCount
        if delta> thresholdRollOver:
            delta = newCount-(oldCount+MAX_COUNT_ENCODER)
        return delta

    def _getDistanceFromCounts(self, counts):
        return counts * math.pi * WHEEL_DIAMETER * COUNTS_IN_REVOLUTION     