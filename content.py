from PyQt5.QtWidgets import QLabel,QFrame,QVBoxLayout,QScrollArea,QScrollBar
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from config import config

from perBangumiEl import PerBangumi
from bangumiInfoHandler import BangumuInfo


import datetime,math
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
        with open("src/style/scrollbar.qss", "r",encoding="utf8") as f:
            qssContent = f.read()
        self.setStyleSheet(qssContent)

    #     self.scrollBar.valueChanged.connect(self.fff)
    # def fff(self):
    #     print(self.scrollBar.value())
    def enterEvent(self, QEvent):
        self.superEl.entered = True
        self.active()
    def leaveEvent(self, QEvent):
        self.superEl.entered = False
        self.disActive()

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


        self.bangumiChapters = BangumuInfo.factory()

        self.nextIndex = 0
        for bangumiChapter in self.bangumiChapters:
            p = PerBangumi(bangumiChapter)
            self.mainLayout.addWidget(p)
        self.setLayout(self.mainLayout)

        self.findNext()

    def findNext(self):
        now = datetime.datetime.now()
        for x in range(self.nextIndex,self.bangumiChapters.__len__()):
            if self.bangumiChapters[x].updateTime > now:
                self.nextIndex = x
                return x
