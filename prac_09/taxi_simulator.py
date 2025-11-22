from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def choose_taxi(taxis, bill_to_date):
    """Return the chosen taxi and the bill to date."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

    index = int(input("Choose taxi: "))
    if index < 0 or index >= len(taxis):
        print("Invalid taxi choice")
        print(f"Bill to date: ${bill_to_date:.2f}")
        return None
    else:
        print(f"Bill to date: ${bill_to_date:.2f}")
        return taxis[index]


def drive(current_taxi, bill_to_date):
    """Return bill to date after driving the taxi."""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
        print(f"Bill to date: ${bill_to_date:.2f}")
        return bill_to_date

    distance = int(input("Drive how far? "))

    current_taxi.start_fare()
    current_taxi.drive(distance)
    trip_cost = current_taxi.get_fare()
    bill_to_date += trip_cost

    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
    print(f"Bill to date: ${bill_to_date:.2f}")

    return bill_to_date


def main():
    """Choose and drive a taxi."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    bill_to_date = 0
    current_taxi = None

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis, bill_to_date)
        elif choice == "d":
            bill_to_date = drive(current_taxi, bill_to_date)
        else:
            print("Invalid option")
            print(f"Bill to date: ${bill_to_date:.2f}")

        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    for taxi in taxis:
        print(taxi)


main()
