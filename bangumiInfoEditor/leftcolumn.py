from PyQt5.QtWidgets import QFrame,QLabel,QListWidget,QVBoxLayout,QPushButton

from .schedulelist import ScheduleList
from .addschedulebutton import AddScheduleButton

class LeftColumn(QFrame):
    def __init__(self,superEl):
        super(LeftColumn, self).__init__()

        self.superEl = superEl

        self.initUplabel()
        self.initList()
        self.initAddScheduleButton()

        self.initLayout()

    def initUplabel(self):
        self.upLabel = QLabel()
        self.upLabel.setFixedWidth(200)
        self.upLabel.setFixedHeight(30)
        self.upLabel.setText("已添加任务:")

    def initList(self):
        self.scheduleList = ScheduleList(self)

    def initAddScheduleButton(self):
        self.addScheduleButton = AddScheduleButton(superEl=self)

    def initLayout(self):
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setContentsMargins(0, 0, 0, 0)

        self.mainLayout.addWidget(self.upLabel)
        self.mainLayout.addWidget(self.scheduleList)
        self.mainLayout.addWidget(self.addScheduleButton)

        self.setLayout(self.mainLayout)



