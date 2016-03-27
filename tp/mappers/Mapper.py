import json


class Mapper:
    def __init__(self):
        self.attribute_map = []
        self.json_string = ""
        self.json_object = None

    def map(self, json_string):
        self.json_string = json_string
        self.json_object = json.loads(json_string)
