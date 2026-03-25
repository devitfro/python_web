class NoUnderscoreMeta(type):
    def __new__(cls, name, bases, dct):
        for key in dct:
            if key.startswith("_"):
                raise ValueError("Attributes cannot start with underscore")
        return super().__new__(cls, name, bases, dct)