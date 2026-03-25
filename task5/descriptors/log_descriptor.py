class LogDescriptor:
    def __init__(self, name="attr"):
        self.name = name
        self.private_name = "_" + name

    def __set_name__(self, owner, name):
        self.name = name
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        value = getattr(obj, self.private_name, None)
        print(f"[GET] {self.name} = {value}")
        return value

    def __set__(self, obj, value):
        print(f"[SET] {self.name} = {value}")
        setattr(obj, self.private_name, value)