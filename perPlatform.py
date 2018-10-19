from PyQt5.QtWidgets import QLabel, QFrame, QHBoxLayout, QVBoxLayout,QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QIcon
from config import PATH
import webbrowser

class PerPlatform(QLabel):
    def __init__(self,platformName,url,superEl):
        self.superEl = superEl
        super(PerPlatform, self).__init__(superEl)
        self.url = url
        self.setCursor(Qt.PointingHandCursor)
        self.img = QPixmap(f"{PATH}/src/img/platformicon/{platformName}.png")
        self.setPixmap(self.img)
        self.setFixedSize(16,16)
    def mousePressEvent(self, e):
        if (e.button() == Qt.LeftButton):
            webbrowser.open(self.url)



