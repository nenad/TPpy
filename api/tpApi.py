from api.tpRequest import TPRequest
from configuration import config


class TPApi:
    def __init__(self):
        self.tpRequest = TPRequest()
        self.hostname = config.get('hostname')

    def getEntityTypeURL(self, entity_type="UserStories"):
        return self.hostname + "/api/v1/" + entity_type
