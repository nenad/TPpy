import json

from api.tpRequest import TPRequest

from api.tpApi import TPApi


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

    request.post('', json.dumps(data))
