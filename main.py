import keyboard
from roomba import Roomba
from actionCoordination import Actuate
from location import Locate
from graphics import PlotHistory
import time


def getSensorData(bot, locationObj, plotHist=True):
    data = bot.get_sensors()
    sampleTime = time.time()
    Actuate(bot, data).response()
    locationObj.updatePosition(data)
    PlotHistory().addValuesToPlot(sampleTime, [locationObj.xPos, locationObj.yPos, locationObj.thetaRad])


def main(plotHist=True):

    #Stop routine logic
    routine_running = True
    def stop_routine():
        nonlocal routine_running
        routine_running = False
    keyboard.add_hotkey('q', stop_routine)

    #Set connection
    bot = Roomba(port="COM7").BOT
    locationObj = Locate()

    while routine_running:
        getSensorData(bot, locationObj, plotHist=plotHist)

    bot.drive_stop()
    bot.close()

    if plotHist:
        PlotHistory().plot()

main()


