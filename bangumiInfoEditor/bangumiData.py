import json,os
from config import PATH
bangumiData = []

dbPath = f"{PATH}/db/bangumisInfo"

bangumiJsons = os.listdir(dbPath)
for bangumiJsonFileName in bangumiJsons:
    with open(f"{dbPath}/{bangumiJsonFileName}","r",encoding="utf8") as f:
        bangumiData.append(json.load(f))
