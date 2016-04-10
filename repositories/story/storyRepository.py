class StoryRepository:
    def __init__(self):
        pass

    def getAll(self):
        raise NotImplementedError()

    def find(self, story_id):
        raise NotImplementedError()

    def findWithTasks(self, story_id):
        raise NotImplementedError()
