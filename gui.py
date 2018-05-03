
import sys
from PyQt4.QtWidgets import (QWidget, QToolTip, 
    QPushButton, QApplication, QDesktopWidget)
from PyQt4.QtGui import QFont    
from PyQt4 import QtGui


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        QToolTip.setFont(QFont('SansSerif', 10))
        
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        buttonSection = QtGui.QSplitter(QtCore.Qt.Horizontal)
        btn = QPushButton('Button', self)
        buttonSection.addWidget(btn)
        buttonSection.addWidget(btn)
        buttonSection.addWidget(btn)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)       
        
        self.setGeometry(600, 600, 600, 600)
        self.setWindowTitle('Kindleing')  
        self.center()  
        self.show()
    def center(self):
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())