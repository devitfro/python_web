class StringAttributesMeta(type):
    def __new__(cls, name, bases, dct):
        for k, v in dct.items():
            if not k.startswith("__") and not isinstance(v, str) and not callable(v):
                raise TypeError("All attributes must be strings")
        return super().__new__(cls, name, bases, dct)