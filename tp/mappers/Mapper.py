import json


class Mapper:
    json = ""
    jsonObject = None
    attributeMap = []

    def __init__(self, json):
        self.json = json
        self.jsonObject = json.loads(json)
