from PyQt5.QtWidgets import QCheckBox, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer

from timeNowLabel import TimeNowLabel
from timeTodayLabel import TimeTodayLabel
from content import ContentHolder

from config import config
from bangumiSystemTray import BangumiSystemTray
import playAlarmAudio
from timeOpreat import *
import threading

class MainWindow(QWidget):
    def __init__(self,app):
        super(MainWindow, self).__init__()
        self.app = app
        self.move(config.mainWindowOffset[0],config.mainWindowOffset[1])
        self.initSystemTray()
        self.setMouseTracking(True)
        self.leftButtonOn = False
        self.initUI()
        self.initChildren()

        self.qTimer = QTimer(self)
        self.qTimer.timeout.connect(self.timer)
        self.qTimer.start(1000)
        self.entered = False
        self.nextLeaveTask = -1

        self.contentHolder.content.findNext()
        self.needSetScrollBarValue = self.contentHolder.content.nextIndex - 1
        self.contentHolder.setScrollBarValue(self.needSetScrollBarValue)

    def timer(self):
        self.now = datetime.datetime.now()
        self.timeNowLabel.setText(self.now.strftime("%H:%M:%S"))
        if self.contentHolder.content.nextDatetime - self.now <= time1seconds:
            self.contentHolder.content.findNext()
            self.nextLeaveTask = 1
            self.needSetScrollBarValue = self.contentHolder.content.nextIndex - 1
            audioThread = threading.Thread(target=playAlarmAudio.play)
            audioThread.start()

        if not (self.now.hour or self.now.minute or self.now.second):
            self.timeTodayLabel.setTimeText()

        if not self.entered:
            if self.nextLeaveTask > 0:
                self.nextLeaveTask -= 1
            elif self.nextLeaveTask == 0:
                self.nextLeaveTask -= 1
                self.setWindowOpacity(config.mainWindowUnfocusedOpacity)
                self.contentHolder.setScrollBarValue(self.needSetScrollBarValue)
                self.contentHolder.disActive()

    def initUI(self):
        # 设置大小
        self.resize(config.mainWindowWid, config.mainWindowHei)
        # 去除背景
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 去除边框,从任务栏隐藏,窗口置顶
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.SplashScreen | Qt.WindowStaysOnTopHint)
        # 窗口透明度
        self.setWindowOpacity(config.mainWindowUnfocusedOpacity)
        # 窗口颜色
        # self.setStyleSheet("background-color: rgba(255,255,0,1)")
        self.initLayout()

    def initLayout(self):
        self.mainLayout = QVBoxLayout()

    def initChildren(self):
        self.timeTodayLabel = TimeTodayLabel(self)
        self.mainLayout.addWidget(self.timeTodayLabel)
        self.timeNowLabel = TimeNowLabel()
        self.mainLayout.addWidget(self.timeNowLabel)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)

        self.contentHolder = ContentHolder(self)
        self.mainLayout.addWidget(self.contentHolder)

        # self.mainLayout.setStretchFactor(self.timeTodayLabel,1)
        # self.mainLayout.setStretchFactor(self.timeNowLabel, 1)
        # self.mainLayout.setStretchFactor(self.content, 20)
        self.setLayout(self.mainLayout)

    def leaveEvent(self, QEvent):
        self.entered = False
        self.nextLeaveTask = 1
        self.needSetScrollBarValue = self.contentHolder.content.nextIndex - 1

    def enterEvent(self, QEvent):
        self.entered = True
        self.setWindowOpacity(config.mainWindowFocusedOpacity)
        self.contentHolder.active()

    # def enterEvent(self, QEvent):
    #
    # def leaveEvent(self, QEvent):

    def initSystemTray(self):
        self.systemTray = BangumiSystemTray(self)


if __name__ == '__main__':
    mainWindow = MainWindow()
    mainWindow.show()
