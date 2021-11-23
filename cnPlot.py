from PyQt5.QtWidgets import QApplication,QVBoxLayout, QPushButton,QWidget
from PyQt5.QtCore import QTimer , QDateTime
import time
import numpy as np

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
XMAX = 500
XPREC = 0.5
class cnPlot():
    def __init__(self):

        #Create Matplotlib figure and canvas
        self.fig = Figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.canvas = FigureCanvasQTAgg(self.fig)
        self.xplot = np.array(0)
        self.yplot = np.array(0)
        self.time = None
        self.xprev = 0
    def add_point(self, point):
        x = float(point[0])
        y = float(point[1])
        if abs(x-self.xprev) >= XPREC:
            self.xplot = np.append(self.xplot,x)
            self.yplot = np.append(self.yplot,y)
            self.xprev = x
        now = time.time()
        if self.time == None:
            self.time = now
        elif now > self.time + 2:
            self.ax.plot(self.xplot,self.yplot,'r')
            self.fig.canvas.draw()
            self.time = now
            print(self.yplot)

