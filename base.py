# !/usr/bin/env python
# -*- coding:utf-8 -*-


from PyQt5.QtGui import QFont, QEnterEvent, QPainter, QColor, QPen,QPainterPath,QBrush,QIcon
from PyQt5.QtCore import Qt,QPoint,QRect,pyqtSignal,QObject,QSize,QEvent
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit,QRadioButton,QCheckBox\
, QLineEdit,QScrollBar,QListWidget,QTableView,QSlider,QScrollArea,QToolButton,QHBoxLayout,QLabel\
,QSpacerItem,QSizePolicy,QGridLayout,QFrame,QAbstractItemView,QListWidgetItem,QGroupBox,QFrame\
    ,QListView,QDesktopWidget

windowsHandle = {}


class TitleBar(QWidget):
    windowMinimumed = pyqtSignal()
    windowMaximumed = pyqtSignal()
    windowNormaled = pyqtSignal()
    windowClosed = pyqtSignal()
    windowMoved = pyqtSignal(QPoint)

    def __init__(self,*args, **kwargs):
        super(TitleBar, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.mPos = None
        self.iconSize = 20
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(palette.Window, QColor(240, 240, 240))
        self.setPalette(palette)
        layout = QHBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.iconLabel = QLabel(self)
        layout.addWidget(self.iconLabel)
        self.titleLabel = QLabel(self)
        self.titleLabel.setMargin(2)
        self.titleLabel.setObjectName("titleLabel")
        layout.addWidget(self.titleLabel)
        layout.addSpacerItem(QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        font = self.font() or QFont()
        font.setFamily('Webdings')

        self.dialog = args[1]

        if self.dialog ==False:
            self.buttonMinimum = QPushButton(
                '0', self, clicked=self.windowMinimumed.emit, font=font, objectName='buttonMinimum')
            layout.addWidget(self.buttonMinimum)
            self.buttonClose = QPushButton(
                'r', self, clicked=self.windowClosed.emit, font=font, objectName='buttonClose')
            layout.addWidget(self.buttonClose)
        else:
            self.buttonClose = QPushButton(
                'r', self, clicked=self.windowClosed.emit, font=font, objectName='buttonClose')
            layout.addWidget(self.buttonClose)

        self.setHeight()

    def showMaximized(self):
        if self.buttonMaximum.text() == '1':
            self.buttonMaximum.setText('2')
            self.windowMaximumed.emit()
        else:
            self.buttonMaximum.setText('1')
            self.windowNormaled.emit()

    def setHeight(self, height=38):
        self.setMinimumHeight(height)
        self.setMaximumHeight(height)
        if self.dialog == False:
            self.buttonMinimum.setMinimumSize(height, height)
            self.buttonMinimum.setMaximumSize(height, height)
            #self.buttonMaximum.setMinimumSize(height, height)
            #self.buttonMaximum.setMaximumSize(height, height)
            self.buttonClose.setMinimumSize(height, height)
            self.buttonClose.setMaximumSize(height, height)
        else:
            self.buttonClose.setMinimumSize(height, height)
            self.buttonClose.setMaximumSize(height, height)

    def setTitle(self, title):
        self.titleLabel.setText(title)


    def setIcon(self, icon):
        self.iconLabel.setPixmap(icon.pixmap(self.iconSize, self.iconSize))

    def setIconSize(self, size):
        self.iconSize = size

    def enterEvent(self, event):
        self.setCursor(Qt.ArrowCursor)
        super(TitleBar, self).enterEvent(event)

    def mouseDoubleClickEvent(self, event):
        super(TitleBar, self).mouseDoubleClickEvent(event)
        self.showMaximized()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mPos = event.pos()
        event.accept()

    def mouseReleaseEvent(self, event):
        self.mPos = None
        event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.mPos:
            self.windowMoved.emit(self.mapToGlobal(event.pos() - self.mPos))
        event.accept()


Left, Top, Right, Bottom, LeftTop, RightTop, LeftBottom, RightBottom = range(8)

class FramelessWindow(QWidget):

    Margins = 5

    def __init__(self, frame_x, frame_y, *args, **kwargs):
        super(FramelessWindow, self).__init__()
        self._pressed = False
        self.Direction = None
        self.loop = None
        try:
            self.dialog = args[0]['dialog']
            self.setParent(args[0]['parent'])
        except:
            self.dialog = False

        self.setStyleSheet("\n"
"QTitleLabel{\n"
"        color:white;\n"
"        background-color: rgb(45,45,45);\n"
"        font: 100 10pt;\n"
"}\n"
"\n"
"#MinMaxButton{\n"
"        background-color: rgba(255, 255, 255, 0);\n"
"        color: white;\n"
"        border: 0px;\n"
"        font: 100 10pt;\n"
"}\n"
"#MinMaxButton:hover{\n"
"        background-color: #D0D0D1;\n"
"        color: black;\n"
"        border: 0px;\n"
"        font: 100 10pt;\n"
"}\n"
"\n"
"#CloseButton:hover{\n"
"        background-color: #D32424;\n"
"        color: white;\n"
"        border: 0px;\n"
"        font: 100 10pt;\n"
"}\n"
"\n"
"QLineEdit{\n"
"        color:white;\n"
"        background-color: rgba(43,43,43,255);\n"
"}\n"
"QTextBrowser#show_text{\n"
"    color: #ffffff;\n"
"    background-color: #323232;\n"
"}\n"
"QTextBrowser#show_text:hover{\n"
"    color: #ffffff;\n"
"    background-color:black;\n"
"}\n"
"QPushButton#start_end{\n"
"    color: black;\n"
"    background-color: white;\n"
"\n"
"}\n"
"QPushButton#start_end:hover{\n"
"    color:white;\n"
"    background-color: black;\n"
"}\n"
"\n"
"QWidget#app{\n"
"    background-color: #c0c0c0;\n"
"}\n"
"QWidget#app:hover{\n"
"    background-color: red;\n"
"}\n"
"\n"
"#titleLabel {\n"
"    color:white;\n"
"}\n"
"\n"
"TitleBar {\n"
"    background-color: rgb(45,45,45);\n"
"    font: 100 10pt;\n"
"    color:red;\n"
"}\n"
"\n"
"\n"
"#buttonMinimum,#buttonMaximum,#buttonClose {\n"
"    border: none;\n"
"    color:white;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"#buttonMinimum:hover,#buttonMaximum:hover {\n"
"    background-color: #D0D0D1;\n"
"    color: black;\n"
"}\n"
"#buttonClose:hover {\n"
"    background-color: #D32424;\n"
"    color: white;\n"
"}\n"
"\n"
"#buttonMinimum:pressed,#buttonMaximum:pressed {\n"
"    background-color: rgb(44, 125, 144);\n"
"}\n"
"#buttonClose:pressed {\n"
"    color: white;\n"
"    background-color: rgb(161, 73, 92);\n"
"}\n"
"\n"
"QPushButton {\n"
"        color: white;\n"
"}\n"
"QPushButton:enabled {\n"
"        background-color: rgb(16, 58, 72);\n"
"        color: white;\n"
"}\n"
"QPushButton:!enabled {\n"
"        background: gray;\n"
"        color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:enabled:hover {\n"
"        background: rgb(0, 180, 255);\n"
"}\n"
"QPushButton:enabled:pressed {\n"
"        background: rgb(0, 140, 215);\n"
"}\n"
"\n"
"\n"
"\n"
"QGroupBox{\n"
"        border: 0px ;\n"
"        background-color: rgb(2, 28, 41);\n"
"}\n"
"\n"
"QGroupBox#gB_showBK,#gB_sysMsgBK,#gB_toolBK,#gB_channelBK{\n"
"        border: 0px ;\n"
"        background-color: rgb(2, 28, 41);\n"
"}\n"
"\n"
"\n"
"QGroupBox#gb_channel,#gB_tool,#gB_sysMsg,#gB_run,#gB_file,#gB_set,#gB_help{\n"
"   border: 2px solid rgb(20,77,107);\n"
"   padding-top: 7px;\n"
"   margin-top:9px;\n"
"   font: 12pt \\\"楷体\\\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(2, 28, 41);\n"
" }\n"
"QGroupBox#gb_channel:title,#gB_tool:title,#gB_sysMsg:title,#gB_run:title ,\n"
"#gB_help:title,#gB_set:title,#gB_file:title{\n"
"\n"
"   subcontrol-origin: margin;\n"
"   subcontrol-position: top left;\n"
"   left:25px;\n"
"   margin-left: 0px;\n"
"   padding:0 1px;\n"
"}\n"
"QGroupBox#widget_show{\n"
"   border-radius: 5px;\n"
"   border: 0px solid #636363;\n"
"}\n"
"\n"
"QGroupBox#gB_config{\n"
"    border: 0px solid rgb(20,77,107);\n"
"    padding-top: 0px;\n"
"   margin-top:0px;\n"
"   font: 12pt \\\"楷体\\\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 11, 17);\n"
"}\n"
"QGroupBox#gB_config:title{\n"
"     subcontrol-origin: margin;\n"
"     subcontrol-position: top left;\n"
"     left:25px;\n"
"     margin-left: 0px;\n"
"     padding:0 0px;\n"
"}\n"
"\n"
"QLabel{\n"
"    color: rgb(170, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"QWidget#bkwidget{\n"
"    background-color: rgb(0, 11, 17)\n"
"}\n"
"\n"
"")


        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setMouseTracking(True)
        layout = QVBoxLayout(self, spacing=0)
        layout.setContentsMargins(
            self.Margins, self.Margins, self.Margins, self.Margins)
        self.titleBar = TitleBar(self,self.dialog)
        layout.addWidget(self.titleBar)
        if self.dialog == False:
            self.titleBar.windowMinimumed.connect(self.showMinimized)
            self.titleBar.windowMaximumed.connect(self.showMaximized)
            self.titleBar.windowNormaled.connect(self.showNormal)
            self.titleBar.windowClosed.connect(self.close)
            self.titleBar.windowMoved.connect(self.move)
            self.windowTitleChanged.connect(self.titleBar.setTitle)
            self.windowIconChanged.connect(self.titleBar.setIcon)
        else:
            self.titleBar.windowClosed.connect(self.close)
            self.titleBar.windowMoved.connect(self.move)
            self.setWindowModality(Qt.WindowModal)
            self.setWindowFlag(Qt.Dialog)
            self.loop = 1

        screen_x = QDesktopWidget().availableGeometry().width()
        screen_y = QDesktopWidget().availableGeometry().height()

        geometry = self.geometry()
        x, y, w, h = geometry.x(), geometry.y(), geometry.width(), geometry.height()
        self.setGeometry((screen_x-frame_x)/2,(screen_y-frame_y)/2,frame_x,frame_y)

        self._pressed =False
    def eventFilter(self, obj, event):
        if isinstance(event, QEnterEvent):
            self.setCursor(Qt.ArrowCursor)
        return super(FramelessWindow, self).eventFilter(obj, event)
    def setTitleBarHeight(self, height=38):
        self.titleBar.setHeight(height)

    def setIconSize(self, size):
        self.titleBar.setIconSize(size)

    def setWidget(self, widget, sign, handle , handleName):
        if hasattr(self, '_widget'):
            return
        if handle!=0:
            self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self._widget = widget
        self._widget.setAutoFillBackground(True)
        palette = self._widget.palette()
        palette.setColor(palette.Window, QColor(240, 240, 240))
        self._widget.setPalette(palette)
        self._widget.installEventFilter(self)
        self.layout().addWidget(self._widget)

    def close(self):
        self.deleteLater()

    def changeWinSize(self,frameX,frameY):
        screen_x = QDesktopWidget().availableGeometry().width()
        screen_y = QDesktopWidget().availableGeometry().height()
        geometry = self.geometry()
        x, y, w, h = geometry.x(), geometry.y(), geometry.width(), geometry.height()
        self.setGeometry((screen_x - frameX) / 2, (screen_y - frameY) / 2, frameX, frameY)

    def move(self, pos):
        if self.windowState() == Qt.WindowMaximized or self.windowState() == Qt.WindowFullScreen:
            return
        super(FramelessWindow, self).move(pos)

    def showMaximized(self):
        super(FramelessWindow, self).showMaximized()
        self.layout().setContentsMargins(0, 0, 0, 0)

    def showNormal(self):
        super(FramelessWindow, self).showNormal()
        self.layout().setContentsMargins(
            self.Margins, self.Margins, self.Margins, self.Margins)



    def paintEvent(self, event):
        super(FramelessWindow, self).paintEvent(event)

        m = 9

        path = QPainterPath()
        path.setFillRule(Qt.WindingFill)
        path.addRect(m, m, self.width() - m * 2, self.height() - m * 2)

        painter = QPainter(self)
        painter.fillPath(path, QBrush(Qt.white))

        color = QColor(100, 100, 100, 100)
        for i in range(m):
            path = QPainterPath()
            path.setFillRule(Qt.WindingFill)
            path.addRoundedRect(m - i, m - i, self.width() - (m - i) * 2, self.height() - (m - i) * 2, 1, 1)
            color.setAlpha(100-10*i)
            painter.setPen(QPen(color, 1, Qt.SolidLine))
            painter.drawRoundedRect(QRect(m - i, m - i, self.width() - (m - i) * 2, self.height() - (m - i) * 2), 0, 0)

    def focusInEvent(self, QFocusEvent):
        pass
    def focusOutEvent(self, QFocusEvent):
        pass
    def actionEvent(self, QActionEvent):
        pass
    def _resizeWidget(self, pos):
        if self.Direction == None:
            return
        mpos = pos - self._mpos
        xPos, yPos = mpos.x(), mpos.y()
        geometry = self.geometry()
        x, y, w, h = geometry.x(), geometry.y(), geometry.width(), geometry.height()
        if self.Direction == LeftTop:
            if w - xPos > self.minimumWidth():
                x += xPos
                w -= xPos
            if h - yPos > self.minimumHeight():
                y += yPos
                h -= yPos
        elif self.Direction == RightBottom:
            if w + xPos > self.minimumWidth():
                w += xPos
                self._mpos = pos
            if h + yPos > self.minimumHeight():
                h += yPos
                self._mpos = pos
        elif self.Direction == RightTop:
            if h - yPos > self.minimumHeight():
                y += yPos
                h -= yPos
            if w + xPos > self.minimumWidth():
                w += xPos
                self._mpos.setX(pos.x())
        elif self.Direction == LeftBottom:
            if w - xPos > self.minimumWidth():
                x += xPos
                w -= xPos
            if h + yPos > self.minimumHeight():
                h += yPos
                self._mpos.setY(pos.y())
        elif self.Direction == Left:
            if w - xPos > self.minimumWidth():
                x += xPos
                w -= xPos
            else:
                return
        elif self.Direction == Right:
            if w + xPos > self.minimumWidth():
                w += xPos
                self._mpos = pos
            else:
                return
        elif self.Direction == Top:
            if h - yPos > self.minimumHeight():
                y += yPos
                h -= yPos
            else:
                return
        elif self.Direction == Bottom:
            if h + yPos > self.minimumHeight():
                h += yPos
                self._mpos = pos
            else:
                return
        self.setGeometry(x, y, w, h)

