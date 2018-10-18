from PyQt5.QtWidgets import QListWidget,QScrollArea,QScrollBar,QListWidgetItem
from PyQt5.QtCore import Qt
from .bangumiData import bangumiData

from .bangumiGeneralConfig import BangumiGeneralConfig

class ScheduleList(QListWidget):
    def __init__(self,superEl):
        self.superEl = superEl

        super(ScheduleList, self).__init__()
        self.setFixedWidth(200)
        self.setFixedHeight(750)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.initListContent()
        self.itemClicked.connect(self.myClickItem)
        self.myCurrentItem = None
    def myClickItem(self, item):
        self.superEl.superEl.rightColumn.bangumiGeneralConfig.setData(item.data)
        self.myCurrentItem = item


    def initListContent(self):
        for perBangumiData in bangumiData:
            self.addItem(ScheduleListItem(perBangumiData))


# class ScheduleListArea(QScrollArea):
#     def __init__(self):
#         super(ScheduleListArea, self).__init__()
#         self.setFixedWidth(200)
#
#         self.scrollBar = QScrollBar()
#         self.scrollBar.setCursor(Qt.PointingHandCursor)
#         self.setVerticalScrollBar(self.scrollBar)
#
#         self.content = ScheduleList()
#         self.setWidget(self.content)
class ScheduleListItem(QListWidgetItem):
    def __init__(self,perBangumiData):
        super(ScheduleListItem, self).__init__()
        if perBangumiData:
            self.setText(perBangumiData["title"])
        else:
            self.setText("番剧")
        self.data = perBangumiData
