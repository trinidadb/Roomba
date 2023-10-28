import keyboard
from interruption import interrupt_seconds
from roomba import Roomba
from sensorData import Actuate
import time

@interrupt_seconds(0.05)
def getSensorData(bot):
    data = bot.get_sensors()
    Actuate(bot, data).response()


def main():

    #Stop routine logic
    routine_running = True
    def stop_routine():
        nonlocal routine_running
        routine_running = False
    keyboard.add_hotkey('q', stop_routine)

    #Set connection
    bot = Roomba(port="COM7").BOT

    while routine_running:
        getSensorData(bot)

    bot.close()

main()

# def rotate():
#     bot = Roomba(port="COM7").BOT

#     angle = 90
#     speed=100
#     rad = 72/2
#     time_to_spin = (abs(angle) / (360*speed/ (speed*rad)))

#     # bot.drive_direct(300,-300)
#     # time.sleep(2.2)
#     # print(time_to_spin)
#     # bot.drive_stop()
#     turn_angle = 0.0

#     if angle > 0:
#         cmd = (speed, -speed)  # R, L
#     else:
#         cmd = (-speed, speed)
#         angle = -angle

#     while abs(turn_angle) < angle:
#         bot.drive_direct(*cmd)
#         sensors = bot.get_sensors()
#         turn_angle += sensors.angle  # roomba only tracks the delta angle

#     bot.drive_direct(0, 0)   

#     bot.close()

# rotate()    

#6.45seg 100mm/s