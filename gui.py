import sys
import os

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

import shutil
import foldercount
 
class App(QWidget):
    global photoind, pic, pushButton
    def __init__(self):
        super().__init__()
        self.title = 'Kindling'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 680
        self.photoind = 1
        self.photopath = './images/resize/userpic'+ str(self.photoind) +'.jpg'
        self.datapath = './training_data/'
        self.pic = QLabel(self)
        self.initUI()

 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


        pixmap = QPixmap(self.photopath)
        self.pic.setPixmap(pixmap)

        self.pushButton = QtWidgets.QPushButton('Dislike',self)
        self.pushButton.setGeometry(QtCore.QRect(160, 645, 92, 30))
        self.pushButton.setObjectName("pushButton")


        self.pushButton_2 = QtWidgets.QPushButton('Like',self)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 645, 92, 30))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton.clicked.connect(self.button1Clicked)
        self.pushButton_2.clicked.connect(self.button1Clicked)

 
        self.show()
    def sortimage(self,decision):
        if(os.path.exists(self.photopath)):
            movepath = self.datapath+decision+'/'
            likecount = foldercount.numfile(movepath)
            shutil.copyfile(self.photopath, movepath+decision + str(likecount+1)+'.jpg' )
        else:
            self.close()
    def button1Clicked(self):
        self.sortimage("dislike")
        self.photoChange()

    def button2Clicked(self):
        self.sortimage('like')
        self.photoChange()   

    def photoChange(self):
        self.photoind = self.photoind + 1
        self.photopath = './images/resize/userpic'+ str(self.photoind) +'.jpg'
        pixmap = QPixmap(self.photopath)
        self.pic.setPixmap(pixmap)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_1:
            self.button1Clicked()
        elif e.key() == Qt.Key_2:
            self.button2Clicked()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
