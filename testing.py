import keyboard
from roomba import Roomba
from actionCoordination import Actuate
from location import Locate
from graphics import PlotHistory
import time

def getSensorData(bot, locationObj, plotHist=False):
    data = bot.get_sensors()
    sampleTime = time.time()
    Actuate(bot, data).response()
    locationObj.updatePosition(data)
    PlotHistory().addValuesToPlot(sampleTime, [locationObj.xPos, locationObj.yPos, locationObj.thetaRad])


def main(plotHist=False):

    #Stop routine logic
    routine_running = True
    def stop_routine():
        nonlocal routine_running
        routine_running = False
    keyboard.add_hotkey('q', stop_routine)

    #Set connection
    bot = Roomba(port="COM7").BOT

    location = Locate()

    while routine_running:
        getSensorData(bot, location, plotHist=plotHist)

    bot.drive_stop()
    bot.close()

    if plotHist:
        PlotHistory().plot()


main(plotHist=True)

def simple():
    
    bot = Roomba(port="COM7").BOT

    bot.drive_stop()
    bot.close()

#simple()

def outOfProgrammingMode():
    bot = Roomba(port="COM7").BOT
    try:
    # Start the connection
        bot.start()
        time.sleep(2)  # Give the Roomba time to initialize

        # Send the 'start' command to exit programming mode and enter normal mode
        bot.start()

    finally:
        bot.close()  # Close the connection

