from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt
from .schedulelist import ScheduleListItem


class AddScheduleButton(QPushButton):
    def __init__(self, superEl):
        super(AddScheduleButton, self).__init__()
        self.setFixedWidth(200)
        self.setText("添加任务")
        self.superEl = superEl

    def mousePressEvent(self, e):
        if (e.button() == Qt.LeftButton):
            self.superEl.scheduleList.addItem(ScheduleListItem({
                "title": "新添番剧",
                "headImgSrc": "",
                "startChapter": 1,
                "startDate": "",
                "finishDate": "",
                "updateType": "weekly",
                "updateDay": "0",
                "updateTime": "00:00",
                "platFormTargetUrls": {
                    "default": "bilibili",
                    "bilibili": "https://www.bilibili.com/bangumi/media/md",
                    "iqiyi": "",
                    "qq": "",
                    "youku": "",
                    "acfun": "",
                    "migudm": "",
                    "mgtv": "",
                    "dmhy": "",
                    "niconico": ""
                },
                "follow": True
            }))
