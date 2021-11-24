from PyQt5.QtWidgets import QApplication,QVBoxLayout, QPushButton,QWidget
from PyQt5.QtCore import QTimer , QDateTime
import time
import numpy as np

from matplotlib.figure import Figure
import  matplotlib.pyplot   as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
XMAX = 500
XYPREC = 0.3
ZUPREC = 0.3
class cnPlot():
    def __init__(self):

        #Create Matplotlib figure and canvas
        self.fig, (self.ax1,self.ax2)  = plt.subplots(2)
        self.canvas = FigureCanvasQTAgg(self.fig)
        # set the limits

        self.ax1.set_xlim([0, XMAX])
        self.ax1.set_ylim([-XMAX/8, XMAX/8])
        self.ax2.set_xlim([0, XMAX])
        self.ax2.set_ylim([-XMAX/8, XMAX/8])

        self.xplot = np.array(0)
        self.yplot = np.array(0)
        self.uplot = np.array(0)
        self.zplot = np.array(0)


        self.time = None
        self.xprev = 0
        self.yprev = 0
        self.uprev = 0
        self.zprev = 0

    def add_point(self, point):
        x = float(point[0])
        y = float(point[1])
        z = float(point[2])
        u = float(point[3])
        if abs(x-self.xprev) >= XYPREC or abs(y-self.yprev) >= XYPREC:
            self.xplot = np.append(self.xplot,x)
            self.yplot = np.append(self.yplot,y)
            self.xprev = x
            self.yprev = y
        if abs(z-self.zprev) >= ZUPREC or abs(u-self.uprev) >= ZUPREC:
            self.zplot = np.append(self.zplot,z)
            self.uplot = np.append(self.uplot,u)
            self.zprev = z
            self.uprev = u
        now = time.time()
        if self.time == None:
            self.time = now
        elif now > self.time + 1:
            self.ax1.plot(self.xplot,self.yplot,'r')
            self.ax2.plot(self.uplot,self.zplot,'r')
            self.fig.canvas.draw()
            self.time = now

