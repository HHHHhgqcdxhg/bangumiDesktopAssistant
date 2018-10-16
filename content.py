from PyQt5.QtWidgets import QLabel,QFrame,QVBoxLayout,QScrollArea,QScrollBar
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from config import config

from perBangumiEl import PerBangumi
from bangumiInfoHandler import BangumuInfo

class ContentHolder(QScrollArea):
    def __init__(self):
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


class Content(QFrame):
    def __init__(self,superEl):
        self.superEl = superEl
        super(Content, self).__init__()
        self.setStyleSheet(f"background-color: {config.colors.contentBg}")

        self.mainLayout = QVBoxLayout()


        bangumiChapters = BangumuInfo.factory()
        for bangumiChapter in bangumiChapters:
            p = PerBangumi(bangumiChapter)
            self.mainLayout.addWidget(p)
            self.setLayout(self.mainLayout)



