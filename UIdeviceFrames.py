# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIdeviceFrames.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_device(object):
    def setupUi(self, device):
        device.setObjectName("device")
        device.resize(634, 370)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(device.sizePolicy().hasHeightForWidth())
        device.setSizePolicy(sizePolicy)
        device.setStyleSheet("background-color: rgb(0, 11, 17);")
        self.gridLayout_3 = QtWidgets.QGridLayout(device)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 2, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem2, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 2, 0, 1, 1)
        self.gB_useBK = QtWidgets.QWidget(device)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gB_useBK.sizePolicy().hasHeightForWidth())
        self.gB_useBK.setSizePolicy(sizePolicy)
        self.gB_useBK.setMinimumSize(QtCore.QSize(634, 370))
        self.gB_useBK.setMaximumSize(QtCore.QSize(634, 370))
        self.gB_useBK.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.gB_useBK.setObjectName("gB_useBK")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gB_useBK)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.bkl = QtWidgets.QWidget(self.gB_useBK)
        self.bkl.setStyleSheet("background-color: rgb(25, 25, 25);")
        self.bkl.setObjectName("bkl")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bkl)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graphbk = QtWidgets.QWidget(self.bkl)
        self.graphbk.setMinimumSize(QtCore.QSize(350, 350))
        self.graphbk.setMaximumSize(QtCore.QSize(350, 350))
        self.graphbk.setStyleSheet("\n"
"background-color: rgb(85, 255, 255);")
        self.graphbk.setObjectName("graphbk")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.graphbk)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.imgLabel = QtWidgets.QLabel(self.graphbk)
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        self.horizontalLayout_3.addWidget(self.imgLabel)
        self.horizontalLayout.addWidget(self.graphbk)
        self.dsada = QtWidgets.QWidget(self.bkl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dsada.sizePolicy().hasHeightForWidth())
        self.dsada.setSizePolicy(sizePolicy)
        self.dsada.setMinimumSize(QtCore.QSize(257, 350))
        self.dsada.setMaximumSize(QtCore.QSize(257, 350))
        self.dsada.setStyleSheet("border-radius: 10px;\n"
"")
        self.dsada.setObjectName("dsada")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.dsada)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalWidget = QtWidgets.QWidget(self.dsada)
        self.verticalWidget.setMaximumSize(QtCore.QSize(259, 16777215))
        self.verticalWidget.setStyleSheet("\n"
"background-color: rgb(39, 39, 39);")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dsadsa = QtWidgets.QWidget(self.verticalWidget)
        self.dsadsa.setMinimumSize(QtCore.QSize(0, 0))
        self.dsadsa.setMaximumSize(QtCore.QSize(111111, 16777215))
        self.dsadsa.setObjectName("dsadsa")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dsadsa)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.read = QtWidgets.QPushButton(self.dsadsa)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.read.sizePolicy().hasHeightForWidth())
        self.read.setSizePolicy(sizePolicy)
        self.read.setMaximumSize(QtCore.QSize(16777215, 30))
        self.read.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 25 12pt \"微软雅黑 Light\";\n"
"border:0px solid white;\n"
"border-radius: 10px;\n"
" padding:5 0px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color:#C0C0C0; \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:#FEF4BF;\n"
"}\n"
"\n"
"")
        self.read.setObjectName("read")
        self.verticalLayout_3.addWidget(self.read)
        self.reset = QtWidgets.QPushButton(self.dsadsa)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset.sizePolicy().hasHeightForWidth())
        self.reset.setSizePolicy(sizePolicy)
        self.reset.setMinimumSize(QtCore.QSize(50, 0))
        self.reset.setMaximumSize(QtCore.QSize(16777215, 30))
        self.reset.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 25 12pt \"微软雅黑 Light\";\n"
"border:0px solid white;\n"
"border-radius: 10px;\n"
" padding:5 0px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color:#C0C0C0; \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:#FEF4BF;\n"
"}\n"
"\n"
"")
        self.reset.setObjectName("reset")
        self.verticalLayout_3.addWidget(self.reset)
        self.oneKey = QtWidgets.QPushButton(self.dsadsa)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oneKey.sizePolicy().hasHeightForWidth())
        self.oneKey.setSizePolicy(sizePolicy)
        self.oneKey.setMinimumSize(QtCore.QSize(50, 0))
        self.oneKey.setMaximumSize(QtCore.QSize(16777215, 30))
        self.oneKey.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 25 12pt \"微软雅黑 Light\";\n"
"border:0px solid white;\n"
"border-radius: 10px;\n"
" padding:5 0px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color:#C0C0C0; \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:#FEF4BF;\n"
"}\n"
"\n"
"")
        self.oneKey.setObjectName("oneKey")
        self.verticalLayout_3.addWidget(self.oneKey)
        self.handKey = QtWidgets.QPushButton(self.dsadsa)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.handKey.sizePolicy().hasHeightForWidth())
        self.handKey.setSizePolicy(sizePolicy)
        self.handKey.setMinimumSize(QtCore.QSize(50, 0))
        self.handKey.setMaximumSize(QtCore.QSize(16777215, 30))
        self.handKey.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 25 12pt \"微软雅黑 Light\";\n"
"border:0px solid white;\n"
"border-radius: 10px;\n"
" padding:5 0px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color:#C0C0C0; \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:#FEF4BF;\n"
"}\n"
"\n"
"")
        self.handKey.setObjectName("handKey")
        self.verticalLayout_3.addWidget(self.handKey)
        self.verticalLayout.addWidget(self.dsadsa)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.label = QtWidgets.QLabel(self.verticalWidget)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_5.addWidget(self.verticalWidget)
        self.horizontalLayout.addWidget(self.dsada)
        self.verticalLayout_2.addWidget(self.bkl)
        self.gridLayout_3.addWidget(self.gB_useBK, 1, 1, 2, 1)

        self.retranslateUi(device)
        QtCore.QMetaObject.connectSlotsByName(device)

    def retranslateUi(self, device):
        _translate = QtCore.QCoreApplication.translate
        device.setWindowTitle(_translate("device", "Form"))
        self.read.setText(_translate("device", "读取图片"))
        self.reset.setText(_translate("device", "图片复位"))
        self.oneKey.setText(_translate("device", "一键填充：close"))
        self.handKey.setText(_translate("device", "手动填充：close"))
        self.label.setText(_translate("device", "by:林 "))

