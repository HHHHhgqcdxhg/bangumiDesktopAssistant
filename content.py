from PyQt5.QtWidgets import QLabel,QFrame,QVBoxLayout,QScrollArea,QScrollBar
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from config import config

from perBangumiEl import PerBangumi
from bangumiInfoHandler import BangumuInfo
from config import PATH

from timeOperate import time1Minutes,time1seconds
import datetime,sip
class ContentHolder(QScrollArea):
    def __init__(self,superEl):
        self.superEl = superEl
        super(ContentHolder, self).__init__()

        self.scrollBar = QScrollBar()

        self.scrollBar.setCursor(Qt.PointingHandCursor)
        self.setVerticalScrollBar(self.scrollBar)
        # self.setCursor()
        self.content = Content(self)
        self.setWidget(self.content)
        with open(f"{PATH}/src/style/scrollbar.qss", "r",encoding="utf8") as f:
            qssContent = f.read()
        self.setStyleSheet(qssContent)

    #     self.scrollBar.valueChanged.connect(self.fff)
    # def fff(self):
    #     print(self.scrollBar.value())
    # def enterEvent(self, QEvent):
    #     self.superEl.entered = True
    #     self.active()
    # def leaveEvent(self, QEvent):
    #     self.superEl.entered = False
    #     self.disActive()

    def active(self):
        self.content.setStyleSheet(f"background-color: {config.colors.contentDisplayBg}")
        # self.contentHolder.scrollBar.setValue(0)

    def disActive(self):
        self.content.setStyleSheet(f"background-color: {config.colors.contentBg}")


    def setScrollBarValue(self,n):
        # print(1)
        # h=self.height()
        # l = self.content.bangumiChapters.__len__()
        # ratio = (n - 1)/l
        # mi = self.scrollBar.minimum()
        # m = self.scrollBar.maximum()
        # value = ratio * m + h/2 - (m / l)/2
        # self.scrollBar.setValue(int(value))
        # m = self.scrollBar.maximum()
        # l = self.content.bangumiChapters.__len__()
        # self.scrollBar.setValue(int((n/l) * m + self.height()/2))
        self.scrollBar.setValue(n * 106 + 6)

class Content(QFrame):
    def __init__(self,superEl:ContentHolder):
        self.superEl = superEl
        super(Content, self).__init__()
        self.setStyleSheet(f"background-color: {config.colors.contentBg}")

        self.mainLayout = QVBoxLayout()
        self.nextDatetime = None
        self.nextIndex = 0

        self.bangumiChaptersEls = []
        self.setChildren()


    def setChildren(self):
        self.bangumiChapters = BangumuInfo.factory()
        for bangumiChapter in self.bangumiChapters:
            p = PerBangumi(bangumiChapter)
            self.bangumiChaptersEls.append(p)
            self.mainLayout.addWidget(p)
        self.setLayout(self.mainLayout)
        self.findNext()

    def removeChildren(self):
        for bangumiChapterEl in self.bangumiChaptersEls:
            # self.mainLayout.removeItem(bangumiChapterEl)
            self.mainLayout.removeWidget(bangumiChapterEl)
            sip.delete(bangumiChapterEl)
        self.bangumiChaptersEls = []

    def reloadChildren(self):
        self.removeChildren()
        self.setChildren()
        self.findNext()
        self.superEl.superEl.needSetScrollBarValue = self.nextIndex - 1
        self.superEl.setScrollBarValue(self.superEl.superEl.needSetScrollBarValue)


    def findNext(self):
        now = datetime.datetime.now()
        for x in range(self.bangumiChapters.__len__()):
            if self.bangumiChapters[x].updateTime - now >= time1seconds:
                self.nextDatetime = self.bangumiChapters[x].updateTime
                self.nextIndex = x
                return x
