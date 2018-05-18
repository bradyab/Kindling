import sys
import os

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDesktopWidget
from PyQt5.QtGui import QIcon, QPixmap

import shutil
import foldercount
import predict
 
class App(QWidget):
    global photoind, pic, pushButton
    def __init__(self, operation):
        super().__init__()
        self.title = 'Kindling - '+ operation #sys.argv[1]
        self.operation = operation
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 680
        self.trainpath = './training_data/'
        self.photoind = 1
        self.photopath = './images/userpic'+ str(self.photoind) +'.jpg'
        self.predictpath = './prediction/userpic' + str(self.photoind) + '.jpg'
        self.pic = QLabel(self)
        self.make_directories()
        if operation == 'predict': #sys.argv[1] == 'predict':
            self.prediction = predict.predictlikedislike(self.predictpath)
        self.initUI()

    def make_directories(self):
        if not os.path.isdir(self.trainpath):
            os.makedirs(self.trainpath)
        if not os.path.isdir(self.trainpath+'like/'):
            os.makedirs(self.trainpath+'like/')
        if not os.path.isdir(self.trainpath+'dislike/'):
            os.makedirs(self.trainpath+'dislike/')
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        if self.operation == 'train': #sys.argv[1] == 'train':
            pixmap = QPixmap(self.photopath)
            pixmap = pixmap.scaled(640,640)
            self.pic.setPixmap(pixmap)

            self.pushButton_1 = QtWidgets.QPushButton('Dislike',self)
            self.pushButton_1.setGeometry(QtCore.QRect(160, 645, 92, 30))
            self.pushButton_1.setObjectName("pushButton")
            self.pushButton_1.clicked.connect(self.button1Clicked)

            self.pushButton_2 = QtWidgets.QPushButton('Like',self)
            self.pushButton_2.setGeometry(QtCore.QRect(360, 645, 92, 30))
            self.pushButton_2.setObjectName("pushButton_2")
            self.pushButton_2.clicked.connect(self.button2Clicked)

        elif self.operation == 'predict': #sys.argv[1] == 'predict':
            pixmap = QPixmap(self.predictpath)
            pixmap = pixmap.scaled(640,640)
            self.pic.setPixmap(pixmap)

            dislikechance = self.prediction[0][0]
            dislikechance = float("{0:.2f}".format(dislikechance))
            self.pushButton_3 = QtWidgets.QPushButton('Dislike - ' + str(dislikechance),self)
            self.pushButton_3.setGeometry(QtCore.QRect(160, 645, 92, 30))
            self.pushButton_3.setObjectName('pushButton_3')
            self.pushButton_3.clicked.connect(self.button3Clicked)

            likechance = self.prediction[0][1]
            likechance = float("{0:.2f}".format(likechance))
            self.pushButton_4 = QtWidgets.QPushButton('Like - ' + str(likechance), self)
            self.pushButton_4.setGeometry(QtCore.QRect(360,645, 92, 30))
            self.pushButton_4.setObjectName('pushButton_4')
            self.pushButton_4.clicked.connect(self.button4Clicked)

        self.center()
        self.show()

    def center(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def sortimagetrain(self,decision):
        if(os.path.exists(self.photopath)):
            movepath = self.trainpath+decision+'/'
            likecount = foldercount.numfile(movepath)
            shutil.copyfile(self.photopath, movepath+decision + str(likecount+1)+'.jpg' )
        else:
            self.close()
    def button1Clicked(self):
        self.sortimagetrain("dislike")
        #self.photoChange("./images/")

    def button2Clicked(self):
        self.sortimagetrain('like')
        #self.photoChange("./images/")   

    def button3Clicked(self):
        self.photoChange("./prediction/")
        self.buttonChange()

    def button4Clicked(self):
        self.photoChange("./prediction/")
        self.buttonChange()

    def photoChange(self, imagepath):
        if self.operation == 'train': #sys.argv[1] == 'train':
            self.photoind += 1
            self.photopath = imagepath+'userpic'+ str(self.photoind) +'.jpg'
            pixmap = QPixmap(self.photopath)
            pixmap = pixmap.scaled(640,640)
            self.pic.setPixmap(pixmap)
        elif self.operation == 'predict': #sys.argv[1] == 'predict':
            self.photoind += 1
            self.predictpath = './prediction/userpic' + str(self.photoind) + '.jpg'
            pixmap = QPixmap(self.predictpath)
            pixmap = pixmap.scaled(640,640)
            self.pic.setPixmap(pixmap)

        return self.photoind
    def buttonChange(self):
        self.prediction = predict.predictlikedislike(self.predictpath)

        dislikechance = self.prediction[0][0]
        dislikechance = float("{0:.2f}".format(dislikechance))
        self.pushButton_3.setText('Dislike - ' + str(dislikechance))
        

        likechance = self.prediction[0][1]
        likechance = float("{0:.2f}".format(likechance))
        self.pushButton_4.setText('Like - ' + str(likechance))

    def keyPressEvent(self, e):
        if self.operation == 'train': #sys.argv[1] == "train":
            if e.key() == Qt.Key_Escape:
                self.close()
            elif e.key() == Qt.Key_1:
                self.button1Clicked()
            elif e.key() == Qt.Key_2:
                self.button2Clicked()
        elif self.operation == 'predict': #sys.argv[1] == "predict":
            if e.key() == Qt.Key_Escape:
                self.close()
            elif e.key() == Qt.Key_1:
                self.button3Clicked()
            elif e.key() == Qt.Key_2:
                self.button4Clicked()
    
# if __name__ == '__main__':
#     if len(sys.argv) > 1:
#         if sys.argv[1] in ["train", "predict"]:
#             app = QApplication(sys.argv)
#             ex = App()
#             sys.exit(app.exec_())
#         else:
#             print("Use the train or predict argument")
#     else:
#         print("Use the train or predict argument")