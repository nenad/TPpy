import json
import datetime

from api.tpRequest import TPRequest
from api.tpApi import TPApi
from configuration import config
from tp.mappers.timeMapper import TimeMapper


def create(description, hours, assignable_id):
    api = TPApi()
    request = TPRequest()
    request.setBasicUrl(api.getEntityTypeURL('Times'))
    request.setIncludedProperties(['Description', 'Spent', 'Assignable[Id, Name, EntityType[Name]]'])

    data = {
        "Description": description,
        "Spent": hours,
        "Assignable": {
            "Id": assignable_id
        }
    }

    response = request.post('', json.dumps(data))
    return TimeMapper().map(json.loads(response.content))


def atDate(date_str):
    api = TPApi()
    req = TPRequest()
    mapper = TimeMapper()
    req.setBasicUrl(api.getEntityTypeURL('Times'))
    req.setIncludedProperties(['Description', 'Spent', 'Assignable[Id, Name, EntityType[Name]]'])
    user_id = config.get_project_var('user_id')
    req.setQuery("(User.Id eq %s) and (Date eq '%s')" % (user_id, date_str))
    response = req.get()
    times_json = json.loads(response.content)
    times = []
    for item in times_json['Items']:
        times.append(mapper.map(item))
    return times

