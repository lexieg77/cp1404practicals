from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def choose_taxi(bill_to_date):
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Taxi's available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

    index = int(input("Choose taxi: "))
    if index > len(taxis) - 1:
        print("Invalid taxi choice")
        print(f"Bill to date: ${bill_to_date:.2f}")
    else:
        print(f"Bill to date: ${bill_to_date:.2f}")
        current_taxi = taxis[index]
        return current_taxi


def drive(current_taxi, bill_to_date):
    if current_taxi == None:
        print("You need to choose a taxi before you can drive")
        print(f"Bill to date: ${bill_to_date:.2f}")
    else:
        drive_total = int(input("Drive how far? "))

        current_taxi.start_fare()
        current_taxi.drive(drive_total)
        trip_cost = current_taxi.get_fare()
        bill_to_date += trip_cost
        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
        print(f"Bill to date: ${bill_to_date:.2f}")

def main():
    bill_to_date = 0
    current_taxi = None

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(bill_to_date)
        elif choice == "d":
            drive(current_taxi, bill_to_date)
        else:
            print("Invalid option")
            print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    # quit



main()