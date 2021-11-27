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
        self.xmax= XMAX
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
        self.n_axis = 0
        self.axis_names = []
        self.axis_values = np.empty(0)

    def plot_axis(self):
        self.ax1.cla()
        self.ax2.cla()
        self.ax1.set_xlim([-10, self.xmax])
        self.ax1.set_ylim([-10, self.xmax/4])
        self.ax2.set_xlim([-10, self.xmax])
        self.ax2.set_ylim([-10, self.xmax/4])
        a = self.axis_values
        self.xplot = a[:,0]
        self.yplot = a[:,1]
        self.uplot = a[:,2]
        self.zplot = a[:,3]
        self.ax1.plot(self.xplot,self.yplot,'g')
        self.ax2.plot(self.uplot,self.zplot,'g')
        self.fig.canvas.draw()
    def load_gcode_file(self,filename):
        print(f"load gcode {filename}")
        self.n_axis = 0
        self.axis_names = []
        self.axis_values = np.empty(0)
        with open(filename,"r") as f:
            for line in f:
                fields = line.split(' ')
                if fields[0] != "G1":
                    continue
                if (len(fields) - 1 ) /2 > self.n_axis:
                    self.n_axis = int ( (len(fields) - 1 ) /2 )
                print(self.n_axis)
                if np.size(self.axis_values) == 0:
                    self.axis_values = np.empty((0,self.n_axis),float)
                row = []
                names = []
                for ax in range(1,self.n_axis+1):
                    pos = ax * 2
                    names.append(fields[pos - 1])
                    row.append( float(fields[pos ] ))
                self.axis_names = names
                self.axis_values = np.append(self.axis_values,[row],axis=0)
        print(self.axis_values.shape)
        print(self.axis_values[:,0].max())
        print(self.axis_values[:,2].max())
        self.xmax = max(self.axis_values[:,0].max(),self.axis_values[:,2].max())
        print(self.xmax)
        self.plot_axis()
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
        self.fig.canvas.draw()
