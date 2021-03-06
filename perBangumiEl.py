from config import config
from PyQt5.QtWidgets import QLabel, QFrame, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
import datetime
import webbrowser
from timeOperate import time1Days, weekDay2Str, time7Days, timeZero, time14Days
from config import PATH
import perPlatform


class PerBangumi(QFrame):
    def __init__(self, bangumiInfo):
        super(PerBangumi, self).__init__()
        self.bangumiInfo = bangumiInfo
        self.initUI()

    def initUI(self):
        self.setFixedWidth(272)
        self.setFixedHeight(100)
        # self.setStyleSheet(f"background-color: red")
        self.mainLayout = QHBoxLayout()
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.addWidget(PerBangumiTimeFrame(self.bangumiInfo.updateTime))
        self.mainLayout.addWidget(PerBangumiImg(self.bangumiInfo.imgSrc, self.bangumiInfo.url))
        self.mainLayout.addWidget(
            PerBangumiInfo(self.bangumiInfo.title, self.bangumiInfo.chapter, self.bangumiInfo.platformsInfo))
        self.setLayout(self.mainLayout)


class PerBangumiTimeFrame(QFrame):
    def __init__(self, updateTime: datetime.datetime):
        super(PerBangumiTimeFrame, self).__init__()
        self.setFixedWidth(70)
        self.setFixedHeight(28)
        self.setStyleSheet(f"background-color:{config.colors.bangumiTimeBg};border-radius:8px;")
        self.mainLayout = QHBoxLayout()
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.addWidget(PerBangumiTimeDotLabel())
        now = datetime.datetime.now()
        thisWeekLastDays = datetime.timedelta(days=6 - now.weekday())
        if updateTime.date() == now.date():
            updateTimeText = f"今天\n{updateTime.strftime('%H:%M')}"
        elif updateTime.date() == now.date() + time1Days:
            updateTimeText = f"明天\n{updateTime.strftime('%H:%M')}"
        elif timeZero <= updateTime.date() - now.date() <= thisWeekLastDays:
            updateTimeDay = updateTime.weekday()
            updateTimeWeekDay = weekDay2Str(updateTimeDay)
            updateTimeText = f"{updateTimeWeekDay}\n{updateTime.strftime('%H:%M')}"
        elif thisWeekLastDays <= updateTime.date() - now.date() <= time7Days + thisWeekLastDays:
            updateTimeDay = updateTime.weekday()
            updateTimeWeekDay = weekDay2Str(updateTimeDay)
            updateTimeText = f"下{updateTimeWeekDay}\n{updateTime.strftime('%H:%M')}"
        else:
            updateTimeText = f"{updateTime.strftime('%m-%d')}\n{updateTime.strftime('%H:%M')}"
        self.mainLayout.addWidget(PerBangumiTimeLabel(updateTimeText))
        self.setLayout(self.mainLayout)
        # self.setStyleSheet("background-color:green;")


class PerBangumiTimeDotLabel(QLabel):
    def __init__(self):
        super(PerBangumiTimeDotLabel, self).__init__()
        self.setStyleSheet(
            f"background:transparent;margin:0;font-size:27px;color:{config.colors.dotBeforBangumiTime};")
        self.setFixedWidth(17)
        self.setText("·")
        # self.resize(20, 10)
        # self.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        # self.setText("first line\nsecond line")
        # self.setAlignment(Qt.AlignBottom | Qt.AlignRight)


class PerBangumiTimeLabel(QLabel):
    def __init__(self, updateTimeText: str):
        super(PerBangumiTimeLabel, self).__init__()
        self.setStyleSheet(f"background:transparent;color:{config.colors.bangumiTime};")
        self.setText(updateTimeText)


class PerBangumiImg(QLabel):
    def __init__(self, imgPath, url):
        super(PerBangumiImg, self).__init__()
        self.setFixedWidth(64)
        self.setFixedHeight(64)
        self.url = url
        self.img = QPixmap(f"{PATH}/src/img/bangumiheadimg/" + imgPath)
        self.setPixmap(self.img)

        self.setCursor(Qt.PointingHandCursor)

    def mousePressEvent(self, e):
        if (e.button() == Qt.LeftButton):
            webbrowser.open(self.url)


class PerBangumiInfo(QFrame):
    def __init__(self, title: str, chapter: str, platformsInfo: dict):
        super(PerBangumiInfo, self).__init__()
        self.setFixedWidth(140)
        # self.setStyleSheet("background-color:white")

        self.mainLayout = QVBoxLayout()
        self.mainLayout.setContentsMargins(0, 0, 0, 0)

        self.titleEl = Title(title)
        self.chapterEl = Chapter(chapter)
        self.platformsEl = Platforms(platformsInfo)

        self.mainLayout.addWidget(self.titleEl)
        self.mainLayout.addWidget(self.chapterEl)
        self.mainLayout.addWidget(self.platformsEl)

        self.mainLayout.setStretchFactor(self.titleEl, 2)
        self.mainLayout.setStretchFactor(self.chapterEl, 1)
        self.mainLayout.setStretchFactor(self.platformsEl, 2)

        self.setLayout(self.mainLayout)


class Title(QLabel):
    def __init__(self, title):
        super(Title, self).__init__()
        self.setFixedWidth(125)
        self.setWordWrap(True)
        self.setStyleSheet(f"color:{config.colors.bangumiTitle};")
        self.setText(title)


class Chapter(QLabel):
    def __init__(self, chapter):
        super(Chapter, self).__init__()
        self.setStyleSheet(f"color:{config.colors.bangumiChapter};")
        self.setText(chapter)


class Platforms(QFrame):
    def __init__(self, platformsInfo: dict):
        super(Platforms, self).__init__()

        platformsInfo = self.filter(platformsInfo)
        c = 0
        for k, v in platformsInfo.items():
            if k == "default":
                continue
            l = perPlatform.PerPlatform(k, v, self)
            l.move((c % 6) * 20, int(c / 6) * 20)
            c += 1
        # for x in range(8):
        #     a = QLabel()
        #     img = QPixmap(f"{PATH}/src/img/platformicon/bilibili.png")
        #     a.setPixmap(img)
        #     self.mainLayout.addWidget(a,x//4,x%4,1,1)

    @staticmethod
    def filter(platforms: dict):
        retDict = {}
        for k, v in platforms.items():
            if k == "default":
                retDict[k] = v
            elif k == "bilibili":
                if v and not v == "https://www.bilibili.com/bangumi/media/md":
                    retDict[k] = v
            elif k == "acfun":
                if v and not v == "http://www.acfun.cn/bangumi/aa":
                    retDict[k] = v
            elif k in ["iqiyi", "qq", "youku", "migudm", "mgtv", "dmhy", "niconico","dilidili"] and v:
                retDict[k] = v
        return retDict

# perBangumiTimeDotLabel = PerBangumiTimeDotLabel()
