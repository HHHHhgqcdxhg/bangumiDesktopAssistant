from PyQt5.QtWidgets import QLabel,QFrame
from PyQt5.QtCore import Qt
import datetime
from timeOpreat import weekDay2Str
from PyQt5.QtGui import QColor
from config import config

class TimeTodayLabel(QLabel):
    def __init__(self,superEl):
        self.superEl = superEl
        super(TimeTodayLabel, self).__init__()
        self.now = datetime.datetime.now()
        self.setTimeText()
        self.setCursor(Qt.SizeAllCursor)
        self.setAlignment(Qt.AlignCenter)
        self.setBgDisvisiable()
        self.setFixedHeight(30)

    def setTimeText(self):
        self.now = datetime.datetime.now()
        dateA = self.now.strftime("%Y-%m-%d-%w").split("-")
        weekDay = self.now.weekday()
        weekDayName = weekDay2Str(weekDay)
        dateS = f"{dateA[0]}年{dateA[1]}月{dateA[2]}日  {weekDayName}"
        self.setText(dateS)

    def reSetTimeText(self,now):
        self.now = now
        dateA = self.now.strftime("%Y-%m-%d-%w").split("-")
        weekDay = self.now.weekday()
        weekDayName = weekDay2Str(weekDay)
        dateS = f"{dateA[0]}年{dateA[1]}月{dateA[2]}日  {weekDayName}"
        self.setText(dateS)

    def setBgVisiable(self):
        self.setStyleSheet(f"background-color: {config.colors.topBg}")

    def setBgDisvisiable(self):
        self.setStyleSheet("background-color: rgba(0,255,0,0.01)")

    def mousePressEvent(self,e):
        if (e.button() == Qt.LeftButton):
            self.superEl.leftButtonOn = True
            ePos = e.globalPos()
            self.superEl.dragStartX, self.superEl.dragStartY = ePos.x(),ePos.y()
            self.superEl.windowX = self.superEl.x()
            self.superEl.windowY = self.superEl.y()

    def mouseReleaseEvent(self, e):
        if (e.button() == Qt.LeftButton):
            self.superEl.leftButtonOn = False

    def mouseMoveEvent(self, e):
        if self.superEl.leftButtonOn:
            ePos = e.globalPos()
            x,y = ePos.x(),ePos.y()
            self.superEl.move(x - self.superEl.dragStartX + self.superEl.windowX,y - self.superEl.dragStartY + self.superEl.windowY)

    def enterEvent(self, QEvent):
        self.setBgVisiable()

    def leaveEvent(self, QEvent):
        self.setBgDisvisiable()