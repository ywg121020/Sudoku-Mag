# !/usr/bin/env python
# -*- coding:utf-8 -*-

'''
添加模块目录
'''

import  sys


from PyQt5.QtGui import QIcon,QEnterEvent
from PyQt5.QtWidgets import QApplication,QMessageBox,QFileDialog
from UIdeviceFrames import *
from base import *
from PyQt5.QtGui import QIcon,QPixmap,QImage
from PyQt5.QtCore import QRect,QObject,Qt,pyqtSignal,QTimer
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from imgMsg import *
import cv2
class mainFramelessWindow(FramelessWindow):
    def __init__(self, frame_x, frame_y, *args, **kwargs):
        super(mainFramelessWindow, self).__init__(frame_x,frame_y,*args, **kwargs)


class mainFrame(QWidget, Ui_device):
    def __init__(self, *args, **kwargs):
        super(mainFrame, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.read.clicked.connect(self.openFile)
        self.successFlag = 0
        self.handFlag = 0
        self.autoFlag = 0
        self.oneKey.setText("一键填充：CLOSE")
        self.handKey.setText("手动填充：CLOSE")
        self.reset.clicked.connect(self.resetProcess)
        self.oneKey.clicked.connect(self.oneKeyProcess)
        self.handKey.clicked.connect(self.handkeyProcess)
    def handkeyProcess(self):
        if self.autoFlag == 1:
            pass
        else:
            if self.successFlag == 1:
                if self.handFlag == 0:
                    self.handKey.setText("手动填充：OPEN ")
                    self.handFlag = 1
                else:
                    self.handKey.setText("手动填充：CLOSE")
                    self.handFlag = 0
    def oneKeyProcess(self):
        if self.handKey == 1:
            pass
        else:
            if self.successFlag == 1:
                if self.autoFlag == 0:
                    self.oneKey.setText("一键填充：OPEN ")
                    self.autoFlag = 1
                    self.autoMagProcess()
                else:
                    self.oneKey.setText("一键填充：CLOSE")
                    self.autoFlag = 0

    def resetProcess(self):
        self.handFlag = 0
        self.autoFlag = 0
        if self.successFlag == 1:
            self.imgMagHand = copy.deepcopy(self.img)
            self.showImg(copy.deepcopy(self.img))
            self.imgMagAuto = copy.deepcopy(self.img)

        self.oneKey.setText("一键填充：CLOSE")
        self.handKey.setText("手动填充：CLOSE")
    def showImg(self,img):
        height, width, bytesPerComponent = img.shape
        bytesPerLine = bytesPerComponent * width
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB,img)
        self.image = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.imgLabel.setPixmap(QPixmap.fromImage(self.image).scaled(self.imgLabel.width(), self.imgLabel.height()))

    def openFile(self):
        self.handFlag = 0
        self.autoFlag = 0
        if self.successFlag == 1:
            self.imgMagHand = copy.deepcopy(self.img)
            self.showImg(copy.deepcopy(self.img))
            self.imgMagAuto = copy.deepcopy(self.img)

        self.oneKey.setText("一键填充：CLOSE")
        self.handKey.setText("手动填充：CLOSE")

        fname, _ = QFileDialog.getOpenFileName(self, self.tr("Open Image"), 'c:\\',
                                           self.tr("Image Files(*.png *.jpg *.bmp)"))
        try:
            self.img ,self.soduko,self.sudoku= magPIC(fname)
            self.imgMagHand = copy.deepcopy(self.img)
            self.imgMagAuto = copy.deepcopy(self.img)

            self.successFlag = 1
            self.showImg(copy.deepcopy(self.img))
        except:
            self.successFlag = 0
            pass
    def handMagProcess(self,i,j):
        if self.successFlag == 1 and self.handFlag == 1:
            x = int((i + 0.25) * (350 / 9))
            y = int((j + 0.45) * (350 / 9))
            if (self.soduko[j][i] == 0):
                cv2.putText(self.imgMagHand, str(self.sudoku.value[j][i]), (x, y + 10), 3, 0.8, \
                            (255, 0, 0), 1, cv2.LINE_AA)
            self.showImg(copy.deepcopy(self.imgMagHand))

    def autoMagProcess(self):
        if  self.successFlag == 1 and self.autoFlag == 1:
            for i in range(9):
                for j in range(9):
                    x = int((i+0.25)*(350/9))
                    y = int((j+0.45)*(350/9))
                    if(self.soduko[j][i] == 0):
                        cv2.putText(self.imgMagAuto,str(self.sudoku.value[j][i]),(x,y+10), 3,0.8, \
                                    (255, 0, 0), 1, cv2.LINE_AA)
            self.showImg(copy.deepcopy(self.imgMagAuto))
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if event.pos().x()>10 and event.pos().x()<360 and \
                    event.pos().y()>10 and  event.pos().y()<360:
                handX = int((event.pos().x()-10)/(350 / 9))
                handY = int((event.pos().y()-10)/(350 / 9))
                self.handMagProcess(handX,handY)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = mainFramelessWindow(634,370)
    w.setWindowTitle('解数独')
    w.setWidget(mainFrame(), 0, 0, w.window())
    w.show()

    sys.exit(app.exec_())