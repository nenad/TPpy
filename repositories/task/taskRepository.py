class TaskRepository:
    def __init__(self):
        pass

    def getAll(self):
        raise NotImplementedError()

    def find(self, task_id):
        raise NotImplementedError()

    def findWithTimes(self, task_id):
        raise NotImplementedError()
