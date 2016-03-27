from tp.mappers.Mapper import Mapper
from tp.models.project import Project


class ProjectMapper(Mapper):
    def __init__(self):
        Mapper.__init__(self)

    def map(self, json_object):
        project = Project()
        project.id = json_object['Id']
        project.name = json_object['Name']
        return project
