from tp.models.entity import Entity


class Task(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.name = ""  # String
        self.description = ""  # String
        self.startDate = None
        self.endDate = None
        self.createDate = None
        self.modifyDate = None
        self.lastCommentDate = None
        self.tags = []
        self.numericPriority = 0
        self.effort = 0.0
        self.effortCompleted = 0.0
        self.effortToDo = 0.0
        self.progress = 0.0
        self.timeSpent = 0.0
        self.timeRemain = 0.0
        self.plannedStartDate = None
        self.plannedEndDate = None
        self.entityType = None
        self.project = None
        self.owner = None
        self.lastCommentedUser = None
        self.linkedTestPlan = None
        self.release = None
        self.iteration = None
        self.teamIteration = None
        self.team = None
        self.priority = None
        self.entityState = None
        self.responsibleTeam = None
        self.userStory = None
        self.customFields = []
