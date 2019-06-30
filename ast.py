
class Object:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.value})"


class Number(Object):
    pass

class Integer(Number):
    pass

class Float(Number):
    pass


class String(Object):
    pass

class Character(Object):
    pass

class Boolean(Object):
    pass

class FunctionCall:
    def __init__(self, args):
        self.args = args

    def __repr__(self):
        return f"Call To{self.__class__.__name__} With {self.args}"

class Printf(FunctionCall):
    pass

