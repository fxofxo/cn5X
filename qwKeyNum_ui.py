# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qwKeyNum_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_keynum(object):
  def setupUi(self, keynum):
    keynum.setObjectName("keynum")
    keynum.resize(261, 359)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(keynum.sizePolicy().hasHeightForWidth())
    keynum.setSizePolicy(sizePolicy)
    self.gridLayout = QtWidgets.QGridLayout(keynum)
    self.gridLayout.setContentsMargins(6, 6, 6, 6)
    self.gridLayout.setSpacing(3)
    self.gridLayout.setObjectName("gridLayout")
    self.qwBarreTitre = QtWidgets.QWidget(keynum)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.qwBarreTitre.sizePolicy().hasHeightForWidth())
    self.qwBarreTitre.setSizePolicy(sizePolicy)
    self.qwBarreTitre.setMinimumSize(QtCore.QSize(0, 32))
    self.qwBarreTitre.setMaximumSize(QtCore.QSize(16777215, 32))
    self.qwBarreTitre.setObjectName("qwBarreTitre")
    self.horizontalLayout = QtWidgets.QHBoxLayout(self.qwBarreTitre)
    self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
    self.horizontalLayout.setSpacing(0)
    self.horizontalLayout.setObjectName("horizontalLayout")
    spacerItem = QtWidgets.QSpacerItem(214, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.horizontalLayout.addItem(spacerItem)
    self.btnClose = QtWidgets.QPushButton(self.qwBarreTitre)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
    self.btnClose.setSizePolicy(sizePolicy)
    self.btnClose.setMinimumSize(QtCore.QSize(32, 32))
    self.btnClose.setMaximumSize(QtCore.QSize(32, 32))
    font = QtGui.QFont()
    font.setPointSize(22)
    font.setBold(True)
    font.setWeight(75)
    self.btnClose.setFont(font)
    self.btnClose.setStyleSheet("background-color: rgb(0, 0, 63);\n"
"color: rgb(248, 255, 192);")
    self.btnClose.setObjectName("btnClose")
    self.horizontalLayout.addWidget(self.btnClose)
    self.gridLayout.addWidget(self.qwBarreTitre, 0, 0, 1, 4)
    self.keybButtonClear = QtWidgets.QPushButton(keynum)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.keybButtonClear.sizePolicy().hasHeightForWidth())
    self.keybButtonClear.setSizePolicy(sizePolicy)
    self.keybButtonClear.setMinimumSize(QtCore.QSize(60, 60))
    self.keybButtonClear.setMaximumSize(QtCore.QSize(60, 60))
    font = QtGui.QFont()
    font.setPointSize(22)
    self.keybButtonClear.setFont(font)
    self.keybButtonClear.setFocusPolicy(QtCore.Qt.NoFocus)
    self.keybButtonClear.setStyleSheet("background-color: rgb(246, 97, 81);")
    self.keybButtonClear.setObjectName("keybButtonClear")
    self.gridLayout.addWidget(self.keybButtonClear, 1, 0, 1, 1)
    self.keybButtonBackSpace = QtWidgets.QPushButton(keynum)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.keybButtonBackSpace.sizePolicy().hasHeightForWidth())
    self.keybButtonBackSpace.setSizePolicy(sizePolicy)
    self.keybButtonBackSpace.setMinimumSize(QtCore.QSize(60, 60))
    self.keybButtonBackSpace.setMaximumSize(QtCore.QSize(60, 60))
    font = QtGui.QFont()
    font.setPointSize(22)
    self.keybButtonBackSpace.setFont(font)
    self.keybButtonBackSpace.setFocusPolicy(QtCore.Qt.NoFocus)
    self.keybButtonBackSpace.setStyleSheet("background-color: rgb(255, 163, 72);")
    self.keybButtonBackSpace.setObjectName("keybButtonBackSpace")
    self.gridLayout.addWidget(self.keybButtonBackSpace, 1, 1, 1, 1)
    self.keybButtonLeft = QtWidgets.QPushButton(keynum)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.keybButtonLeft.sizePolicy().hasHeightForWidth())
    self.keybButtonLeft.setSizePolicy(sizePolicy)
    self.keybButtonLeft.setMinimumSize(QtCore.QSize(60, 60))
    self.keybButtonLeft.setMaximumSize(QtCore.QSize(60, 60))
    font = QtGui.QFont()
    font.setPointSize(22)
    self.keybButtonLeft.setFont(font)
    self.keybButtonLeft.setFocusPolicy(QtCore.Qt.NoFocus)
    self.keybButtonLeft.setStyleSheet("background-color: rgb(248, 228, 92);")
    self.keybButtonLeft.setObjectName("keybButtonLeft")
    self.gridLayout.addWidget(self.keybButtonLeft, 1, 2, 1, 1)
    self.keybButtonRight = QtWidgets.QPushButton(keynum)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.keybButtonRight.sizePolicy().hasHeightForWidth())
    self.keybButtonRight.setSizePolicy(sizePolicy)
    self.keybButtonRight.setMinimumSize(QtCore.QSize(60, 60))
    self.keybButtonRight.setMaximumSize(QtCore.QSize(60, 60))
    font = QtGui.QFont()
    font.setPointSize(22)
    self.keybButtonRight.setFont(font)
    self.keybButtonRight.setFocusPolicy(QtCore.Qt.NoFocus)
    self.keybButtonRight.setStyleSheet("background-color: rgb(248, 228, 92);")
    self.keybButtonRight.setObjectName("keybButtonRight")
    self.gridLayout.addWidget(self.keybButtonRight, 1, 3, 1, 1)
    self.keybButton7 = QtWidgets.QPushButton(keynum)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.keybButton7.sizePolicy().hasHeightForWidth())
    self.keybButton7.setSizePolicy(sizePolicy)
    self.keybButton7.setMinimumSize(QtCore.QSize(60, 60))
    self.keybButton7.setMaximumSize(QtCore.QSize(60, 60))
    font = QtGui.QFont()
    font.setPointSize(22)
    self.keybButton7.setFont(font)
    self.keybButton7.setFocusPolicy(QtCore.Qt.NoFocus)
    self.keybButton7.setStyleSheet("background-color: rgb(98, 160, 234);")
    self.keybButton7.setObjectName("keybButton7")
    self.gridLayout.addWidget(self.keybButton7, 2, 0, 1, 1)
    self.keybButton8 = QtWidgets.QPushButton(keynum)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.keybButton8.sizePolicy().hasHeightForWidth())
    self.keybButton8.setSizePolicy(sizePolicy)
    self.keybButton8.setMinimumSize(QtCore.QSize(60, 60))
    self.keybButton8.setMaximumSize(QtCore.QSize(60, 60))
    font = QtGui.QFont()
    font.setPointSize(22)
    self.keybButton8.setFont(font)
    self.keybButton8.setFocusPolicy(QtCore.Qt.NoFocus)
    self.keybButton8.setStyleSheet("background-color: rgb(98, 160, 234);")
    self.keybButton8.setObjectName("keybButton8")
    self.gridLayout.addWidget(self.keybButton8, 2, 1, 1, 1)
    self.keybButton9 = QtWidgets.QPushButton(keynum)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.keybButton9.sizePolicy().hasHeightForWidth())
    self.keybButton9.setSizePolicy(sizePolicy)
    self.keybButton9.setMinimumSize(QtCore.QSize(60, 60))
    self.keybButton9.setMaximumSize(QtCore.QSize(60, 60))
    font = QtGui.QFont()
    font.setPointSize(22)
    self.keybButton9.setFont(font)
    self.keybButton9.setFocusPolicy(QtCore.Qt.NoFocus)
    self.keybButton9.setStyleSheet("background-color: rgb(98, 160, 234);")
    self.keybButton9.setObjectName("keybButton9")
    self.gridLayout.addWidget(self.keybButton9, 2, 2, 1, 1)
    self.keybButtonHome = QtWidgets.QPushButton(keynum)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.keybButtonHome.sizePolicy().hasHeightForWidth())
    self.keybButtonHome.setSizePolicy(sizePolicy)
    self.keybButtonHome.setMinimumSize(QtCore.QSize(60, 60))
    self.keybButtonHome.setMaximumSize(QtCore.QSize(60, 60))
    font = QtGui.QFont()
    font.setPointSize(22)
    self.keybButtonHome.setFont(font)
    self.keybButtonHome.setFocusPolicy(QtCore.Qt.NoFocus)
    self.keybButtonHome.setStyleSheet("background-color: rgb(248, 228, 92);")
    self.keybButtonHome.setObjectName("keybButtonHome")
    self.gridLayout.addWidget(self.keybButtonHome, 2, 3, 1, 1)
    self.keybButton4 = QtWidgets.QPushButton(keynum)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.keybButton4.sizePolicy().hasHeightForWidth())
    self.keybButton4.setSizePolicy(sizePolicy)
    self.keybButton4.setMinimumSize(QtCore.QSize(60, 60))
    self.keybButton4.setMaximumSize(QtCore.QSize(60, 60))
    font = QtGui.QFont()
    font.setPointSize(22)
    self.keybButton4.setFont(font)
    self.keybButton4.setFocusPolicy(QtCore.Qt.NoFocus)
    self.keybButton4.setStyleSheet("background-color: rgb(98, 160, 234);")
    self.keybButton4.setObjectName("keybButton4")
    self.gridLayout.addWidget(self.keybButton4, 3, 0, 1, 1)
    self.keybButton5 = QtWidgets.QPushButton(keynum)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.keybButton5.sizePolicy().hasHeightForWidth())
    self.keybButton5.setSizePolicy(sizePolicy)
    self.keybButton5.setMinimumSize(QtCore.QSize(60, 60))
    self.keybButton5.setMaximumSize(QtCore.QSize(60, 60))
    font = QtGui.QFont()
    font.setPointSize(22)
    self.keybButton5.setFont(font)
    self.keybButton5.setFocusPolicy(QtCore.Qt.NoFocus)
    self.keybButton5.setStyleSheet("background-color: rgb(98, 160, 234);")
    self.keybButton5.setObjectName("keybButton5")
    self.gridLayout.addWidget(self.keybButton5, 3, 1, 1, 1)
    self.keybButton6 = QtWidgets.QPushButton(keynum)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.keybButton6.sizePolicy().hasHeightForWidth())
    self.keybButton6.setSizePolicy(sizePolicy)
    self.keybButton6.setMinimumSize(QtCore.QSize(60, 60))
    self.keybButton6.setMaximumSize(QtCore.QSize(60, 60))
    font = QtGui.QFont()
    font.setPointSize(22)
    self.keybButton6.setFont(font)
    self.keybButton6.setFocusPolicy(QtCore.Qt.NoFocus)
    self.keybButton6.setStyleSheet("background-color: rgb(98, 160, 234);")
    self.keybButton6.setObjectName("keybButton6")
    self.gridLayout.addWidget(self.keybButton6, 3, 2, 1, 1)
    self.keybButtonEnd = QtWidgets.QPushButton(keynum)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.keybButtonEnd.sizePolicy().hasHeightForWidth())
    self.keybButtonEnd.setSizePolicy(sizePolicy)
    self.keybButtonEnd.setMinimumSize(QtCore.QSize(60, 60))
    self.keybButtonEnd.setMaximumSize(QtCore.QSize(60, 60))
    font = QtGui.QFont()
    font.setPointSize(22)
    self.keybButtonEnd.setFont(font)
    self.keybButtonEnd.setFocusPolicy(QtCore.Qt.NoFocus)
    self.keybButtonEnd.setStyleSheet("background-color: rgb(248, 228, 92);")
    self.keybButtonEnd.setObjectName("keybButtonEnd")
    self.gridLayout.addWidget(self.keybButtonEnd, 3, 3, 1, 1)
    self.keybButton1 = QtWidgets.QPushButton(keynum)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.keybButton1.sizePolicy().hasHeightForWidth())
    self.keybButton1.setSizePolicy(sizePolicy)
    self.keybButton1.setMinimumSize(QtCore.QSize(60, 60))
    self.keybButton1.setMaximumSize(QtCore.QSize(60, 60))
    font = QtGui.QFont()
    font.setPointSize(22)
    self.keybButton1.setFont(font)
    self.keybButton1.setFocusPolicy(QtCore.Qt.NoFocus)
    self.keybButton1.setStyleSheet("background-color: rgb(98, 160, 234);")
    self.keybButton1.setObjectName("keybButton1")
    self.gridLayout.addWidget(self.keybButton1, 4, 0, 1, 1)
    self.keybButton2 = QtWidgets.QPushButton(keynum)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.keybButton2.sizePolicy().hasHeightForWidth())
    self.keybButton2.setSizePolicy(sizePolicy)
    self.keybButton2.setMinimumSize(QtCore.QSize(60, 60))
    self.keybButton2.setMaximumSize(QtCore.QSize(60, 60))
    font = QtGui.QFont()
    font.setPointSize(22)
    self.keybButton2.setFont(font)
    self.keybButton2.setFocusPolicy(QtCore.Qt.NoFocus)
    self.keybButton2.setStyleSheet("background-color: rgb(98, 160, 234);")
    self.keybButton2.setObjectName("keybButton2")
    self.gridLayout.addWidget(self.keybButton2, 4, 1, 1, 1)
    self.keybButton3 = QtWidgets.QPushButton(keynum)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.keybButton3.sizePolicy().hasHeightForWidth())
    self.keybButton3.setSizePolicy(sizePolicy)
    self.keybButton3.setMinimumSize(QtCore.QSize(60, 60))
    self.keybButton3.setMaximumSize(QtCore.QSize(60, 60))
    font = QtGui.QFont()
    font.setPointSize(22)
    self.keybButton3.setFont(font)
    self.keybButton3.setFocusPolicy(QtCore.Qt.NoFocus)
    self.keybButton3.setStyleSheet("background-color: rgb(98, 160, 234);")
    self.keybButton3.setObjectName("keybButton3")
    self.gridLayout.addWidget(self.keybButton3, 4, 2, 1, 1)
    self.keybButtonUp = QtWidgets.QPushButton(keynum)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.keybButtonUp.sizePolicy().hasHeightForWidth())
    self.keybButtonUp.setSizePolicy(sizePolicy)
    self.keybButtonUp.setMinimumSize(QtCore.QSize(60, 60))
    self.keybButtonUp.setMaximumSize(QtCore.QSize(60, 60))
    font = QtGui.QFont()
    font.setPointSize(22)
    self.keybButtonUp.setFont(font)
    self.keybButtonUp.setFocusPolicy(QtCore.Qt.NoFocus)
    self.keybButtonUp.setStyleSheet("background-color: rgb(181, 131, 90);")
    self.keybButtonUp.setObjectName("keybButtonUp")
    self.gridLayout.addWidget(self.keybButtonUp, 4, 3, 1, 1)
    self.keybButtonMoins = QtWidgets.QPushButton(keynum)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.keybButtonMoins.sizePolicy().hasHeightForWidth())
    self.keybButtonMoins.setSizePolicy(sizePolicy)
    self.keybButtonMoins.setMinimumSize(QtCore.QSize(60, 60))
    self.keybButtonMoins.setMaximumSize(QtCore.QSize(60, 60))
    font = QtGui.QFont()
    font.setPointSize(22)
    font.setBold(False)
    font.setWeight(50)
    self.keybButtonMoins.setFont(font)
    self.keybButtonMoins.setFocusPolicy(QtCore.Qt.NoFocus)
    self.keybButtonMoins.setStyleSheet("background-color: rgb(153, 193, 241);")
    self.keybButtonMoins.setObjectName("keybButtonMoins")
    self.gridLayout.addWidget(self.keybButtonMoins, 5, 0, 1, 1)
    self.keybButton0 = QtWidgets.QPushButton(keynum)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.keybButton0.sizePolicy().hasHeightForWidth())
    self.keybButton0.setSizePolicy(sizePolicy)
    self.keybButton0.setMinimumSize(QtCore.QSize(60, 60))
    self.keybButton0.setMaximumSize(QtCore.QSize(60, 60))
    font = QtGui.QFont()
    font.setPointSize(22)
    self.keybButton0.setFont(font)
    self.keybButton0.setFocusPolicy(QtCore.Qt.NoFocus)
    self.keybButton0.setStyleSheet("background-color: rgb(98, 160, 234);")
    self.keybButton0.setObjectName("keybButton0")
    self.gridLayout.addWidget(self.keybButton0, 5, 1, 1, 1)
    self.keybButtonPoint = QtWidgets.QPushButton(keynum)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.keybButtonPoint.sizePolicy().hasHeightForWidth())
    self.keybButtonPoint.setSizePolicy(sizePolicy)
    self.keybButtonPoint.setMinimumSize(QtCore.QSize(60, 60))
    self.keybButtonPoint.setMaximumSize(QtCore.QSize(60, 60))
    font = QtGui.QFont()
    font.setPointSize(22)
    self.keybButtonPoint.setFont(font)
    self.keybButtonPoint.setFocusPolicy(QtCore.Qt.NoFocus)
    self.keybButtonPoint.setStyleSheet("background-color: rgb(153, 193, 241);")
    self.keybButtonPoint.setObjectName("keybButtonPoint")
    self.gridLayout.addWidget(self.keybButtonPoint, 5, 2, 1, 1)
    self.keybButtonDown = QtWidgets.QPushButton(keynum)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.keybButtonDown.sizePolicy().hasHeightForWidth())
    self.keybButtonDown.setSizePolicy(sizePolicy)
    self.keybButtonDown.setMinimumSize(QtCore.QSize(60, 60))
    self.keybButtonDown.setMaximumSize(QtCore.QSize(60, 60))
    font = QtGui.QFont()
    font.setPointSize(22)
    self.keybButtonDown.setFont(font)
    self.keybButtonDown.setFocusPolicy(QtCore.Qt.NoFocus)
    self.keybButtonDown.setStyleSheet("background-color: rgb(181, 131, 90);")
    self.keybButtonDown.setObjectName("keybButtonDown")
    self.gridLayout.addWidget(self.keybButtonDown, 5, 3, 1, 1)

    self.retranslateUi(keynum)
    QtCore.QMetaObject.connectSlotsByName(keynum)

  def retranslateUi(self, keynum):
    _translate = QtCore.QCoreApplication.translate
    keynum.setWindowTitle(_translate("keynum", "keyNum"))
    self.btnClose.setText(_translate("keynum", "X"))
    self.keybButtonClear.setText(_translate("keynum", "⌧"))
    self.keybButtonBackSpace.setText(_translate("keynum", "⌫"))
    self.keybButtonLeft.setText(_translate("keynum", "←"))
    self.keybButtonRight.setText(_translate("keynum", "→"))
    self.keybButton7.setText(_translate("keynum", "7"))
    self.keybButton8.setText(_translate("keynum", "8"))
    self.keybButton9.setText(_translate("keynum", "9"))
    self.keybButtonHome.setText(_translate("keynum", "⇱"))
    self.keybButton4.setText(_translate("keynum", "4"))
    self.keybButton5.setText(_translate("keynum", "5"))
    self.keybButton6.setText(_translate("keynum", "6"))
    self.keybButtonEnd.setText(_translate("keynum", "⇲"))
    self.keybButton1.setText(_translate("keynum", "1"))
    self.keybButton2.setText(_translate("keynum", "2"))
    self.keybButton3.setText(_translate("keynum", "3"))
    self.keybButtonUp.setText(_translate("keynum", "↑"))
    self.keybButtonMoins.setText(_translate("keynum", "−"))
    self.keybButton0.setText(_translate("keynum", "0"))
    self.keybButtonPoint.setText(_translate("keynum", "."))
    self.keybButtonDown.setText(_translate("keynum", "↓"))
