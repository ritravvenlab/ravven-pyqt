# Dr. Kaputa
# hello world with pyqt

import sys
from PyQt4 import QtCore, QtGui

class MyWidget(QtGui.QPushButton):
  def __init__(self):
    super(MyWidget,self).__init__()
    self.setText("hello world")
    self.show()
    
def main():
  app = QtGui.QApplication(sys.argv)
  myWidget = MyWidget()
  sys.exit(app.exec_())
  
if __name__ == '__main__':
  main()