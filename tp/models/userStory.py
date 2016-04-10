import json

from tp.models.entity import Entity


class UserStory(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.name = None  # String
        self.description = None  # String
        self.startDate = None  # DateTime
        self.endDate = None  # DateTime
        self.createDate = None  # DateTime
        self.modifyDate = None  # DateTime
        self.lastCommentDate = None  # DateTime
        self.tags = None  # Array of String
        self.effort = None  # Float
        self.effortCompleted = None  # Float
        self.effortToDo = None  # Float
        self.timeSpent = None  # Float
        self.timeRemain = None  # Float
        self.initialEstimate = None  # Float
        self.customFields = None  # CustomField
        self.owner = None  # Owner
        self.project = None  # Project
        self.entityType = None  # EntityType
        self.release = None  # Release
        self.iteration = None  # Iteration
        self.priority = None  # Priority
        self.entityState = None  # EntityState
        self.feature = None  # Feature
        self.comments = None  # Array of Comment
        self.attachments = None  # Array of Attachment
        self.assignedUser = None  # User
        self.assignments = None  # Array of Assignment
        self.impediments = None  # Array of Impediment
        self.times = None  # Array of Time
        self.roleEfforts = None  # Array of RoleEffort
        self.tasks = None  # Array of Task
        self.bugs = None  # Array of Bug
        self.testCases = None  # Array of TestCase
        self.requests = None  # Array of Request
