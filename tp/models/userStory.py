from tp.models.entity import Entity


class UserStory(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.name = ""  # String
        self.description = ""  # String
        self.startDate = None  # DateTime
        self.endDate = None  # DateTime
        self.createDate = None  # DateTime
        self.modifyDate = None  # DateTime
        self.lastCommentDate = None  # DateTime
        self.tags = []  # Array of String
        self.effort = 0.0  # Float
        self.effortCompleted = 0.0  # Float
        self.effortToDo = 0.0  # Float
        self.timeSpent = 0.0  # Float
        self.timeRemain = 0.0  # Float
        self.initialEstimate = 0.0  # Float
        self.customFields = None  # CustomField
        self.owner = None  # Owner
        self.project = None  # Project
        self.entityType = None  # EntityType
        self.release = None  # Release
        self.iteration = None  # Iteration
        self.priority = None  # Priority
        self.entityState = None  # EntityState
        self.feature = None  # Feature
        self.comments = []  # Array of Comment
        self.attachments = []  # Array of Attachment
        self.assignedUser = None  # User
        self.assignments = []  # Array of Assignment
        self.impediments = []  # Array of Impediment
        self.times = []  # Array of Time
        self.roleEfforts = []  # Array of RoleEffort
        self.tasks = []  # Array of Task
        self.bugs = []  # Array of Bug
        self.testCases = []  # Array of TestCase
        self.requests = []  # Array of Request
