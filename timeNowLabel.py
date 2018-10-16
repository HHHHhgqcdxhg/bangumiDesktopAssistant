from PyQt5.QtWidgets import QLabel,QFrame
from PyQt5.QtCore import Qt
import datetime
from config import config
class TimeNowLabel(QLabel):
    def __init__(self):
        super(TimeNowLabel, self).__init__()
        self.resetText()
        self.setStyleSheet(f"color:{config.colors.timeNowText};font-size:17px;font-weight:bold;")
        self.setFixedHeight(30)
    def resetText(self):
        self.setText(datetime.datetime.now().strftime("%H:%M:%S"))

