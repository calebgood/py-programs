import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import PyQt4

class window(QWidget):
   def __init__(self, parent = None):
      super(window, self).__init__(parent)
		
      layout = QVBoxLayout()
      self.btn = QPushButton("Get tat img")
      self.btn.clicked.connect(self.getfile)
		
      layout.addWidget(self.btn)
      self.le = QLabel("Long time no see")
      layout.addWidget(self.le)
      
      self.contents = QTextEdit()
      layout.addWidget(self.contents)
      self.setLayout(layout)
      self.setWindowTitle("conv this to tkinter")
	
   def getfile(self):
      fname = QFileDialog.getOpenFileName(self, 'Open file', 
         'c:\\',"Image files (*.jpg *.gif)")
      dotat=QPixmap(fname)
      self.le.setPixmap(dotat)
				

def main():
   app = QApplication(sys.argv)
   ex = window()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
