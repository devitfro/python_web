class HelloMeta(type):
    def __new__(cls, name, bases, dct):
        def hello(self):
            print(f"Hello from {name}")

        dct["hello"] = hello
        return super().__new__(cls, name, bases, dct)