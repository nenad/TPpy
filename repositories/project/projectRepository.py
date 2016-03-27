class ProjectRepository:
    def __init__(self):
        pass

    def getAll(self):
        raise NotImplementedError()

    def find(self, project_id):
        raise NotImplementedError()
