import json
from api.tpRequest import TPRequest
from api.tpApi import TPApi
from tp.mappers.timeMapper import TimeMapper


def create(description, hours, assignable_id):
    api = TPApi()
    request = TPRequest()
    request.setBasicUrl(api.getEntityTypeURL('Times'))

    data = {
        "Description": description,
        "Spent": hours,
        "Assignable": {
            "Id": assignable_id
        }
    }

    response = request.post('', json.dumps(data))
    return TimeMapper().map(json.loads(response.content))
