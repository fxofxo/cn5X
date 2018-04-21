# -*- coding: utf-8 -*-

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'                                                                         '
' Copyright 2018 Gauthier Brière (gauthier.briere "at" gmail.com)         '
'                                                                         '
' This file is part of cn5X++                                               '
'                                                                         '
' cn5X++ is free software: you can redistribute it and/or modify it         '
'  under the terms of the GNU General Public License as published by      '
' the Free Software Foundation, either version 3 of the License, or       '
' (at your option) any later version.                                     '
'                                                                         '
' cn5X++ is distributed in the hope that it will be useful, but           '
' WITHOUT ANY WARRANTY; without even the implied warranty of              '
' MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           '
' GNU General Public License for more details.                            '
'                                                                         '
' You should have received a copy of the GNU General Public License       '
' along with this program.  If not, see <http://www.gnu.org/licenses/>.   '
'                                                                         '
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIntValidator

class qwEditMask(QtWidgets.QWidget):
  ''' Widget personalisé construisant un masque binaire (pour 6 axes) avec 6 cases à cocher
  '''

  valueChanged = pyqtSignal(int) # signal émis à chaque changement de valeur

  def __init__(self, parent=None):
    super().__init__(parent)

    self.__changeEnCours = False

    # Création cadre exterieur
    self.frame = QtWidgets.QFrame()
    self.frame.setMinimumSize(QtCore.QSize(127, 19))
    self.frame.setMaximumSize(QtCore.QSize(127, 19))
    self.frame.setObjectName("frame")
    self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
    self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
    self.horizontalLayout.setSpacing(2)
    self.horizontalLayout.setObjectName("horizontalLayout")

    # création des 6 checkBoxes
    self.chk = []
    for i in range(6):
      print(i)
      self.chk.append(QtWidgets.QCheckBox(self.frame))
      self.chk[i].setLayoutDirection(QtCore.Qt.RightToLeft)
      self.chk[i].setText("")
      self.chk[i].setObjectName("chk{}".format(i))
      self.horizontalLayout.addWidget(self.chk[i])
      self.chk[i].stateChanged.connect(self.chkStateChange)

    # Création zone de texte
    self.lneMask = QtWidgets.QLineEdit(self.frame)
    self.lneMask.setMinimumSize(QtCore.QSize(31, 19))
    self.lneMask.setMaximumSize(QtCore.QSize(31, 19))
    self.lneMask.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.lneMask.setObjectName("lneMask")
    self.lneMask.setText("0")
    validator = QIntValidator(0, 63, self)
    self.lneMask.setValidator(validator)
    self.horizontalLayout.addWidget(self.lneMask)
    self.lneMask.textChanged.connect(self.lneTextChanged)

    self.setLayout(self.horizontalLayout)


  @pyqtSlot(int)
  def chkStateChange(self, value):
    if not self.__changeEnCours:
      self.__changeEnCours = True
      newVal = 0
      for i in range(6):
        if self.chk[i].isChecked():
          newVal += 2**i
      self.lneMask.setText(format(newVal))
      self.valueChanged.emit(newVal)
      self.__changeEnCours = False


  @pyqtSlot(str)
  def lneTextChanged(self, txt: str):
    if not self.__changeEnCours:
      self.__changeEnCours = True
      newVal = int(txt)
      for i in range(6):
        if newVal & 2**i:
          self.chk[i].setCheckState(Qt.Checked)
        else:
          self.chk[i].setCheckState(Qt.Unchecked)
      self.valueChanged.emit(newVal)
      self.__changeEnCours = False


  @pyqtSlot()
  def getValue(self):
    ''' Renvoie la valeur du masque '''
    return int(self.lneMask.text())


  @pyqtSlot(int)
  def setValue(self, val: int):
    ''' affecte une nouvelle valeur au masque '''
    self.lneMask.setText(format(val))


  # Définie la propriété pour permettre la configuration par Designer
  value = QtCore.pyqtProperty(int, fget=getValue, fset=setValue)

