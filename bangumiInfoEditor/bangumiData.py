import json,os

bangumiData = []
current_path = os.path.dirname(__file__)
if "/" in current_path:
    current_paths = current_path.split("/")
else:
    current_paths = current_path.split("\\")
if current_paths[-1] == "bangumiInfoEditor":
    current_path = "/".join(current_paths[:-1])
dbPath = f"{current_path}/db/bangumisInfo"

bangumiJsons = os.listdir(dbPath)
for bangumiJsonFileName in bangumiJsons:
    with open(f"{dbPath}/{bangumiJsonFileName}","r",encoding="utf8") as f:
        bangumiData.append(json.load(f))
