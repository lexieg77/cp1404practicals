from unreliable_car import UnreliableCar


def main():
    """Testing an unreliable car of 30%"""
    my_car = UnreliableCar("Prius 1", 30, 30)

    for i in range(1, 15):
        print(f"My car is able to drive {my_car.drive(i)} km")

    print(my_car)


main()
