from PyQt5.QtWidgets import QFrame,QLabel,QListWidget,QVBoxLayout,QPushButton,QGridLayout,QTextEdit,QComboBox,QFileDialog,QHBoxLayout,QListWidgetItem
import json
class PlatformSelector(QListWidget):
    def __init__(self):
        super(PlatformSelector, self).__init__()
        self.setFixedSize(100,200)
        with open("db/platforms.json","r",encoding="utf8") as f:
            platforms = json.load(f)
        for platformKey,platform in platforms.items():

            self.addItem(PlatformListItem(platformKey,platform["name"]))
        self.itemClicked.connect(self.clickPlatform)

    def clickPlatform(self, item):
        print(item.key)

class PlatformListItem(QListWidgetItem):
    def __init__(self,platformKey,platformName):
        super(PlatformListItem, self).__init__()
        self.setText(platformName)
        self.key = platformKey
