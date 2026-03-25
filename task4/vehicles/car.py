from vehicles.engine import Engine
from vehicles.vehicle import Vehicle


class Car(Engine, Vehicle):
    def __init__(self, model, max_speed):
        self.model = model
        Vehicle.__init__(self, max_speed)

    def drive(self):
        print(f"Car {self.model} is driving at {self.max_speed}")