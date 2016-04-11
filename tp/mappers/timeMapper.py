from tp.mappers.Mapper import Mapper
from tp.mappers.assignableMapper import AssignableMapper
from tp.models.time import Time


class TimeMapper(Mapper):
    def __init__(self):
        Mapper.__init__(self)

    def map(self, json_string):
        time = Time()
        time.id = json_string['Id']
        time.description = json_string['Description']
        time.spent = json_string['Spent']
        time.assignable = AssignableMapper().map(json_string['Assignable'])

        return time
