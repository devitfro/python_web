class Name:
    def __init__(self):
        self.private_name = None

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise ValueError("Name must be string")
        if not value.isalpha() or not value[0].isupper():
            raise ValueError("Name must start with capital and contain only letters")
        setattr(obj, self.private_name, value)