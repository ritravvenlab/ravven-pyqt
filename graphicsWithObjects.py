# Dr. Kaputa
# graphics example with graphic objects

import sys
from PyQt4 import QtGui,QtCore
 
class Ball(QtGui.QGraphicsItem):
  def __init__(self,parent):
    super(Ball,self).__init__()
    self.parent = parent    
    
  def boundingRect(self):
    return QtCore.QRectF(0,0,100,100)

  def paint(self,painter,option,widget):
    painter.setBrush(QtGui.QColor(0,0,255))
    painter.drawEllipse(0,0,100,100)

class Viewer(QtGui.QGraphicsView):
  def __init__(self,parent):
    super(Viewer,self).__init__()
    self.parent = parent
    self.scene = QtGui.QGraphicsScene(self)
    self.setScene(self.scene)

    self.myBall1 = Ball(self)
    self.myBall2 = Ball(self)
    self.myBall1.setPos(1000,0)
    self.scene.addItem(self.myBall1)
    self.scene.addItem(self.myBall2)
     
    # timer code
    self.timer = QtCore.QBasicTimer()
    self.timer.start(1000,self)
    
    self.boardWidth = 1000
    self.boardHeight = 1000
    self.myRect = self.scene.addRect(0,0,self.boardWidth,self.boardHeight)

  def resizeEvent(self,event):
    super(Viewer,self).resizeEvent(event)
    self.fitInView(self.scene.sceneRect(),QtCore.Qt.KeepAspectRatio)

  def timerEvent(self,event):
    self.myBall1.moveBy(-20,20)
    self.myBall2.moveBy(20,20)
    if (self.myBall1.collidesWithItem(self.myBall2)):
      print "collision"
    
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
    pass    
    #self.viewer.myRect.moveBy(-20,-20)
 
def main():
  app = QtGui.QApplication(sys.argv)
  mainWindow = MainWindow()
  sys.exit(app.exec_())
 
if __name__ == '__main__':
  main()