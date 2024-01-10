
import matplotlib.pyplot as plt 
import numpy as np

TIME = []
X_POS = []
Y_POS = []
THETA_RAD = []

plt.ion()  # Turn on interactive mode for Matplotlib
fig, (ax1, ax2) = plt.subplots(1, 2)

def _preProcess(time_s, x_mm, y_mm, theta_rad):
    time = np.array(TIME) - TIME[0]
    x_position_m = np.array(X_POS) / 1000
    y_position_m = np.array(Y_POS) / 1000
    theta_deg = np.rad2deg(np.array(THETA_RAD))
    return time, x_position_m, y_position_m, theta_deg

class Plot:

    @staticmethod
    def addValuesToPlot(time_s, x_mm, y_mm, theta_rad):
        TIME.append(time_s)
        X_POS.append(x_mm)
        Y_POS.append(y_mm)
        THETA_RAD.append(theta_rad)

    @staticmethod    
    def plotHistoric():
        figure, (ax1, ax2) = plt.subplots(1,2) 
        
        time, x_position_m, y_position_m, theta_deg = _preProcess(TIME, X_POS, Y_POS, THETA_RAD)

        ax1.plot(x_position_m, y_position_m, marker='o')
        ax1.set_xlabel('X Position (m)')
        ax1.set_ylabel('Y Position (m)')
        ax1.set_title('Roomba Movement')

        ax2.plot(time, theta_deg, 'r', marker='o')  # 'ro' specifies a red circle marker at the specified angle
        ax2.set_xlabel('Time (sec)')
        ax2.set_ylabel('Angle (°)')        
        ax2.set_title('Roomba Angle')

        plt.show() 

    @staticmethod 
    def plotRealTime():
        global fig, ax1, ax2
        
        time, x_position_m, y_position_m, theta_deg = _preProcess(TIME, X_POS, Y_POS, THETA_RAD)

        ax1.clear()
        ax1.plot(x_position_m, y_position_m, marker='o')
        ax1.set_xlabel('X Position (m)')
        ax1.set_ylabel('Y Position (m)')
        ax1.set_title('Roomba Movement')

        ax2.clear()
        ax2.plot(time[-20:], theta_deg[-20:], 'r', marker='o')  # 'ro' specifies a red circle marker at the specified angle
        ax2.set_xlabel('Time (sec)')
        ax2.set_ylabel('Angle (°)')        
        ax2.set_title('Roomba Angle')   

        plt.pause(0.01)
