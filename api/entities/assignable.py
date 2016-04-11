import json
from api.tpRequest import TPRequest
from api.tpApi import TPApi
from tp.mappers.taskMapper import TaskMapper


def find(assignable_id):
    api = TPApi()
    request = TPRequest()
    request.setBasicUrl(api.getEntityTypeURL('Assignables'))
    response = request.get('', json.dumps(data))
    return TaskMapper().map(json.loads(response.content))
