from tp.models.entity import Entity


class Project(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.name = ""

    def __str__(self):
        return self.id.__str__() + ". " + self.name.encode('utf-8')

    def __unicode__(self):
        return self.__str__()
