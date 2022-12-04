# cn5X++
 

2021-Nov

I will modificate the excelent UI create by Gauthier Brière in order to fit my personal needs and flavours 
building a foam cutter machine


Original developme of Gauthier Brière could be found here

https://github.com/fra589/cn5X

Nouveau panneau de contrôle Grbl 5/6 axes avec pour but d'implémenter toutes les fonctionalités de grbl-Mega-5X...  
*New 5/6 axis Grbl control panel to implement all the grbl-Mega-5X capabilities...*  
  
## Attention !  
Ce dépot est une version en cours de développement. Utilisation à vos risques et périls.
  
## *Warning !*  
*This repository is version under development. Use at your own risk.*  
  
  
| *cn5X++ is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.* |
| :--- |
  
  
## Prérequis :  
depuis la version 0.5.a, QTSerialPort à été remplacé par le module pure python pyserial qui à l'avantage de fonctionner sans (trop) de problème avec Microsoft Windows.  
cn5X++ est basé sur Python3, PyQT5 et python-serial.  
Pour installer les prérequis sur un système Linux type Debian :  
```
apt-get install python3 python3-pyqt5 python3-serial
```
En utilisation sous Linux, l'utilisateur doit faire partie du groupe Unix dialout pour pouvoir utiliser les ports série :  
```
adduser <username> dialout
```
  
## *prerequisite :*  
*since version 0.5.a, QTSerialPort has been replaced by the pure python pyserial module which has the advantage of working without (too many) problems with Microsoft Windows.*  
*cn5X ++ is based on Python3, PyQT5 and python-serial.*  
*To install the prerequisites on a Linux system such as Debian:*  
```
apt-get install python3-serial
apt-get install python3 python3-pyqt5

or  
python3 -m pip install serial
python3 -m pip install pyserial

pip install pyqt5
pip install pyqtchart
pip install numpy
pip install PyQtChart
```

Interface design:

designer
pyrcc5 cn5X.qrc -o cn5X_rc.py 
pyuic5 mainWindow.ui >mainWindow.py 



To use qt tools  designer, pyrcc5 and pyuic5 install:
```
sudo apt-get install qttools5-dev-tools
pip  install pyqt5-dev-tools
pip install pyuic5-tool
Some equivalen utilities as pyside2 can be installed
pip3 install pyside2

```
*When using under Linux, the user must be part of the Unix dialout group to be able to use the serial ports:*  
```
adduser <username> dialout
```
  
-------------
cn5X++ is an open-source project and fueled by the free-time of our intrepid administrators and altruistic users. If you'd like to donate, all proceeds will be used to help fund supporting hardware and testing equipment. Thank you! [![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://www.paypal.com/donate/?business=CZZN52UPPVHCW&no_recurring=0&item_name=Grbl-Mega-5X+%26+cn5X%2B%2B+donations&currency_code=EUR)
>>>>>>> feature/graphprogress
