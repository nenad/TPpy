import json

from api.tpApi import TPApi
from api.tpRequest import TPRequest
from repositories.task.taskRepository import TaskRepository
from tp.mappers.taskMapper import TaskMapper


class TaskHTTPImpl(TaskRepository):
    def __init__(self):
        TaskRepository.__init__(self)
        self.taskMapper = TaskMapper()
        self.entityType = 'Tasks'
        self.tp = TPApi()

    def getAll(self):
        request = TPRequest()
        request.setBasicUrl(self.tp.getEntityTypeURL(self.entityType))
        response = request.get()
        json_objects = json.loads(response.content)
        stories_json = json_objects['Items']
        stories = []
        for story in stories_json:
            stories.append(self.taskMapper.map(story))
        stories.sort(key=lambda p: p.id)
        return stories

    def find(self, task_id):
        request = TPRequest()
        request.setBasicUrl(self.tp.getEntityTypeURL(self.entityType))
        request.setId(task_id)
        response = request.get()
        json_object = json.loads(response.content)
        return self.taskMapper.map(json_object)

    def findWithTimes(self, task_id):
        request = TPRequest()
        request.setBasicUrl(self.tp.getEntityTypeURL(self.entityType))
        request.setId(task_id)
        request.setIncludedProperties(['Times, Name, EntityState'])
        response = request.get()
        json_object = json.loads(response.content)
        return self.taskMapper.map(json_object)
