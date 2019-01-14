# Dr. Kaputa
# pyqt pong example

import sys
from PyQt4 import QtGui, QtCore

class Pong(QtGui.QMainWindow):
  Key_K = QtCore.pyqtSignal()  
  Key_M = QtCore.pyqtSignal()  
  Key_A = QtCore.pyqtSignal()  
  Key_Z = QtCore.pyqtSignal()  
  
  def __init__(self):
    super(Pong, self).__init__()
    self.statusBar().showMessage('Ready')
    self.setWindowIcon(QtGui.QIcon('cool.jpg')) 
    
    exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)        
    exitAction.setShortcut('Ctrl+Q')
    exitAction.setStatusTip('Exit application')
    exitAction.triggered.connect(QtGui.qApp.quit)
    
    menubar = self.menuBar()
    fileMenu = menubar.addMenu('&File')
    fileMenu.addAction(exitAction)    
    
    self.hLayout = QtGui.QHBoxLayout()
    self.leftScorebox = QtGui.QLabel("0")
    self.rightScorebox = QtGui.QLabel("0")  
    self.rightScorebox.setAlignment(QtCore.Qt.AlignRight);  
    self.startButton = QtGui.QPushButton("Start")  

    self.hLayout.addWidget(self.leftScorebox)
    self.hLayout.addWidget(self.startButton)
    self.hLayout.addWidget(self.rightScorebox)       
    
    self.dockFrame = QtGui.QFrame()
    self.dockFrame.setLayout(self.hLayout)    
    
    self.dock = QtGui.QDockWidget(self)
    self.dock.setWidget(self.dockFrame)
    self.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dock)
    self.dock.setWindowTitle("Controls")

    self.setFocusPolicy(QtCore.Qt.StrongFocus)
    self.leftScore = 0
    self.rightScore = 0    
 
    self.board = Board(self)
    self.vLayout = QtGui.QVBoxLayout()    
    self.vLayout.addWidget(self.board)
    
    self.frame = QtGui.QFrame(self)
    self.frame.setLayout(self.vLayout)

    self.setCentralWidget(self.frame)
    self.setWindowTitle("Pong") 
    self.showMaximized()
    self.show()
    
    styleFile ="styleSheet.txt"
    with open(styleFile,"r") as fh:
      self.setStyleSheet(fh.read())
    
    self.startButton.clicked.connect(lambda: self.board.startGame()) 
    
  def keyPressEvent(self, event):
    key = event.key()  
    if key == QtCore.Qt.Key_K:     
      self.Key_K.emit()
    elif key == QtCore.Qt.Key_M:
      self.Key_M.emit()
    elif key == QtCore.Qt.Key_A:
      self.Key_A.emit()
    elif key == QtCore.Qt.Key_Z:
      self.Key_Z.emit()

  def updateScore(self,val):
    if (val == 2):
      self.leftScore = self.leftScore + 1
      self.leftScorebox.setText(str(self.leftScore))
    elif (val == 1):
      self.rightScore = self.rightScore + 1
      self.rightScorebox.setText(str(self.rightScore))
    
class Paddle(QtGui.QGraphicsItem):
  def __init__(self,boardWidth,boardHeight):
    super(Paddle, self).__init__()     
    self.color = QtGui.QColor(0,0,255)
    self.boardWidth = boardWidth
    self.boardHeight = boardHeight
          
  def boundingRect(self):
    return QtCore.QRectF(0,0,20,100)
      
  def paint(self, painter, option, widget):
    painter.setBrush(self.color)
    painter.drawRect(0,0,20,100)
      
  def moveDown(self):
    y = self.y()
    if (y < self.boardHeight - 100):
        self.moveBy(0,50)
      
  def moveUp(self):
    y = self.y()
    if (y > 0):
      self.moveBy(0,-50)
        
class Ball(QtGui.QGraphicsItem):
  def __init__(self,parent,boardWidth,boardHeight):
    super(Ball, self).__init__()     
    self.color = QtGui.QColor(0,0,255)
    self.xVel = 10
    self.yVel = 5
    self.ballWidth = 20
    self.ballHeight = 20
    self.boardWidth = boardWidth
    self.boardHeight = boardHeight
    self.parent = parent
     
  def boundingRect(self):
    return QtCore.QRectF(-self.ballWidth/2,-self.ballHeight/2,self.ballWidth,self.ballHeight)
      
  def paint(self, painter, option, widget):
    painter.setBrush(self.color)
    painter.drawEllipse(-self.ballWidth/2,-self.ballHeight/2,self.ballWidth,self.ballHeight)       
     
  def reflectX(self):
    self.xVel = self.xVel * -1
      
  def reflectY(self):
    self.yVel = self.yVel * -1   
      
  def move(self):
    self.setX(self.x() + self.xVel)
    if (self.x() >= self.boardWidth - self.ballWidth/2):
      return 2
    elif (self.x() <= self.ballWidth/2):
      return 1
  
    self.setY(self.y() + self.yVel)
    if (self.y() >= self.boardHeight - self.ballHeight/2):
      self.reflectY()
    elif (self.y() <= self.ballHeight/2):
      self.reflectY()
        
    if self.collidesWithItem(self.parent.leftPaddle):
      self.reflectX()

    if self.collidesWithItem(self.parent.rightPaddle):
      self.reflectX()

    return 0

class Board(QtGui.QGraphicsView):   
  def __init__(self,parent):
    super(Board, self).__init__()
    self.parent = parent
    self.scene = QtGui.QGraphicsScene(self)
    self.setScene(self.scene)
    self.setBackgroundBrush(QtGui.QBrush(QtGui.QPixmap('cool.jpg')))
    
    self.boardWidth = 1000
    self.boardHeight = 1000    
    
    # effectively sets the logical scene coordinates from 0,0 to 1000,1000
    myFrame = self.scene.addRect(0,0,self.boardWidth,self.boardHeight) 

    self.leftPaddle = Paddle(self.boardWidth,self.boardHeight)
    self.rightPaddle = Paddle(self.boardWidth,self.boardHeight)
    self.ball = Ball(self,self.boardWidth,self.boardHeight)
    
    self.scene.addItem(self.leftPaddle)

    self.scene.addItem(self.rightPaddle)
    self.scene.addItem(self.ball)
 
    self.timer = QtCore.QBasicTimer()
    self.leftPaddle.setPos(0,0)
    self.rightPaddle.setPos(980,100)
    self.ball.setPos(500,500)
    
    self.parent.Key_M.connect(self.rightPaddle.moveDown)
    self.parent.Key_K.connect(self.rightPaddle.moveUp)
    self.parent.Key_Z.connect(self.leftPaddle.moveDown)
    self.parent.Key_A.connect(self.leftPaddle.moveUp)

  def startGame(self):
    self.status = 0
    self.ball.setPos(500,500)
    self.timer.start(17, self)   

  def timerEvent(self, event): 
    if (self.status == 0):
      self.status = self.ball.move()
    else:
      self.timer.stop()
      self.parent.updateScore(self.status)
        
  def resizeEvent(self, event):
    super(Board, self).resizeEvent(event)
    self.fitInView(self.scene.sceneRect(), QtCore.Qt.KeepAspectRatio) 
       
def main():
  app = QtGui.QApplication(sys.argv)
  app.setFont(QtGui.QFont("Helvetica", 10))  
  pong = Pong()
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()