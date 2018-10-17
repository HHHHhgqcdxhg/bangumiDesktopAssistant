from PyQt5.QtWidgets import QListWidget,QScrollArea,QScrollBar,QListWidgetItem
from PyQt5.QtCore import Qt
from bangumiData import bangumiData

class ScheduleList(QListWidget):
    def __init__(self):
        super(ScheduleList, self).__init__()
        self.setFixedWidth(200)
        self.setFixedHeight(750)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.initListContent()
        self.itemClicked.connect(self.myClickItem)

    def myClickItem(self, item):
        print(item.data)

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
        self.setText(perBangumiData["title"])
        self.data = perBangumiData
