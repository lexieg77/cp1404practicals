
from prac_07.guitar import Guitar
import csv

def main():
    """Guitar program, using Guitar class."""
    reading_csv_file()



def reading_csv_file():
    """Language file reader version using the csv module."""
    in_file = open('guitars.csv', 'r', newline='')
    in_file.readline()
    reader = csv.reader(in_file)
    for row in reader:
        print(row)
    in_file.close()

main()
