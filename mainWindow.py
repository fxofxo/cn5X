# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
  def setupUi(self, mainWindow):
    mainWindow.setObjectName("mainWindow")
    mainWindow.resize(1024, 600)
    self.centralwidget = QtWidgets.QWidget(mainWindow)
    self.centralwidget.setObjectName("centralwidget")
    self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
    self.verticalLayout.setObjectName("verticalLayout")
    self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
    self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
    self.tabWidget.setObjectName("tabWidget")
    self.tab = QtWidgets.QWidget()
    self.tab.setObjectName("tab")
    self.grpConnexion = QtWidgets.QGroupBox(self.tab)
    self.grpConnexion.setGeometry(QtCore.QRect(10, 0, 284, 113))
    self.grpConnexion.setObjectName("grpConnexion")
    self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.grpConnexion)
    self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
    self.verticalLayout_2.setSpacing(4)
    self.verticalLayout_2.setObjectName("verticalLayout_2")
    self.frame = QtWidgets.QFrame(self.grpConnexion)
    self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
    self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
    self.frame.setLineWidth(1)
    self.frame.setObjectName("frame")
    self.gridLayout = QtWidgets.QGridLayout(self.frame)
    self.gridLayout.setContentsMargins(0, 0, 0, 0)
    self.gridLayout.setSpacing(4)
    self.gridLayout.setObjectName("gridLayout")
    self.label = QtWidgets.QLabel(self.frame)
    self.label.setObjectName("label")
    self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
    self.cmbPort = QtWidgets.QComboBox(self.frame)
    self.cmbPort.setMinimumSize(QtCore.QSize(158, 23))
    self.cmbPort.setEditable(True)
    self.cmbPort.setObjectName("cmbPort")
    self.gridLayout.addWidget(self.cmbPort, 0, 1, 1, 1)
    self.label_2 = QtWidgets.QLabel(self.frame)
    self.label_2.setObjectName("label_2")
    self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
    self.cmbBauds = QtWidgets.QComboBox(self.frame)
    self.cmbBauds.setMinimumSize(QtCore.QSize(158, 23))
    self.cmbBauds.setObjectName("cmbBauds")
    self.gridLayout.addWidget(self.cmbBauds, 1, 1, 1, 1)
    self.verticalLayout_2.addWidget(self.frame)
    self.frame_2 = QtWidgets.QFrame(self.grpConnexion)
    self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
    self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
    self.frame_2.setObjectName("frame_2")
    self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
    self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
    self.horizontalLayout.setObjectName("horizontalLayout")
    self.lblConnectStatus = QtWidgets.QLabel(self.frame_2)
    self.lblConnectStatus.setMinimumSize(QtCore.QSize(160, 0))
    self.lblConnectStatus.setObjectName("lblConnectStatus")
    self.horizontalLayout.addWidget(self.lblConnectStatus)
    self.btnConnect = QtWidgets.QPushButton(self.frame_2)
    self.btnConnect.setMinimumSize(QtCore.QSize(100, 23))
    self.btnConnect.setObjectName("btnConnect")
    self.horizontalLayout.addWidget(self.btnConnect)
    self.verticalLayout_2.addWidget(self.frame_2)
    self.groupBox = QtWidgets.QGroupBox(self.tab)
    self.groupBox.setGeometry(QtCore.QRect(300, 0, 281, 331))
    self.groupBox.setObjectName("groupBox")
    self.frame_3 = QtWidgets.QFrame(self.groupBox)
    self.frame_3.setGeometry(QtCore.QRect(0, 20, 251, 197))
    self.frame_3.setStyleSheet("background-color: rgb(224, 224, 168);")
    self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
    self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
    self.frame_3.setObjectName("frame_3")
    self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
    self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
    self.gridLayout_2.setSpacing(4)
    self.gridLayout_2.setObjectName("gridLayout_2")
    self.label_6 = QtWidgets.QLabel(self.frame_3)
    font = QtGui.QFont()
    font.setFamily("LED Calculator")
    font.setPointSize(20)
    self.label_6.setFont(font)
    self.label_6.setObjectName("label_6")
    self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)
    self.lblPosX = QtWidgets.QLabel(self.frame_3)
    self.lblPosX.setMinimumSize(QtCore.QSize(170, 0))
    font = QtGui.QFont()
    font.setFamily("LED Calculator")
    font.setPointSize(20)
    self.lblPosX.setFont(font)
    self.lblPosX.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.lblPosX.setObjectName("lblPosX")
    self.gridLayout_2.addWidget(self.lblPosX, 0, 1, 1, 1)
    self.label_3 = QtWidgets.QLabel(self.frame_3)
    font = QtGui.QFont()
    font.setFamily("LED Calculator")
    font.setPointSize(20)
    self.label_3.setFont(font)
    self.label_3.setObjectName("label_3")
    self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
    self.label_4 = QtWidgets.QLabel(self.frame_3)
    font = QtGui.QFont()
    font.setFamily("LED Calculator")
    font.setPointSize(20)
    self.label_4.setFont(font)
    self.label_4.setObjectName("label_4")
    self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
    self.lblPosY = QtWidgets.QLabel(self.frame_3)
    self.lblPosY.setMinimumSize(QtCore.QSize(170, 0))
    font = QtGui.QFont()
    font.setFamily("LED Calculator")
    font.setPointSize(20)
    self.lblPosY.setFont(font)
    self.lblPosY.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.lblPosY.setObjectName("lblPosY")
    self.gridLayout_2.addWidget(self.lblPosY, 1, 1, 1, 1)
    self.label_5 = QtWidgets.QLabel(self.frame_3)
    font = QtGui.QFont()
    font.setFamily("LED Calculator")
    font.setPointSize(20)
    self.label_5.setFont(font)
    self.label_5.setObjectName("label_5")
    self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
    self.lblPosZ = QtWidgets.QLabel(self.frame_3)
    self.lblPosZ.setMinimumSize(QtCore.QSize(170, 0))
    font = QtGui.QFont()
    font.setFamily("LED Calculator")
    font.setPointSize(20)
    self.lblPosZ.setFont(font)
    self.lblPosZ.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.lblPosZ.setObjectName("lblPosZ")
    self.gridLayout_2.addWidget(self.lblPosZ, 2, 1, 2, 1)
    self.lblPosA = QtWidgets.QLabel(self.frame_3)
    self.lblPosA.setMinimumSize(QtCore.QSize(170, 0))
    font = QtGui.QFont()
    font.setFamily("LED Calculator")
    font.setPointSize(20)
    self.lblPosA.setFont(font)
    self.lblPosA.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.lblPosA.setObjectName("lblPosA")
    self.gridLayout_2.addWidget(self.lblPosA, 4, 1, 4, 1)
    self.lblPosB = QtWidgets.QLabel(self.frame_3)
    self.lblPosB.setMinimumSize(QtCore.QSize(170, 0))
    font = QtGui.QFont()
    font.setFamily("LED Calculator")
    font.setPointSize(20)
    self.lblPosB.setFont(font)
    self.lblPosB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.lblPosB.setObjectName("lblPosB")
    self.gridLayout_2.addWidget(self.lblPosB, 8, 1, 1, 1)
    self.label_7 = QtWidgets.QLabel(self.frame_3)
    font = QtGui.QFont()
    font.setFamily("LED Calculator")
    font.setPointSize(20)
    self.label_7.setFont(font)
    self.label_7.setObjectName("label_7")
    self.gridLayout_2.addWidget(self.label_7, 8, 0, 1, 1)
    self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
    self.groupBox_2.setGeometry(QtCore.QRect(10, 120, 281, 211))
    self.groupBox_2.setObjectName("groupBox_2")
    self.btnStart = QtWidgets.QPushButton(self.groupBox_2)
    self.btnStart.setEnabled(False)
    self.btnStart.setGeometry(QtCore.QRect(10, 150, 50, 50))
    self.btnStart.setMinimumSize(QtCore.QSize(50, 50))
    self.btnStart.setMaximumSize(QtCore.QSize(50, 50))
    self.btnStart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    self.btnStart.setStyleSheet("border-radius: 25;")
    self.btnStart.setText("")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("images/btnStart.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.btnStart.setIcon(icon)
    self.btnStart.setIconSize(QtCore.QSize(50, 50))
    self.btnStart.setObjectName("btnStart")
    self.btnStop = QtWidgets.QPushButton(self.groupBox_2)
    self.btnStop.setEnabled(False)
    self.btnStop.setGeometry(QtCore.QRect(80, 150, 50, 50))
    self.btnStop.setMinimumSize(QtCore.QSize(50, 50))
    self.btnStop.setMaximumSize(QtCore.QSize(50, 50))
    self.btnStop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    self.btnStop.setStyleSheet("border-radius: 25;")
    self.btnStop.setText("")
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap("images/btnStop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.btnStop.setIcon(icon1)
    self.btnStop.setIconSize(QtCore.QSize(50, 50))
    self.btnStop.setObjectName("btnStop")
    self.btnUrgence = QtWidgets.QPushButton(self.groupBox_2)
    self.btnUrgence.setGeometry(QtCore.QRect(20, 30, 100, 100))
    self.btnUrgence.setMinimumSize(QtCore.QSize(100, 100))
    self.btnUrgence.setMaximumSize(QtCore.QSize(100, 100))
    self.btnUrgence.setStyleSheet("border-radius: 25;")
    self.btnUrgence.setText("")
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap("images/btnUrgenceOff.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.btnUrgence.setIcon(icon2)
    self.btnUrgence.setIconSize(QtCore.QSize(100, 100))
    self.btnUrgence.setCheckable(True)
    self.btnUrgence.setChecked(True)
    self.btnUrgence.setObjectName("btnUrgence")
    self.ptxtDebug = QtWidgets.QPlainTextEdit(self.tab)
    self.ptxtDebug.setGeometry(QtCore.QRect(10, 340, 681, 111))
    self.ptxtDebug.setReadOnly(True)
    self.ptxtDebug.setObjectName("ptxtDebug")
    self.tabWidget.addTab(self.tab, "")
    self.tab_2 = QtWidgets.QWidget()
    self.tab_2.setObjectName("tab_2")
    self.tabWidget.addTab(self.tab_2, "")
    self.verticalLayout.addWidget(self.tabWidget)
    mainWindow.setCentralWidget(self.centralwidget)
    self.mnuBar = QtWidgets.QMenuBar(mainWindow)
    self.mnuBar.setGeometry(QtCore.QRect(0, 0, 1024, 22))
    self.mnuBar.setObjectName("mnuBar")
    self.mnuApplication = QtWidgets.QMenu(self.mnuBar)
    self.mnuApplication.setObjectName("mnuApplication")
    mainWindow.setMenuBar(self.mnuBar)
    self.statusBar = QtWidgets.QStatusBar(mainWindow)
    self.statusBar.setObjectName("statusBar")
    mainWindow.setStatusBar(self.statusBar)
    self.mnuAppOuvrir = QtWidgets.QAction(mainWindow)
    self.mnuAppOuvrir.setObjectName("mnuAppOuvrir")
    self.mnuAppQuitter = QtWidgets.QAction(mainWindow)
    self.mnuAppQuitter.setObjectName("mnuAppQuitter")
    self.mnuApplication.addAction(self.mnuAppOuvrir)
    self.mnuApplication.addSeparator()
    self.mnuApplication.addAction(self.mnuAppQuitter)
    self.mnuBar.addAction(self.mnuApplication.menuAction())

    self.retranslateUi(mainWindow)
    self.tabWidget.setCurrentIndex(0)
    QtCore.QMetaObject.connectSlotsByName(mainWindow)

  def retranslateUi(self, mainWindow):
    _translate = QtCore.QCoreApplication.translate
    mainWindow.setWindowTitle(_translate("mainWindow", "cn5X"))
    self.grpConnexion.setTitle(_translate("mainWindow", "Connexion"))
    self.label.setText(_translate("mainWindow", "Port :"))
    self.cmbPort.setToolTip(_translate("mainWindow", "Selectionnez le port de la machine grbl."))
    self.label_2.setText(_translate("mainWindow", "Bauds :"))
    self.lblConnectStatus.setText(_translate("mainWindow", "<Non Connecté>"))
    self.btnConnect.setText(_translate("mainWindow", "(Dé)Connecter"))
    self.groupBox.setTitle(_translate("mainWindow", "Machine status"))
    self.label_6.setText(_translate("mainWindow", "A"))
    self.lblPosX.setText(_translate("mainWindow", "+0.000"))
    self.label_3.setText(_translate("mainWindow", "X"))
    self.label_4.setText(_translate("mainWindow", "Y"))
    self.lblPosY.setText(_translate("mainWindow", "+0.000"))
    self.label_5.setText(_translate("mainWindow", "Z"))
    self.lblPosZ.setText(_translate("mainWindow", "+0.000"))
    self.lblPosA.setText(_translate("mainWindow", "+0.000"))
    self.lblPosB.setText(_translate("mainWindow", "+0.000"))
    self.label_7.setText(_translate("mainWindow", "B"))
    self.groupBox_2.setTitle(_translate("mainWindow", "GroupBox"))
    self.btnUrgence.setToolTip(_translate("mainWindow", "Dévérouiller l\'arrêt d\'urgence"))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainWindow", "Tab 1"))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainWindow", "Tab 2"))
    self.mnuApplication.setTitle(_translate("mainWindow", "&Application"))
    self.mnuAppOuvrir.setText(_translate("mainWindow", "&Ouvrir un fichier GCode..."))
    self.mnuAppQuitter.setText(_translate("mainWindow", "&Quitter"))
