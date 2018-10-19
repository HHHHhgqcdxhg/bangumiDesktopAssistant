from PyQt5.QtWidgets import QFrame,QLabel,QListWidget,QVBoxLayout,QPushButton

from bangumiGeneralConfig import BangumiGeneralConfig

class RightColumn(QFrame):
    def __init__(self,superEl):
        self.superEl = superEl
        super(RightColumn, self).__init__()
        self.setFixedWidth(1400)
        self.setFixedHeight(800)
        # self.setStyleSheet("background-color:yellow;")

        self.initUI()

        self.initLayout()

    def initUI(self):
        # self.bangumiGeneralConfig = bangumiGeneralConfig
        self.bangumiGeneralConfig = BangumiGeneralConfig(self)

    def initLayout(self):
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setContentsMargins(0, 0, 0, 0)

        self.mainLayout.addWidget(self.bangumiGeneralConfig)

        self.setLayout(self.mainLayout)

