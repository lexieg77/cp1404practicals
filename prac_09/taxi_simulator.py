from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

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
