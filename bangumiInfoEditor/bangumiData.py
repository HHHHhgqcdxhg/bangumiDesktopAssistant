import json,os

bangumiData = []
dbPath = "db/bangumisInfo"

bangumiJsons = os.listdir(dbPath)
for bangumiJsonFileName in bangumiJsons:
    print(f"{dbPath}/{bangumiJsonFileName}")
    with open(f"{dbPath}/{bangumiJsonFileName}","r",encoding="utf8") as f:
        bangumiData.append(json.load(f))
