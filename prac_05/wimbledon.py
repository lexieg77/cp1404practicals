FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2

def main():
    records = load_data(FILENAME)
    champion_to_court, countries = process_champions_and_countries(records)


def load_data(filename):
    """ Load the records from the file into a list of lists. """
    records = []

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline() # remove column headings
        lines = in_file.readlines()
        for line in lines:
            parts = line.strip().split(",")
            records.append(parts)

def process_champions_and_countries(records):
    """ Process the records to create a dictionary of champions and countries """
    champion_to_count = {}
    countries = set()

    for record in records:
        countries.add[record[INDEX_COUNTRY]] += 1
        try:
            champion_to_count[record[INDEX_CHAMPION] += 1
        except KeyError:
            champion_to_count[INDEX_CHAMPION] = 1
    return champion_to_count, countries


main()

