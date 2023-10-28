import keyboard
from interruption import interrupt_seconds
from roomba import setConnection
from sensorData import Actuate, Roomba

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