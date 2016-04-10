from tp.models.entity import Entity


class Task(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.name = None  # String
        self.description = None  # String
        self.startDate = None
        self.endDate = None
        self.createDate = None
        self.modifyDate = None
        self.lastCommentDate = None
        self.tags = None
        self.numericPriority = None
        self.effort = None
        self.effortCompleted = None
        self.effortToDo = None
        self.progress = None
        self.timeSpent = None
        self.timeRemain = None
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
        self.customFields = None
