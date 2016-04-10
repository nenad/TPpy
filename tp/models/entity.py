import types


class Entity:
    def __init__(self):
        self.id = 0  # Integer

    def __str__(self):
        return self.to_JSON()

    def to_JSON(self):
        jsonstr = ''
        for var in self.__dict__:
            value = self.__dict__[var]
            if value is not None:
                if isinstance(value, types.ListType):
                    jsonstr += var + ':\n'
                    if len(value) == 0:
                        jsonstr += '\tempty' + '\n'
                    for obj in value:
                        jsonstr += '\t\n'.join(['\t' + line for line in obj.__str__().splitlines()]) + '\n\n'
                else:
                    jsonstr += var + ' => ' + value.__str__() + '\n'

        return jsonstr
