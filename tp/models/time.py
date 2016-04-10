from tp.models.entity import Entity


class Time(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.description = None
        self.spent = None
        self.remain = None
