class Ore(object):
    def __init__(self, ore):
        for key in ore:
            self.__setattr__(key, ore[key])

    def __getattr__(self, name):
        return self.__dict__[name] if name != "minerals" else self.__dict__


class Mineral(object):
    def __init__(self, mineral):
        for key in mineral:
            self.__setattr__(key, mineral[key])

    def __getattr__(self, name):
        return self.__dict__[name]
