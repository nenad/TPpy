from tp.mappers.Mapper import Mapper
from tp.models.assignable import Assignable


class AssignableMapper(Mapper):
    def __init__(self):
        Mapper.__init__(self)

    def map(self, json_object):
        assignable = Assignable()
        assignable.id = json_object['Id']
        assignable.name = json_object['Name']
        assignable.entityType = json_object['EntityType']['Name']

        return assignable
