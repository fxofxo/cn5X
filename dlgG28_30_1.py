# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgG28_30_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgG28_30_1(object):
  def setupUi(self, dlgG28_30_1):
    dlgG28_30_1.setObjectName("dlgG28_30_1")
    dlgG28_30_1.resize(387, 313)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(":/cn5X/images/XYZAB.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    dlgG28_30_1.setWindowIcon(icon)
    self.gridLayout = QtWidgets.QGridLayout(dlgG28_30_1)
    self.gridLayout.setContentsMargins(4, 4, 4, 4)
    self.gridLayout.setSpacing(4)
    self.gridLayout.setObjectName("gridLayout")
    self.label = QtWidgets.QLabel(dlgG28_30_1)
    self.label.setObjectName("label")
    self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
    self.frmMPos = QtWidgets.QFrame(dlgG28_30_1)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.frmMPos.sizePolicy().hasHeightForWidth())
    self.frmMPos.setSizePolicy(sizePolicy)
    self.frmMPos.setMinimumSize(QtCore.QSize(0, 0))
    self.frmMPos.setStyleSheet("background-color: rgb(248, 255, 192);\n"
"color: rgb(0, 0, 63);")
    self.frmMPos.setFrameShape(QtWidgets.QFrame.Box)
    self.frmMPos.setObjectName("frmMPos")
    self.gridLayout_2 = QtWidgets.QGridLayout(self.frmMPos)
    self.gridLayout_2.setContentsMargins(4, 0, 4, 0)
    self.gridLayout_2.setSpacing(0)
    self.gridLayout_2.setObjectName("gridLayout_2")
    self.lblLblPosX = QtWidgets.QLabel(self.frmMPos)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(1)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lblLblPosX.sizePolicy().hasHeightForWidth())
    self.lblLblPosX.setSizePolicy(sizePolicy)
    self.lblLblPosX.setMaximumSize(QtCore.QSize(16777215, 16777215))
    font = QtGui.QFont()
    font.setFamily("LED Calculator")
    font.setPointSize(20)
    self.lblLblPosX.setFont(font)
    self.lblLblPosX.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    self.lblLblPosX.setText("X")
    self.lblLblPosX.setObjectName("lblLblPosX")
    self.gridLayout_2.addWidget(self.lblLblPosX, 0, 0, 1, 1)
    self.lblPosX = QtWidgets.QLabel(self.frmMPos)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(3)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lblPosX.sizePolicy().hasHeightForWidth())
    self.lblPosX.setSizePolicy(sizePolicy)
    self.lblPosX.setMinimumSize(QtCore.QSize(0, 0))
    font = QtGui.QFont()
    font.setFamily("LED Calculator")
    font.setPointSize(20)
    self.lblPosX.setFont(font)
    self.lblPosX.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    self.lblPosX.setText("+00000.000")
    self.lblPosX.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.lblPosX.setObjectName("lblPosX")
    self.gridLayout_2.addWidget(self.lblPosX, 0, 1, 1, 1)
    self.lblLblPosY = QtWidgets.QLabel(self.frmMPos)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(1)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lblLblPosY.sizePolicy().hasHeightForWidth())
    self.lblLblPosY.setSizePolicy(sizePolicy)
    self.lblLblPosY.setMaximumSize(QtCore.QSize(16777215, 16777215))
    font = QtGui.QFont()
    font.setFamily("LED Calculator")
    font.setPointSize(20)
    self.lblLblPosY.setFont(font)
    self.lblLblPosY.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    self.lblLblPosY.setText("Y")
    self.lblLblPosY.setObjectName("lblLblPosY")
    self.gridLayout_2.addWidget(self.lblLblPosY, 1, 0, 1, 1)
    self.lblPosY = QtWidgets.QLabel(self.frmMPos)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(3)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lblPosY.sizePolicy().hasHeightForWidth())
    self.lblPosY.setSizePolicy(sizePolicy)
    self.lblPosY.setMinimumSize(QtCore.QSize(0, 0))
    font = QtGui.QFont()
    font.setFamily("LED Calculator")
    font.setPointSize(20)
    self.lblPosY.setFont(font)
    self.lblPosY.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    self.lblPosY.setText("+00000.000")
    self.lblPosY.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.lblPosY.setObjectName("lblPosY")
    self.gridLayout_2.addWidget(self.lblPosY, 1, 1, 1, 1)
    self.lblLblPosZ = QtWidgets.QLabel(self.frmMPos)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(1)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lblLblPosZ.sizePolicy().hasHeightForWidth())
    self.lblLblPosZ.setSizePolicy(sizePolicy)
    self.lblLblPosZ.setMaximumSize(QtCore.QSize(16777215, 16777215))
    font = QtGui.QFont()
    font.setFamily("LED Calculator")
    font.setPointSize(20)
    self.lblLblPosZ.setFont(font)
    self.lblLblPosZ.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    self.lblLblPosZ.setText("Z")
    self.lblLblPosZ.setObjectName("lblLblPosZ")
    self.gridLayout_2.addWidget(self.lblLblPosZ, 2, 0, 1, 1)
    self.lblPosZ = QtWidgets.QLabel(self.frmMPos)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(3)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lblPosZ.sizePolicy().hasHeightForWidth())
    self.lblPosZ.setSizePolicy(sizePolicy)
    self.lblPosZ.setMinimumSize(QtCore.QSize(0, 0))
    font = QtGui.QFont()
    font.setFamily("LED Calculator")
    font.setPointSize(20)
    self.lblPosZ.setFont(font)
    self.lblPosZ.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    self.lblPosZ.setText("+00000.000")
    self.lblPosZ.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.lblPosZ.setObjectName("lblPosZ")
    self.gridLayout_2.addWidget(self.lblPosZ, 2, 1, 1, 1)
    self.lblLblPosA = QtWidgets.QLabel(self.frmMPos)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(1)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lblLblPosA.sizePolicy().hasHeightForWidth())
    self.lblLblPosA.setSizePolicy(sizePolicy)
    self.lblLblPosA.setMaximumSize(QtCore.QSize(16777215, 16777215))
    font = QtGui.QFont()
    font.setFamily("LED Calculator")
    font.setPointSize(20)
    self.lblLblPosA.setFont(font)
    self.lblLblPosA.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    self.lblLblPosA.setText("A")
    self.lblLblPosA.setObjectName("lblLblPosA")
    self.gridLayout_2.addWidget(self.lblLblPosA, 3, 0, 1, 1)
    self.lblPosA = QtWidgets.QLabel(self.frmMPos)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(3)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lblPosA.sizePolicy().hasHeightForWidth())
    self.lblPosA.setSizePolicy(sizePolicy)
    self.lblPosA.setMinimumSize(QtCore.QSize(0, 0))
    font = QtGui.QFont()
    font.setFamily("LED Calculator")
    font.setPointSize(20)
    self.lblPosA.setFont(font)
    self.lblPosA.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    self.lblPosA.setText("+00000.000")
    self.lblPosA.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.lblPosA.setObjectName("lblPosA")
    self.gridLayout_2.addWidget(self.lblPosA, 3, 1, 1, 1)
    self.lblLblPosB = QtWidgets.QLabel(self.frmMPos)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(1)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lblLblPosB.sizePolicy().hasHeightForWidth())
    self.lblLblPosB.setSizePolicy(sizePolicy)
    self.lblLblPosB.setMaximumSize(QtCore.QSize(16777215, 16777215))
    font = QtGui.QFont()
    font.setFamily("LED Calculator")
    font.setPointSize(20)
    self.lblLblPosB.setFont(font)
    self.lblLblPosB.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    self.lblLblPosB.setText("B")
    self.lblLblPosB.setObjectName("lblLblPosB")
    self.gridLayout_2.addWidget(self.lblLblPosB, 4, 0, 1, 1)
    self.lblPosB = QtWidgets.QLabel(self.frmMPos)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(3)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lblPosB.sizePolicy().hasHeightForWidth())
    self.lblPosB.setSizePolicy(sizePolicy)
    self.lblPosB.setMinimumSize(QtCore.QSize(0, 0))
    font = QtGui.QFont()
    font.setFamily("LED Calculator")
    font.setPointSize(20)
    self.lblPosB.setFont(font)
    self.lblPosB.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    self.lblPosB.setText("+00000.000")
    self.lblPosB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.lblPosB.setObjectName("lblPosB")
    self.gridLayout_2.addWidget(self.lblPosB, 4, 1, 1, 1)
    self.lblLblPosC = QtWidgets.QLabel(self.frmMPos)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(1)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lblLblPosC.sizePolicy().hasHeightForWidth())
    self.lblLblPosC.setSizePolicy(sizePolicy)
    self.lblLblPosC.setMaximumSize(QtCore.QSize(16777215, 16777215))
    font = QtGui.QFont()
    font.setFamily("LED Calculator")
    font.setPointSize(20)
    self.lblLblPosC.setFont(font)
    self.lblLblPosC.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    self.lblLblPosC.setText("C")
    self.lblLblPosC.setObjectName("lblLblPosC")
    self.gridLayout_2.addWidget(self.lblLblPosC, 5, 0, 1, 1)
    self.lblPosC = QtWidgets.QLabel(self.frmMPos)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(3)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lblPosC.sizePolicy().hasHeightForWidth())
    self.lblPosC.setSizePolicy(sizePolicy)
    self.lblPosC.setMinimumSize(QtCore.QSize(0, 0))
    font = QtGui.QFont()
    font.setFamily("LED Calculator")
    font.setPointSize(20)
    self.lblPosC.setFont(font)
    self.lblPosC.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    self.lblPosC.setText("+00000.000")
    self.lblPosC.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.lblPosC.setObjectName("lblPosC")
    self.gridLayout_2.addWidget(self.lblPosC, 5, 1, 1, 1)
    self.gridLayout.addWidget(self.frmMPos, 1, 0, 1, 3)
    self.pushButton = QtWidgets.QPushButton(dlgG28_30_1)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
    self.pushButton.setSizePolicy(sizePolicy)
    self.pushButton.setText("")
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(":/cn5X/images/questionG28.1.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.pushButton.setIcon(icon1)
    self.pushButton.setIconSize(QtCore.QSize(48, 48))
    self.pushButton.setAutoDefault(False)
    self.pushButton.setFlat(True)
    self.pushButton.setObjectName("pushButton")
    self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
    self.lblMessage = QtWidgets.QLabel(dlgG28_30_1)
    self.lblMessage.setWordWrap(True)
    self.lblMessage.setObjectName("lblMessage")
    self.gridLayout.addWidget(self.lblMessage, 2, 1, 1, 2)
    self.chkDontShow = QtWidgets.QCheckBox(dlgG28_30_1)
    self.chkDontShow.setObjectName("chkDontShow")
    self.gridLayout.addWidget(self.chkDontShow, 3, 0, 1, 2)
    self.buttonBox = QtWidgets.QDialogButtonBox(dlgG28_30_1)
    self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
    self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Yes)
    self.buttonBox.setObjectName("buttonBox")
    self.gridLayout.addWidget(self.buttonBox, 3, 2, 1, 1)

    self.retranslateUi(dlgG28_30_1)
    QtCore.QMetaObject.connectSlotsByName(dlgG28_30_1)

  def retranslateUi(self, dlgG28_30_1):
    _translate = QtCore.QCoreApplication.translate
    dlgG28_30_1.setWindowTitle(_translate("dlgG28_30_1", "Define G28.1 absolute position"))
    self.label.setText(_translate("dlgG28_30_1", "Current machine position (MPos)"))
    self.lblMessage.setText(_translate("dlgG28_30_1", "Save the current machine position (MPos) in the G28.1 Grbl\'s location?"))
    self.chkDontShow.setText(_translate("dlgG28_30_1", "Don\'t show confirmation again"))

import cn5X_rc