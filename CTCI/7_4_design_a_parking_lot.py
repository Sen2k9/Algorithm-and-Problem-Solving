

class ParkingLot:

    def __init__(self, spaces):

        self.spaces = spaces

    def vehicle_enter(self, vehicle):
        
        if self.is_full():
            return False
        
        if vehicle.tag:
            vehicle.parked = True
            self.spaces -= 1
            return True

        return False

    def vehicle_exit(self, vehicle):
        vehicle.parked = False
        self.spaces += 1
        return True
    
    def is_full(self):
        return True if self.spaces == 0 else False


class Vehicle:

    def __init__(self, title, tag=False, parked=False):
        self.title = title
        self.tag = tag
        self.parked = parked # check whether the car is parked or not
    
    def is_parked(self):

        return self.parked


lot = ParkingLot(2)

v1 = Vehicle("Camry", True)
v2 = Vehicle("Accord", True)
v3 = Vehicle("Altima", True)

assert lot.vehicle_enter(v1) == True
assert lot.vehicle_enter(v2) == True
assert lot.vehicle_enter(v3) == False
assert v3.parked == False
assert v2.parked == True
