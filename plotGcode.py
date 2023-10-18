from  cn5X_config import CONFIG_QTCHART_ENABLED

import numpy as np
import time
from PyQt5 import QtCore, QtWidgets, uic,QtGui
if CONFIG_QTCHART_ENABLED:
    from PyQt5 import QtChart

XMAX = 500
DMIN = 4
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
        if CONFIG_QTCHART_ENABLED:
            self.chart_xy = QtChart.QChart()
            self.chart_uz = QtChart.QChart()

            #self.xy_serie = QtChart.QScatterSeries()
            #self.xy_serie.setMarkerSize(5.0)
            self.xy_base_serie = QtChart.QLineSeries()
            self.xy_serie = QtChart.QLineSeries()
            self.xy_base_serie.setColor(QtGui.QColor("cyan"))
            self.xy_serie.setColor(QtGui.QColor("red"))

            self.uz_base_serie = QtChart.QLineSeries()
            self.uz_serie = QtChart.QLineSeries()
            self.uz_base_serie.setColor(QtGui.QColor("cyan"))
            self.uz_serie.setColor(QtGui.QColor("red"))


            self.chart_xy.addSeries(self.xy_base_serie)
            self.chart_xy.addSeries(self.xy_serie)
            self.chart_uz.addSeries(self.uz_base_serie)
            self.chart_uz.addSeries(self.uz_serie)

            self.chart_xy.createDefaultAxes()
            self.chart_uz.createDefaultAxes()
            self.chart_xy.legend().hide()
            self.chart_uz.legend().hide()


            # self.chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)

            self.chartview_xy = QtChart.QChartView(self.chart_xy)
            self.chartview_uz = QtChart.QChartView(self.chart_uz)

            # self.chart_container.setContentsMargins(0, 0, 0, 0)
            # lay = QtWidgets.QHBoxLayout(self.chart_container)

            lay = QtWidgets.QVBoxLayout(widget)
            lay.setContentsMargins(0, 0, 0, 0)
            lay.addWidget(self.chartview_xy)
            lay.addWidget(self.chartview_uz)


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
                fields = fields[: -1]  # get rid of \n char


                if (len(fields) - 1 ) /2 > self.n_axis:
                    self.n_axis = int ( (len(fields) - 1 ) /2 )

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
            print(self.axis_values)
            print(self.axis_values.shape)
            max_value_axis = np.max(self.axis_values,axis=0)
            self.xmax = max_value_axis[0]
            self.ymax = max_value_axis[1]
            self.umax = max_value_axis[2]
            self.zmax = max_value_axis[3]
            self.n = len(self.axis_values)
            #self.set_limits()

    def __distance(self,a0,a1):
        d = a1 - a0
        return np.sqrt(np.sum( d * d))

    def filter_by_dist(self):
        if CONFIG_QTCHART_ENABLED:
            self.filter_axe_dist(self.axis_values[:, [0, 1]], self.xy_base_serie)
            self.filter_axe_dist(self.axis_values[:, [2, 3]], self.uz_base_serie)


    def filter_axe_dist(self, xy_values, serie):
        serie.clear()
        xpos_2_plot = [0]
        p_prv = [0,0]
        for i, p in enumerate(xy_values):
            #dist = self.__distance(p, xy_values[self.xprv_p-1])
            dist = self.__distance(p,p_prv)
            if dist > DMIN:
                p_prv = p
                self.xprv_p = i
                xpos_2_plot.append(i)
                serie.append(QtCore.QPointF(p[0],p[1]))

    def add_point_fake(self):
        t0 = time.time()
        p = self.axis_values[self.pos, [0, 1]]
        self.pos += 1
        self.pos = self.pos % self.n
        self.xy_serie.append(QtCore.QPointF(p[0], p[1]))
        t1 = time.time()
        print(t0-t1)
    def add_point(self,p): # (x,y, z, u)
        if CONFIG_QTCHART_ENABLED:
            self.xy_serie.append(QtCore.QPointF(p[0],p[1]))
            if len(p) > 3:
                self.uz_serie.append(QtCore.QPointF(p[3],p[2]))
    def set_limits(self):
        widget_w = self.widget.width()
        widget_h = self.widget.height() / 2 # Two chartview on widget
        print(f"{widget_w} x {widget_h}")
        x_min = -5
        x_max = max(self.xmax,self.umax)
        y_min = -5
        y_max = self.xmax *(  widget_h / widget_w)
        if CONFIG_QTCHART_ENABLED:
            self.chart_xy.axisX(self.xy_serie).setMin(x_min)
            self.chart_xy.axisX(self.xy_serie).setMax(x_max)
            self.chart_xy.axisY(self.xy_serie).setMin(y_min)
            self.chart_xy.axisY(self.xy_serie).setMax(y_max)

            self.chart_uz.axisX(self.uz_serie).setMin(x_min)
            self.chart_uz.axisX(self.uz_serie).setMax(x_max)
            self.chart_uz.axisY(self.uz_serie).setMin(y_min)
            self.chart_uz.axisY(self.uz_serie).setMax(y_max)










