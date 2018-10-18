from PyQt5.QtWidgets import QLabel,QFrame
from PyQt5.QtCore import Qt
import datetime
from config import config
class TimeNowLabel(QLabel):
    def __init__(self):
        super(TimeNowLabel, self).__init__()
        self.resetText()
        self.setContentsMargins(10,0,0,0)
        self.setStyleSheet(f"color:{config.colors.timeNowText};font-size:17px;font-weight:bold;background-color:{config.colors.timeNowBg};border-radius:10px")
        self.setFixedHeight(30)
        self.setFixedWidth(102)
    def resetText(self):
        self.setText(datetime.datetime.now().strftime("%H:%M:%S"))

