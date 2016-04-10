from tp.mappers.Mapper import Mapper
from tp.mappers.taskMapper import TaskMapper
from tp.models.userStory import UserStory


class StoryMapper(Mapper):
    def __init__(self):
        Mapper.__init__(self)
        # stateMapper = StateMapper()
        self.taskMapper = TaskMapper()

    def map(self, json_object):
        story = UserStory()
        story.id = json_object['Id']
        story.name = json_object['Name']
        story.entityState = json_object['EntityState']['Name']
        if 'Tasks' in json_object:
            tasks = json_object['Tasks']['Items']
            if len(tasks) > 0:
                story.tasks = [self.taskMapper.map(task) for task in tasks]

        return story
