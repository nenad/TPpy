from tp.models.entity import Entity


class User(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.kind = ""
        self.firstName = ""
        self.lastName = ""
        self.email = ""
        self.login = ""
        self.createDate = None
        self.modifyDate = None
        self.deleteDate = None
        self.isActive = False
        self.isAdministrator = False
        self.lastLoginDate = None
        self.weeklyAvailableHours = 0.0
        self.currentAllocation = 0
        self.currentAvailableHours = 0.0
        self.availableFrom = None
        self.availableFutureAllocation = 0
        self.availableFutureHours = 0.0
        self.isObserver = False
        self.locale = None
        self.skills = None
        self.activeDirectoryName = None
        self.role = None
