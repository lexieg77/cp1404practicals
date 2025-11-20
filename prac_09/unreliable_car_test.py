from unreliable_car import UnreliableCar

def main():
    """Testing an unreliable car of 30%"""
    my_car = UnreliableCar("Prius 1", 30, 30)
    print(f"My car is able to drive {my_car.drive(20)} km")
