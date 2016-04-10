import json
from api.tpRequest import TPRequest
from api.tpApi import TPApi
from tp.mappers.storyMapper import StoryMapper


def create(name, project_id):
    api = TPApi()
    request = TPRequest()
    request.setBasicUrl(api.getEntityTypeURL())

    data = {
        'Name': name,
        'Project': {
            "Id": project_id
        }
    }

    response = request.post('', json.dumps(data))
    return StoryMapper().map(json.loads(response.content))
