class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def drive(self):
        print(f"Driving at maximum speed of {self.max_speed}")