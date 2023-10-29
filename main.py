import keyboard
from roomba import Roomba
from actionCoordination import Actuate
from location import Locate


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

main()


