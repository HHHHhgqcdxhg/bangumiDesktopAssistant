import json

with open("src/db/config.json","r") as f:
    configDict = json.load(f)

class Colors:
    def __init__(self):
        self.dict = configDict["colors"]
        for k,v in self.dict.items():
            if type(v) == str:
                v = f"\"{v}\""
            exec(f"self.{k}={v}")

class Config:
    def __init__(self):
        self.dict = configDict
        for k,v in self.dict.items():
            if type(v) == dict or type(v) == list:
                continue
            elif type(v) == str:
                v = f"\"{v}\""
            exec(f"self.{k}={v}")
        self.colors = Colors()

    def __str__(self):
        return str(configDict)

config = Config()

if __name__ == '__main__':
    a = {"111":111}
    print(type(a))
