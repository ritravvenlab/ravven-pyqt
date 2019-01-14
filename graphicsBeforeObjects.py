# Dr. Kaputa
# grahics example with timer

import sys
from PyQt4 import QtGui,QtCore
 
class Viewer(QtGui.QGraphicsView):
  def __init__(self,parent):
    super(Viewer,self).__init__()
    self.parent = parent
    self.scene = QtGui.QGraphicsScene(self)
    self.setScene(self.scene)
    self.myRect = self.scene.addRect(0,0,50,50)
    self.myCircle = self.scene.addEllipse(0,0,100,100)

    # timer code
    self.timer = QtCore.QBasicTimer()
    self.timer.start(2000,self.parent)

  def timerEvent(self,event):
    self.myRect.moveBy(20,20)

  def keyPressEvent(self,event):
    key = event.key()
    if key == QtCore.Qt.Key_A:
      self.myRect.moveBy(-20,-20)
 
class MainWindow(QtGui.QMainWindow):
  def __init__(self):
    super(MainWindow,self).__init__()

    self.myLayout = QtGui.QVBoxLayout()
    self.viewer = Viewer(self)
    self.myLayout.addWidget(self.viewer)

    self.myFrame = QtGui.QFrame(self)
    self.myFrame.setLayout(self.myLayout)     
     
    self.setCentralWidget(self.myFrame)
    self.show()
    
  def timerEvent(self,event):
    self.viewer.myRect.moveBy(20,20)
 
def main():
  app = QtGui.QApplication(sys.argv)
  mainWindow = MainWindow()
  sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()