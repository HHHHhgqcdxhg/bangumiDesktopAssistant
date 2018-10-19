import datetime, json, os
from config import PATH
class BangumuInfo():
    def __init__(self, info: dict,chapterId, updateTime: datetime.datetime):
        self.title = info["title"]
        self.chapter = f"第{chapterId}话"
        self.imgSrc = info["headImgSrc"]
        self.url = info["platFormTargetUrls"][info["platFormTargetUrls"]["default"]]
        self.platformsInfo = info["platFormTargetUrls"]
        self.updateTime = updateTime

    @staticmethod
    def factory()->list:
        bangumiData = []
        bangumiChapters = []
        dbPath = f"{PATH}/src/db/bangumisInfo"
        bangumiJsons = os.listdir(dbPath)
        for bangumiJsonFileName in bangumiJsons:
            with open(f"{dbPath}/{bangumiJsonFileName}", "r", encoding="utf8") as f:
                bangumiData.append(json.load(f))

        for perBangumiData in bangumiData:
            if not perBangumiData["info"]["follow"]:
                continue
            for perChapter in perBangumiData["chapters"]:
                bangumiChapters.append(BangumuInfo(perBangumiData,perChapter["chapterId"], datetime.datetime.strptime(perChapter["updateTime"], "%Y-%m-%d %H:%M:%S")))

        # with open("bangumiInfoEditor/db/bangumisInfo/.json", "r", encoding="utf8") as f:
        #     bangumiInfoList = json.load(f)
        # bangumiChapters = []
        # for bangumiInfo in bangumiInfoList:
        #     updateTimes = BangumuInfo.getUpdateTimes(bangumiInfo["startDate"], bangumiInfo["finishDate"], bangumiInfo["updateTime"], bangumiInfo["updateType"])
        #     for updateTime in updateTimes:
        #         bangumiChapters.append(BangumuInfo(bangumiInfo,updateTime))
        # for x in bangumiChapters:
        #     print(x)
        # print(bangumiChapters.__len__())

        # bangumiChapters = sorted(bangumiChapters,key=lambda bangumiChapter: bangumiChapter.updateTime)
        bangumiChapters.sort(key=lambda bangumiChapter: bangumiChapter.updateTime)
        return bangumiChapters

    @staticmethod
    def getUpdateTimes(startDate: str, finishDate: str, updateTime: str, updateType: str):
        updateTimeA = updateTime.split(":")
        if updateTimeA.__len__() == 2:
            updateTimeA.append("00")
            updateTime = ":".join(updateTimeA)
        startUpdateDateTime = datetime.datetime.strptime(f"{startDate} {updateTime}", "%Y-%m-%d %H:%M:%S")
        finalUpdateDateTime = datetime.datetime.strptime(f"{finishDate} {updateTime}", "%Y-%m-%d %H:%M:%S")

        now = datetime.datetime.now()

        if updateType == "weekly":
            interval = datetime.timedelta(days=7)
            updateDateTime = startUpdateDateTime
            updateDateTimes = []
            chaptersCount = 0
            while finalUpdateDateTime >= updateDateTime >= startUpdateDateTime and chaptersCount <= 100:
                chaptersCount += 1
                if updateDateTime < now:
                    updateDateTime += interval
                    continue
                updateDateTimes.append(updateDateTime)
                updateDateTime += interval
            return updateDateTimes

        elif updateType == "monthly":
            updateDateTime = startUpdateDateTime
            updateDateTimes = []
            chaptersCount = 0
            while finalUpdateDateTime >= updateDateTime >= startUpdateDateTime and chaptersCount <= 100:
                chaptersCount += 1
                if updateDateTime < now:
                    updateTimeArr = updateDateTime.strftime("%Y-%m-%d %H:%M:%S").split("-")
                    m = int(updateTimeArr[1])
                    if not m == 12:
                        updateTimeArr[1] = str(m + 1)
                    else:
                        updateTimeArr[0] = str(int(updateTimeArr[0]) + 1)
                        updateTimeArr[1] = "1"
                    updateDateTimeStr = "-".join(updateTimeArr)
                    updateDateTime = datetime.datetime.strptime(updateDateTimeStr, "%Y-%m-%d %H:%M:%S")
                    continue
                updateDateTimes.append(updateDateTime)
                updateTimeArr = updateDateTime.strftime("%Y-%m-%d %H:%M:%S").split("-")
                m = int(updateTimeArr[1])
                if not m == 12:
                    updateTimeArr[1] = str(m + 1)
                else:
                    updateTimeArr[0] = str(int(updateTimeArr[0]) + 1)
                    updateTimeArr[1] = "1"
                updateDateTimeStr = "-".join(updateTimeArr)
                updateDateTime = datetime.datetime.strptime(updateDateTimeStr, "%Y-%m-%d %H:%M:%S")
            return updateDateTimes

if __name__ == '__main__':
    # a = json.load()
    # b = a[2]
    # getUpdateTimes(b["startDate"], b["finishDate"], b["updateTime"], b["updateType"])
    bangumiChapters = BangumuInfo.factory()
    bangumiChaptersS = [(x.title, str(x.updateTime)) for x in bangumiChapters]
    for x in bangumiChaptersS:
        print(x)
