
from prac_07.guitar import Guitar
import csv

def main():
    """Guitar program, using Guitar class."""
    guitars = reading_csv_file()

    # Sort guitars by year
    guitars.sort()
    print("Guitars sorted by year:")
    for guitar in guitars:
        print(guitar)


def reading_csv_file():
    """Language file reader version using the csv module."""
    in_file = open('guitars.csv', 'r', newline='')
    in_file.readline()
    reader = csv.reader(in_file)
    guitars = []
    for row in reader:
        guitars.append(row)
    in_file.close()

    return guitars


main()
