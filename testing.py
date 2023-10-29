import keyboard
from roomba import Roomba
from actionCoordination import Actuate
from location import Locate
import time

def getSensorData(bot):
    data = bot.get_sensors()
    Actuate(bot, data).response()
    #Locate(data)


def main():

    #Stop routine logic
    routine_running = True
    def stop_routine():
        nonlocal routine_running
        routine_running = False
    keyboard.add_hotkey('q', stop_routine)

    #Set connection
    bot = Roomba(port="COM5").BOT

    while routine_running:
        getSensorData(bot)

    bot.drive_stop()
    bot.close()

#main()

def simple():
    #Stop routine logic
    routine_running = True
    def stop_routine():
        nonlocal routine_running
        routine_running = False
    keyboard.add_hotkey('q', stop_routine)

    #Set connection
    bot = Roomba(port="COM7").BOT

    first = False
    bot.drive_direct(20,20)
    while routine_running:
        data = bot.get_sensors()
        if not first:
            first = data.encoder_counts_left
        last=data.encoder_counts_left

    print(first)
    print(last)

    bot.drive_stop()
    bot.close()


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


def rotate():
    bot = Roomba(port="COM7").BOT

    angle = 360
    speed=100
    rad = 72/2

    # bot.drive_direct(300,-300)
    # time.sleep(2.2)
    # print(time_to_spin)
    # bot.drive_stop()
    turn_angle = 0.0

    if angle > 0:
        cmd = (speed, -speed)  # R, L
    else:
        cmd = (-speed, speed)
        angle = -angle

    firstL = False
    firstR = False
    while abs(turn_angle) < angle:
        bot.drive_direct(*cmd)
        sensors = bot.get_sensors()
        turn_angle += sensors.angle  # roomba only tracks the delta angle
        if not firstL:
            firstL = sensors.encoder_counts_left
            firstR = sensors.encoder_counts_right
        lastL=sensors.encoder_counts_left
        lastR=sensors.encoder_counts_right

    print(f"Left: {firstL}, {lastL}. Diff {lastL-firstL}")
    print(f"Right: {firstR}, {lastR}. Diff {lastR-firstR}")


    bot.drive_direct(0, 0)   

    bot.close()

rotate()    

#6.45seg 100mm/s