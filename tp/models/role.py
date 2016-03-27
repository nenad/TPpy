from tp.models.entity import Entity


class Role(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.name = ""
        self.hasEffort = False
        self.canChangeOwner = False
