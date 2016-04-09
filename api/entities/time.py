import json
from api.tpRequest import TPRequest
from api.tpApi import TPApi


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

    request.post('', json.dumps(data))
