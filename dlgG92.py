# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgG92.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_dlgG92(object):
  def setupUi(self, dlgG92):
    dlgG92.setObjectName("dlgG92")
    dlgG92.setWindowModality(QtCore.Qt.ApplicationModal)
    dlgG92.resize(358, 276)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(dlgG92.sizePolicy().hasHeightForWidth())
    dlgG92.setSizePolicy(sizePolicy)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(":/cn5X/images/origine.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    dlgG92.setWindowIcon(icon)
    dlgG92.setModal(True)
    self.gridLayout_2 = QtWidgets.QGridLayout(dlgG92)
    self.gridLayout_2.setContentsMargins(4, 4, 4, 4)
    self.gridLayout_2.setHorizontalSpacing(6)
    self.gridLayout_2.setVerticalSpacing(0)
    self.gridLayout_2.setObjectName("gridLayout_2")
    self.widget = QtWidgets.QWidget(dlgG92)
    self.widget.setObjectName("widget")
    self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
    self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
    self.horizontalLayout.setSpacing(0)
    self.horizontalLayout.setObjectName("horizontalLayout")
    self.label_2 = QtWidgets.QLabel(self.widget)
    self.label_2.setText("")
    self.label_2.setPixmap(QtGui.QPixmap(":/cn5X/images/origine.svg"))
    self.label_2.setScaledContents(True)
    self.label_2.setObjectName("label_2")
    self.horizontalLayout.addWidget(self.label_2)
    self.label = QtWidgets.QLabel(self.widget)
    self.label.setWordWrap(True)
    self.label.setObjectName("label")
    self.horizontalLayout.addWidget(self.label)
    self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 2)
    self.widget1 = QtWidgets.QWidget(dlgG92)
    self.widget1.setObjectName("widget1")
    self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
    self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
    self.verticalLayout_2.setSpacing(0)
    self.verticalLayout_2.setObjectName("verticalLayout_2")
    spacerItem = QtWidgets.QSpacerItem(20, 22, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    self.verticalLayout_2.addItem(spacerItem)
    self.widget2 = QtWidgets.QWidget(self.widget1)
    self.widget2.setObjectName("widget2")
    self.gridLayout = QtWidgets.QGridLayout(self.widget2)
    self.gridLayout.setContentsMargins(0, 0, 0, 0)
    self.gridLayout.setHorizontalSpacing(0)
    self.gridLayout.setVerticalSpacing(2)
    self.gridLayout.setObjectName("gridLayout")
    self.chkDefineX = QtWidgets.QCheckBox(self.widget2)
    self.chkDefineX.setObjectName("chkDefineX")
    self.gridLayout.addWidget(self.chkDefineX, 0, 0, 1, 1)
    self.dsbG92valeurX = QtWidgets.QDoubleSpinBox(self.widget2)
    self.dsbG92valeurX.setMaximumSize(QtCore.QSize(16777215, 23))
    self.dsbG92valeurX.setStyleSheet("color: #bebebe;")
    self.dsbG92valeurX.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.dsbG92valeurX.setDecimals(3)
    self.dsbG92valeurX.setMinimum(-10000.0)
    self.dsbG92valeurX.setMaximum(10000.0)
    self.dsbG92valeurX.setSingleStep(0.1)
    self.dsbG92valeurX.setProperty("value", 0.0)
    self.dsbG92valeurX.setObjectName("dsbG92valeurX")
    self.gridLayout.addWidget(self.dsbG92valeurX, 0, 1, 1, 1)
    self.chkDefineY = QtWidgets.QCheckBox(self.widget2)
    self.chkDefineY.setObjectName("chkDefineY")
    self.gridLayout.addWidget(self.chkDefineY, 1, 0, 1, 1)
    self.dsbG92valeurY = QtWidgets.QDoubleSpinBox(self.widget2)
    self.dsbG92valeurY.setMaximumSize(QtCore.QSize(16777215, 23))
    self.dsbG92valeurY.setStyleSheet("color: #bebebe;")
    self.dsbG92valeurY.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.dsbG92valeurY.setDecimals(3)
    self.dsbG92valeurY.setMinimum(-10000.0)
    self.dsbG92valeurY.setMaximum(10000.0)
    self.dsbG92valeurY.setSingleStep(0.1)
    self.dsbG92valeurY.setProperty("value", 0.0)
    self.dsbG92valeurY.setObjectName("dsbG92valeurY")
    self.gridLayout.addWidget(self.dsbG92valeurY, 1, 1, 1, 1)
    self.chkDefineZ = QtWidgets.QCheckBox(self.widget2)
    self.chkDefineZ.setObjectName("chkDefineZ")
    self.gridLayout.addWidget(self.chkDefineZ, 2, 0, 1, 1)
    self.dsbG92valeurZ = QtWidgets.QDoubleSpinBox(self.widget2)
    self.dsbG92valeurZ.setMaximumSize(QtCore.QSize(16777215, 23))
    self.dsbG92valeurZ.setStyleSheet("color: #bebebe;")
    self.dsbG92valeurZ.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.dsbG92valeurZ.setDecimals(3)
    self.dsbG92valeurZ.setMinimum(-10000.0)
    self.dsbG92valeurZ.setMaximum(10000.0)
    self.dsbG92valeurZ.setSingleStep(0.1)
    self.dsbG92valeurZ.setProperty("value", 0.0)
    self.dsbG92valeurZ.setObjectName("dsbG92valeurZ")
    self.gridLayout.addWidget(self.dsbG92valeurZ, 2, 1, 1, 1)
    self.chkDefineA = QtWidgets.QCheckBox(self.widget2)
    self.chkDefineA.setObjectName("chkDefineA")
    self.gridLayout.addWidget(self.chkDefineA, 3, 0, 1, 1)
    self.dsbG92valeurA = QtWidgets.QDoubleSpinBox(self.widget2)
    self.dsbG92valeurA.setMaximumSize(QtCore.QSize(16777215, 23))
    self.dsbG92valeurA.setStyleSheet("color: #bebebe;")
    self.dsbG92valeurA.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.dsbG92valeurA.setDecimals(3)
    self.dsbG92valeurA.setMinimum(-10000.0)
    self.dsbG92valeurA.setMaximum(10000.0)
    self.dsbG92valeurA.setSingleStep(0.1)
    self.dsbG92valeurA.setProperty("value", 0.0)
    self.dsbG92valeurA.setObjectName("dsbG92valeurA")
    self.gridLayout.addWidget(self.dsbG92valeurA, 3, 1, 1, 1)
    self.chkDefineB = QtWidgets.QCheckBox(self.widget2)
    self.chkDefineB.setObjectName("chkDefineB")
    self.gridLayout.addWidget(self.chkDefineB, 4, 0, 1, 1)
    self.dsbG92valeurB = QtWidgets.QDoubleSpinBox(self.widget2)
    self.dsbG92valeurB.setMaximumSize(QtCore.QSize(16777215, 23))
    self.dsbG92valeurB.setStyleSheet("color: #bebebe;")
    self.dsbG92valeurB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.dsbG92valeurB.setDecimals(3)
    self.dsbG92valeurB.setMinimum(-10000.0)
    self.dsbG92valeurB.setMaximum(10000.0)
    self.dsbG92valeurB.setSingleStep(0.1)
    self.dsbG92valeurB.setProperty("value", 0.0)
    self.dsbG92valeurB.setObjectName("dsbG92valeurB")
    self.gridLayout.addWidget(self.dsbG92valeurB, 4, 1, 1, 1)
    self.chkDefineC = QtWidgets.QCheckBox(self.widget2)
    self.chkDefineC.setObjectName("chkDefineC")
    self.gridLayout.addWidget(self.chkDefineC, 5, 0, 1, 1)
    self.dsbG92valeurC = QtWidgets.QDoubleSpinBox(self.widget2)
    self.dsbG92valeurC.setMaximumSize(QtCore.QSize(16777215, 23))
    self.dsbG92valeurC.setStyleSheet("color: #bebebe;")
    self.dsbG92valeurC.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.dsbG92valeurC.setDecimals(3)
    self.dsbG92valeurC.setMinimum(-10000.0)
    self.dsbG92valeurC.setMaximum(10000.0)
    self.dsbG92valeurC.setSingleStep(0.1)
    self.dsbG92valeurC.setProperty("value", 0.0)
    self.dsbG92valeurC.setObjectName("dsbG92valeurC")
    self.gridLayout.addWidget(self.dsbG92valeurC, 5, 1, 1, 1)
    self.verticalLayout_2.addWidget(self.widget2)
    self.gridLayout_2.addWidget(self.widget1, 1, 0, 1, 1)
    self.widget3 = QtWidgets.QWidget(dlgG92)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.widget3.sizePolicy().hasHeightForWidth())
    self.widget3.setSizePolicy(sizePolicy)
    self.widget3.setObjectName("widget3")
    self.verticalLayout = QtWidgets.QVBoxLayout(self.widget3)
    self.verticalLayout.setContentsMargins(0, 0, 0, 0)
    self.verticalLayout.setSpacing(4)
    self.verticalLayout.setObjectName("verticalLayout")
    self.btnSetOriginG92 = QtWidgets.QPushButton(self.widget3)
    self.btnSetOriginG92.setEnabled(False)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.btnSetOriginG92.sizePolicy().hasHeightForWidth())
    self.btnSetOriginG92.setSizePolicy(sizePolicy)
    self.btnSetOriginG92.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    self.btnSetOriginG92.setObjectName("btnSetOriginG92")
    self.verticalLayout.addWidget(self.btnSetOriginG92)
    self.btnSetOriginG92_1 = QtWidgets.QPushButton(self.widget3)
    self.btnSetOriginG92_1.setEnabled(True)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.btnSetOriginG92_1.sizePolicy().hasHeightForWidth())
    self.btnSetOriginG92_1.setSizePolicy(sizePolicy)
    self.btnSetOriginG92_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    self.btnSetOriginG92_1.setObjectName("btnSetOriginG92_1")
    self.verticalLayout.addWidget(self.btnSetOriginG92_1)
    spacerItem1 = QtWidgets.QSpacerItem(18, 33, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    self.verticalLayout.addItem(spacerItem1)
    self.chkAutoclose = QtWidgets.QCheckBox(self.widget3)
    self.chkAutoclose.setChecked(True)
    self.chkAutoclose.setObjectName("chkAutoclose")
    self.verticalLayout.addWidget(self.chkAutoclose)
    self.buttonBox = QtWidgets.QDialogButtonBox(self.widget3)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
    self.buttonBox.setSizePolicy(sizePolicy)
    self.buttonBox.setOrientation(QtCore.Qt.Vertical)
    self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
    self.buttonBox.setObjectName("buttonBox")
    self.verticalLayout.addWidget(self.buttonBox)
    self.gridLayout_2.addWidget(self.widget3, 1, 1, 1, 1)

    self.retranslateUi(dlgG92)
    QtCore.QMetaObject.connectSlotsByName(dlgG92)

  def retranslateUi(self, dlgG92):
    _translate = QtCore.QCoreApplication.translate
    dlgG92.setWindowTitle(_translate("dlgG92", "G92 Offset setting"))
    self.label.setText(_translate("dlgG92", "G92 commands work from current axis location and add and subtract correctly to give the current axis position the value assigned by the G92 command."))
    self.chkDefineX.setText(_translate("dlgG92", "Assign X value"))
    self.chkDefineY.setText(_translate("dlgG92", "Assign Y value"))
    self.chkDefineZ.setText(_translate("dlgG92", "Assign Z value"))
    self.chkDefineA.setText(_translate("dlgG92", "Assign A value"))
    self.chkDefineB.setText(_translate("dlgG92", "Assign B value"))
    self.chkDefineC.setText(_translate("dlgG92", "Assign C value"))
    self.btnSetOriginG92.setText(_translate("dlgG92", "Set G92\n"
"Axis values"))
    self.btnSetOriginG92_1.setText(_translate("dlgG92", "Turn off\n"
"and reset\n"
"G92"))
    self.chkAutoclose.setText(_translate("dlgG92", "Auto close"))

import cn5X_rc
