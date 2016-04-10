import json
import types

from tp.mappers.Mapper import Mapper
from tp.models.task import Task


class TaskMapper(Mapper):
    def __init__(self):
        Mapper.__init__(self)

    def map(self, json_string):
        task = Task()
        task.id = json_string['Id']
        task.name = json_string['Name']

        return task
