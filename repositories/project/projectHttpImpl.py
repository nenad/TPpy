import json

from api.tpApi import TPApi
from api.tpRequest import TPRequest
from repositories.project.projectRepository import ProjectRepository
from tp.mappers.projectMapper import ProjectMapper


class ProjectHTTPImpl(ProjectRepository):
    def __init__(self):
        ProjectRepository.__init__(self)
        self.projectMapper = ProjectMapper()
        self.entityType = 'Projects'
        self.tp = TPApi()

    def getAll(self):
        request = TPRequest()
        request.setBasicUrl(self.tp.getEntityTypeURL(self.entityType))
        response = request.get()
        json_objects = json.loads(response.content)
        projects_json = json_objects['Items']
        projects = []
        for project in projects_json:
            projects.append(self.projectMapper.map(project))
        projects.sort(key=lambda p: p.id)
        return projects

    def find(self, project_id):
        request = TPRequest()
        request.setBasicUrl(self.tp.getEntityTypeURL(self.entityType))
        request.setId(project_id)
        response = request.get()
        json_object = json.loads(response)
        return self.projectMapper.map(json_object)
