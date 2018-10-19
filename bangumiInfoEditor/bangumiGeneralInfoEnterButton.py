from PyQt5.QtWidgets import QFrame, QLabel, QListWidget, QVBoxLayout, QPushButton, QGridLayout, QTextEdit, QComboBox,QMessageBox,QFileDialog
from PyQt5.QtCore import Qt
import datetime,json
from .makeChaptersInfo import BangumiChapters
from config import PATH
class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


class BangumiGeneralInfoEnterButton(QPushButton):
    def __init__(self, superEl):
        self.superEl = superEl
        super(BangumiGeneralInfoEnterButton, self).__init__()
        self.setText("保存")
        # self.mainLayout.addWidget(self.enterButton, 10, 0, 1, 7)

    def mousePressEvent(self, e):
        if (e.button() == Qt.LeftButton):
            try:
                self.superEl.lastSetPlatformData()
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

                if newData["updateType"] == "weekly":
                    if not newData["updateDay"] in ["周一","周二","周三","周四","周五","周六","周日"]:
                        QMessageBox.critical(self, "错误", "周更番的更新日请填周一到周日中的一个")
                else:
                    try:
                        if not int(newData["updateDay"]) in range(1,31):
                            raise Exception()
                    except:
                        QMessageBox.critical(self, "错误", "月更番的更新日请填入1~31之间的数字!")
                bangumiChapters = BangumiChapters(newData)
                # self -> bangumiGeneralConfig -> rightColumn -> BangumiInfoEditorWindow
                scheduleList = self.superEl.superEl.superEl.leftColumn.scheduleList
                scheduleList.myCurrentItem.setText(bangumiChapters.title)
                scheduleList.myCurrentItem.data = bangumiChapters
                with open(f"{PATH}/src/db/bangumisInfo/{bangumiChapters.title}.json","w+",encoding="utf8") as f:
                    writeDict = bangumiChapters.makeDict()
                    json.dump(writeDict,f,ensure_ascii=False,cls=CJsonEncoder)
                # print(self.superEl.superEl.superEl.leftColumn.scheduleList.myCurrentItem.text())

                QMessageBox.about(self, "设置成功!", "设置成功!\n请重启桌面挂件以应用设置!")
            except Exception as e:
                stre = str(e)
                if stre == "noImage":
                    QMessageBox.critical(self, "错误", "请添加图片")
                elif stre == "noTitle":
                    QMessageBox.critical(self, "错误", "标题不可以为新添番剧!")
                else:
                    QMessageBox.critical(self, "错误", "请正确填写且不能留空")

