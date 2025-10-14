FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2

def main():
    """ Read the records in the file and output details about the Wimbledon champions and countries"""
    records = load_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)

def process_records(records):
    """ Process the records to create a dictionary of champions and countries. """
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_to_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_count[record[INDEX_CHAMPION]] = 1
    return champion_to_count, countries

def display_results(champion_to_count, countries):
    """ Display champions and countries. """
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))

def load_records(filename):
    """ Load the records from the file into a list of lists. """
    records = []

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Remove CSV header row
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()

