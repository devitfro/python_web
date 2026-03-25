from vehicles.car import Car
from vehicles.boat import Boat

class AmphibiousVehicle(Car, Boat):
    def __init__(self, model, boat_type, max_speed):
        self.model = model
        self.type = boat_type
        self.max_speed = max_speed
        self.is_on_land = True

    def drive(self):
        if self.is_on_land:
            print(f"Car {self.model} is driving at {self.max_speed}")
        else:
            print(f"Boat of type {self.type} is sailing at {self.max_speed}")