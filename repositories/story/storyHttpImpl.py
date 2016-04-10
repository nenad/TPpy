import json

from api.tpApi import TPApi
from api.tpRequest import TPRequest
from repositories.story.storyRepository import StoryRepository
from tp.mappers.storyMapper import StoryMapper


class StoryHTTPImpl(StoryRepository):
    def __init__(self):
        StoryRepository.__init__(self)
        self.storyMapper = StoryMapper()
        self.entityType = 'UserStories'
        self.tp = TPApi()

    def getAll(self):
        request = TPRequest()
        request.setBasicUrl(self.tp.getEntityTypeURL(self.entityType))
        response = request.get()
        json_objects = json.loads(response.content)
        stories_json = json_objects['Items']
        stories = []
        for story in stories_json:
            stories.append(self.storyMapper.map(story))
        stories.sort(key=lambda p: p.id)
        return stories

    def find(self, story_id):
        request = TPRequest()
        request.setBasicUrl(self.tp.getEntityTypeURL(self.entityType))
        request.setId(story_id)
        response = request.get()
        json_object = json.loads(response.content)
        return self.storyMapper.map(json_object)

    def findWithTasks(self, story_id):
        request = TPRequest()
        request.setBasicUrl(self.tp.getEntityTypeURL(self.entityType))
        request.setId(story_id)
        request.setIncludedProperties(['Tasks, Name, EntityState'])
        response = request.get()
        json_object = json.loads(response.content)
        return self.storyMapper.map(json_object)
