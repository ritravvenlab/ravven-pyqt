# Dr. Kaputa
# basic coordinate example

import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    self.grid = Grid(self)
    self.vLayout = QtGui.QVBoxLayout()    
    self.vLayout.addWidget(self.grid)
    self.frame = QtGui.QFrame(self)
    self.frame.setLayout(self.vLayout)
    self.setCentralWidget(self.frame)
    self.showMaximized()
    self.show()
   
class Grid(QtGui.QGraphicsView):   
  def __init__(self,parent):
    super(Grid, self).__init__()
    self.parent = parent
    self.scene = QtGui.QGraphicsScene(self)
    self.setScene(self.scene)

    self.gridWidth = 1
    self.gridHeight = 1    
    
    # effectively sets the logical scene coordinates from 0,0 to 1,1
    myFrame = self.scene.addRect(0,0,self.gridWidth,self.gridHeight) 

    self.scene.addRect(0,0,.1,.2)
         
  def resizeEvent(self, event):
    super(Grid, self).resizeEvent(event)
    self.fitInView(self.scene.sceneRect(), QtCore.Qt.KeepAspectRatio) 
       
def main():
  app = QtGui.QApplication(sys.argv) 
  mainWindow = MainWindow()
  sys.exit(app.exec_())

if __name__ == '__main__':
    main()