# Dr. Kaputa
# main window example
  
import sys
from PyQt4 import QtGui,QtCore
 
class MainWindow(QtGui.QMainWindow):
  def __init__(self):
    super(MainWindow,self).__init__()
    self.statusBar().showMessage("ready")

    self.dock = QtGui.QDockWidget(self)
    self.button1 = QtGui.QPushButton("button 1")
    self.button2 = QtGui.QPushButton("button 2")
    self.vLayout = QtGui.QVBoxLayout()
    self.vLayout.addWidget(self.button1)
    self.vLayout.addWidget(self.button2)
    self.dockFrame = QtGui.QFrame()
    self.dockFrame.setLayout(self.vLayout)
    self.dock.setWidget(self.dockFrame)
    self.addDockWidget(QtCore.Qt.DockWidgetArea(4),self.dock)
    
    self.dock2 = QtGui.QDockWidget(self)
    self.button3 = QtGui.QPushButton("button 3")
    self.button4 = QtGui.QPushButton("button 4")
    self.vLayout2 = QtGui.QVBoxLayout()
    self.vLayout2.addWidget(self.button3)
    self.vLayout2.addWidget(self.button4)
    self.dockFrame2 = QtGui.QFrame()
    self.dockFrame2.setLayout(self.vLayout2)
    self.dock2.setWidget(self.dockFrame2)
    self.addDockWidget(QtCore.Qt.DockWidgetArea(4),self.dock2)    
     
    exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)        
    exitAction.setShortcut('Ctrl+Q')
    exitAction.setStatusTip('Exit application')
    exitAction.triggered.connect(QtGui.qApp.quit)

    self.statusBar()

    menubar = self.menuBar()
    fileMenu = menubar.addMenu('&File')
    fileMenu.addAction(exitAction)    
    
    self.show()
 
def main():
  app = QtGui.QApplication(sys.argv)
  mainWindow = MainWindow()
  sys.exit(app.exec_())
 
if __name__ == '__main__':
  main()