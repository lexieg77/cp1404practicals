from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
bill_to_date = 0

def choose_taxi():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Taxi's available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

    taxi_choice = int(input("Chose taxi: "))
    if taxi_choice > len(taxis) - 1:
        print("Invalid taxi choice")
        print(f"Bill to date: ${bill_to_date:.2f}")
    else:
        print(f"Bill to date: ${bill_to_date:.2f}")


def main():
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            choose_taxi()
        elif choice == "d":
            pass
        else:
            print("Invalid option")
            print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    # quit

    current_taxi = None

main()