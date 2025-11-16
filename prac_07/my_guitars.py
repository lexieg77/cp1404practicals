FILENAME = "guitars.csv"

from prac_07.guitar import Guitar
import csv

def main():
    """Guitar program, using Guitar class."""
    guitars = reading_csv_file()
    sort_guitars(guitars)
    add_new_guitar(guitars)
    write_new_guitars(guitars)


def reading_csv_file():
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(FILENAME, 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        for line in reader:
            if len(line) == 3:  # skip bad rows
                name, year, cost = line
                guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def sort_guitars(guitars):
    """ Sort guitars by year."""
    guitars.sort()
    print("Guitars sorted by year:")
    for guitar in guitars:
        print(guitar)

def add_new_guitar(guitars):
    """Add new guitars to the csv file."""
    print("Add a guitar")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(f"{guitar_to_add} added.")
        name = input("Name: ")

def write_new_guitars(guitars):
    """Write new guitars to the CSV file."""
    with open(FILENAME, "w", newline='') as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


main()
