import json

from api.tpApi import TPApi
from api.tpRequest import TPRequest
from configuration import config
from repositories.assignable.assignableRepo import AssignableRepository


class State:
    def __init__(self):
        pass

    BACKLOG = 'Backlog'
    READY = 'Ready'
    IN_PROGRESS = 'In Progress'
    IN_TESTING = 'In Testing'
    IN_REVIEW = 'In Review'
    DONE = 'Done'


def change_state(new_state, entity_id):
    entity = AssignableRepository().find(entity_id)
    entity_type = entity.entityType
    process_id = config.get_project_var('process_id')

    entity_states_url = TPApi().getEntityTypeURL('EntityStates')
    entity_state_request = TPRequest()
    entity_state_request.setBasicUrl(entity_states_url)
    entity_state_request.setQuery(
        '(Process.Id eq %s) and (EntityType.Name eq "%s") and (Name eq "%s")' % (process_id, entity_type, new_state))

    state_id = json.loads(entity_state_request.get().content)["Items"][0]["Id"]

    data = {
        "Id": entity_id,
        "EntityState": {
            "Id": state_id
        }
    }

    assignable_url = TPApi().getEntityTypeURL('Assignables')
    update_request = TPRequest()
    update_request.setBasicUrl(assignable_url)
    update_request.post("", json.dumps(data))
