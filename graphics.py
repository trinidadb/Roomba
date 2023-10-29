
import matplotlib.pyplot as plt 
import numpy as np

class PlotHistory:

    X_SERIE = []
    MULTI_Y_SERIES = {"xPos":[], "yPos":[], "thetaRad": []}

    def addValuesToPlot(self, xSerie, ySeries):
        PlotHistory.X_SERIE.append(xSerie)

        PlotHistory.MULTI_Y_SERIES["xPos"].append(ySeries[0])
        PlotHistory.MULTI_Y_SERIES["yPos"].append(ySeries[1])
        PlotHistory.MULTI_Y_SERIES["thetaRad"].append(ySeries[2])
        
    def plot(self):
        # Initialise the subplot function using number of rows and columns 
        figure, axis = plt.subplots(1, 3) 
        
        time = np.array(PlotHistory.X_SERIE) - PlotHistory.X_SERIE[0]
        x_position_m = np.array(PlotHistory.MULTI_Y_SERIES["xPos"]) / 1000
        y_position_m = np.array(PlotHistory.MULTI_Y_SERIES["yPos"]) / 1000
        theta_deg = np.rad2deg(np.array(PlotHistory.MULTI_Y_SERIES["thetaRad"]))

        axis[0].plot(time, x_position_m)
        axis[1].plot(time, y_position_m)
        axis[2].plot(time, theta_deg)

        axis[0].set_title("X Postion (m)") 
        axis[1].set_title("Y Postion (m)")
        axis[2].set_title("Theta (deg)")   
        
        # Combine all the operations and display 
        plt.show() 