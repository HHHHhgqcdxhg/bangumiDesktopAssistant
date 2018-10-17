from PyQt5.QtWidgets import QFrame, QLabel, QListWidget, QVBoxLayout, QPushButton, QGridLayout, QTextEdit, QComboBox,QMessageBox,QFileDialog
from PyQt5.QtCore import Qt
import datetime
from makeChaptersInfo import BangumiChapters
class BangumiGeneralInfoEnterButton(QPushButton):
    def __init__(self, superEl):
        self.superEl = superEl
        super(BangumiGeneralInfoEnterButton, self).__init__()
        self.setText("保存")
        # self.mainLayout.addWidget(self.enterButton, 10, 0, 1, 7)

    def mousePressEvent(self, e):
        if (e.button() == Qt.LeftButton):
            try:
                if self.superEl.platformsEditor.platformSelector.myCurrentItem:
                    self.superEl.data["platFormTargetUrls"][self.superEl.platformsEditor.platformSelector.myCurrentItem.key] = self.superEl.platformsEditor.urlEditor.toPlainText()

                newData = {
                    "title": self.superEl.mainTitleEditor.toPlainText(),

                    "headImgSrc": self.superEl.headImagePathDisableLabel.text(),
                    "startChapter": int(self.superEl.firstUpdateChapterEditor.toPlainText()),
                    "startDate": self.superEl.startDateEditor.toPlainText(),
                    "finishDate": self.superEl.finalDateEditor.toPlainText(),
                    "updateTime": self.superEl.dayTimeEditor.toPlainText(),

                    "updateType": "weekly",

                    "updateDay": self.superEl.updateDayEditor.toPlainText(),
                    "platFormTargetUrls": self.superEl.data["platFormTargetUrls"],
                    "follow": True
                }
                if self.superEl.updateTypeComboBox.currentText() == "月更":
                    newData["updateType"] = "monthly"
                if self.superEl.followComboBox.currentText() == "否":
                    newData["follow"] = False
                BangumiChapters(newData)
            except:
                QMessageBox.critical(self, "错误", "请正确填写且不能留空")
