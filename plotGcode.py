import numpy as np
from PyQt5 import QtCore, QtWidgets, uic, QtChart,QtGui

import time
import random

XMAX = 500
DMIN = 1
class plotGcode():

    def __init__(self, widget):
        self.widget = widget
        self.n_axis = 0
        self.axis_values = np.empty(0)
        self.axis_names = []
        self.pos = 0
        self.xplot = np.array(0)
        self.yplot = np.array(0)
        self.yplot = np.array(0)
        self.uplot = np.array(0)
        self.zplot = np.array(0)
        self.xprv_p = 0
        self.uprv_p = 0

        self.chart = QtChart.QChart()

        #self.xy_serie = QtChart.QScatterSeries()
        #self.xy_serie.setMarkerSize(5.0)
        self.xy_base_serie = QtChart.QLineSeries()
        self.xy_serie = QtChart.QLineSeries()
        self.xy_base_serie.setColor(QtGui.QColor("cyan"))
        self.xy_serie.setColor(QtGui.QColor("red"))

        self.uz_serie = QtChart.QLineSeries()


        self.chart.addSeries(self.xy_base_serie)
        self.chart.addSeries(self.xy_serie)
        self.chart.addSeries(self.uz_serie)



        self.chart.createDefaultAxes()
        self.chart.legend().hide()

        #self.chart.axisX(self.ma5).setVisible(False)

        # self.chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)

        self.chartview = QtChart.QChartView(self.chart)
        # self.chart_container.setContentsMargins(0, 0, 0, 0)
        # lay = QtWidgets.QHBoxLayout(self.chart_container)

        lay = QtWidgets.QHBoxLayout(widget)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.chartview)


    def load_gcode_file(self, filename):
        self.read_file(filename)
        self.set_limits()
        self.filter_by_dist()

    def read_file(self,filename):
        with open(filename,"r") as f:
            for line in f:
                fields = line.split(' ')
                if fields[0] != "G1":
                    continue
                print(len(fields))
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
                    print(self.axis_names)
                    print(row)
                self.axis_names = names
                self.axis_values = np.append(self.axis_values,[row],axis=0)
            print(self.axis_values)
            print(self.axis_values.shape)
            self.xmax = np.max(self.axis_values[:,0])
            self.ymax = np.max(self.axis_values[:,1])
            self.n = len(self.axis_values)
            self.set_limits()

    def __distance(self,a0,a1):
        d = a1 - a0
        return np.sqrt(np.sum( d * d))

    def filter_by_dist(self):
         self.filter_axe_dist(self.axis_values[:, [0, 1]], self.xy_serie)
         self.filter_axe_dist(self.axis_values[:, [2, 3]], self.uz_serie)

    def filter_axe_dist(self, xy_values, serie):
        serie.clear()
        xpos_2_plot = [0]
        for i, p in enumerate(xy_values):
            dist = self.__distance(p, xy_values[self.xprv_p-1])
            if dist > DMIN:
                self.xprv_p = i
                xpos_2_plot.append(i)
                self.xy_base_serie.append(QtCore.QPointF(p[0],p[1]))

        xy_filtered = xy_values[xpos_2_plot,:]
        print(f"{xy_values.shape}{xy_filtered.shape}")

    def add_point_fake(self):
        t0 = time.time()
        p = self.axis_values[self.pos, [0, 1]]
        self.pos += 1
        self.pos = self.pos % self.n
        self.xy_serie.append(QtCore.QPointF(p[0], p[1]))
        t1 = time.time()
        print(t0-t1)
    def add_point(self,p):
        self.xy_serie.append(QtCore.QPointF(p[0],p[1]))
    def set_limits(self):
        widget_w = self.widget.width()
        widget_h = self.widget.height()
        print(f"{widget_w} x {widget_h}")
        x_min = -10
        x_max = self.xmax
        y_min = -10
        y_max = self.xmax *(  widget_h / widget_w)
        self.chart.axisX(self.xy_serie).setMin(x_min)
        self.chart.axisX(self.xy_serie).setMax(x_max)
        self.chart.axisY(self.xy_serie).setMin(y_min)
        self.chart.axisY(self.xy_serie).setMax(y_max)










