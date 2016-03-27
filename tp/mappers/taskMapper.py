from tp.mappers.Mapper import Mapper


class TaskMapper(Mapper):
    def __init__(self, json_string):
        Mapper.__init__(self, json_string)
