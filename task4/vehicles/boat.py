from vehicles.engine import Engine
from vehicles.vehicle import Vehicle


class Boat(Engine, Vehicle):
    def __init__(self, boat_type, max_speed):
        self.type = boat_type
        Vehicle.__init__(self, max_speed)

    def drive(self):
        print(f"Boat of type {self.type} is sailing at {self.max_speed}")