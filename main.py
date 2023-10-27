import keyboard
from interruption import interrupt_seconds
from roomba import setConnection

@interrupt_seconds(0.05)
def getSensorData(bot):
    #data = bot.get_sensors()
    pass

def main():

    #Stop routine logic
    routine_running = True
    def stop_routine():
        nonlocal routine_running
        routine_running = False
    keyboard.add_hotkey('q', stop_routine)

    bot = setConnection("COM5")

    while routine_running:
        getSensorData(bot)

main()