import json

from api.tpApi import TPApi
from api.tpRequest import TPRequest
from tp.mappers.assignableMapper import AssignableMapper


class AssignableRepository:
    def __init__(self):
        pass

    def find(self, assignable_id):
        api = TPApi()
        request = TPRequest()
        request.setBasicUrl(api.getEntityTypeURL('Assignables'))
        request.setId(assignable_id)
        request.setIncludedProperties(['Name', 'Id', 'Description', 'EntityType[Name]'])
        response = request.get()
        return AssignableMapper().map(json.loads(response.content))
