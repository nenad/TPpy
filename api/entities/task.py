import json
from api.tpRequest import TPRequest
from api.tpApi import TPApi


def create(name, story_id):
    api = TPApi()
    request = TPRequest()
    request.setBasicUrl(api.getEntityTypeURL('Tasks'))

    data = {
        "Name": name,
        "UserStory": {
            "Id": story_id
        }
    }

    request.post('', json.dumps(data))
