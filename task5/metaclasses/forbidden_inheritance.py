class ForbiddenInheritanceMeta(type):
    def __new__(cls, name, bases, dct):
        for base in bases:
            if "Forbidden" in base.__name__:
                raise TypeError("Cannot inherit from Forbidden class")
        return super().__new__(cls, name, bases, dct)