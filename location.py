import math
import numpy as np

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
        self.leftEnc_old = None
        self.rightEnc_old = None

    def updatePosition(self, data):
        leftEnc = data.encoder_counts_left
        rightEnc = data.encoder_counts_right

        if not (self.leftEnc_old or self.rightEnc_old):
            self.leftEnc_old, self.rightEnc_old = leftEnc, rightEnc
            return
        
        deltaLeft = self._getEncoderCountDelta(leftEnc, self.leftEnc_old)
        deltaRight = self._getEncoderCountDelta(rightEnc, self.rightEnc_old)

        distLeft = self._getDistanceFromCounts(deltaLeft) ##mm
        distRight = self._getDistanceFromCounts(deltaRight) ##mm

        avgDistance = (distLeft + distRight)/2
        avgDistance = avgDistance if abs(avgDistance)>2 else 0
        factorDeCorreccionDist = 0.6/0.53 #Se lo encontro experimentalmente
        avgDistance *= factorDeCorreccionDist

        deltaThetaRad = (distRight-distLeft)/WHEEL_DISTANCE
        factorDeCorreccionAngular = 360/329 #364/320 #Se lo encontro experimentalmente
        self.thetaRad += (deltaThetaRad* factorDeCorreccionAngular)

        self.thetaRad = self.thetaRad if abs(self.thetaRad)>0.7 else 0

        if self.thetaRad > 2*math.pi:
            self.thetaRad -= 2*math.pi
        elif self.thetaRad < -2*math.pi:
            self.thetaRad += 2*math.pi         

        self.xPos += avgDistance * math.cos(self.thetaRad)
        self.yPos += avgDistance * math.sin(self.thetaRad)

        self.leftEnc_old = leftEnc
        self.rightEnc_old = rightEnc        

    def _getEncoderCountDelta(self, newCount, oldCount):
        delta = newCount-oldCount
        thresholdRollOver = MAX_COUNT_ENCODER/2
        if delta< -thresholdRollOver:
            delta = (newCount + MAX_COUNT_ENCODER)-oldCount
        if delta> thresholdRollOver:
            delta = newCount-(oldCount+MAX_COUNT_ENCODER)
        return delta

    def _getDistanceFromCounts(self, counts):
        return counts * math.pi * WHEEL_DIAMETER / COUNTS_IN_REVOLUTION     