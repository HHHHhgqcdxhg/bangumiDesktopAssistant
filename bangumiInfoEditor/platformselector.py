from PyQt5.QtWidgets import QFrame,QLabel,QListWidget,QVBoxLayout,QPushButton,QGridLayout,QTextEdit,QComboBox,QFileDialog,QHBoxLayout,QListWidgetItem
import json
from config import PATH
class PlatformSelector(QListWidget):
    def __init__(self,superEl):
        self.superEl = superEl
        super(PlatformSelector, self).__init__()

        self.setFixedSize(100,200)
        self.bangumiPlatforms = {}
        with open(f"{PATH}/db/platforms.json","r",encoding="utf8") as f:
            platforms = json.load(f)
        for platformKey,platform in platforms.items():
            self.bangumiPlatforms[platformKey] = {
                "playformEl":PlatformListItem(platformKey,platform["name"]),
                "url":""
            }
            self.addItem(self.bangumiPlatforms[platformKey]["playformEl"])
        self.itemClicked.connect(self.clickPlatform)
        self.myCurrentItem = None



    def clickPlatform(self, item):
        try:
            if self.myCurrentItem:
                self.superEl.superEl.lastSetPlatformData()
                # self.superEl.superEl.data["platFormTargetUrls"][self.myCurrentItem.key] = self.superEl.urlEditor.toPlainText()
            self.myCurrentItem = item

            self.superEl.urlEditor.setText(self.superEl.superEl.data["platFormTargetUrls"][item.key])
            if self.superEl.superEl.data["platFormTargetUrls"]["default"] == item.key:
                self.superEl.checkBox.setCheckState(True)
            else:
                self.superEl.checkBox.setCheckState(False)
        except:
            self.superEl.urlEditor.setText("")

    # def initData(self):
    #     self.

class PlatformListItem(QListWidgetItem):
    def __init__(self,platformKey,platformName):
        super(PlatformListItem, self).__init__()
        self.setText(platformName)
        self.key = platformKey
