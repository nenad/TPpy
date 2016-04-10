import json
from api.tpRequest import TPRequest
from api.tpApi import TPApi
from tp.mappers.taskMapper import TaskMapper


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

    response = request.post('', json.dumps(data))
    return TaskMapper().map(json.loads(response.content))
