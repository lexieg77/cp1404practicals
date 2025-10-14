def main():
    filename = "wimbledon.csv"
    load_data(filename)




def load_data(filename):
    """ Load the data from the file into a list of lists. """
    data = []

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline() # remove column headings
        lines = in_file.readlines()
        for line in lines:
            parts = line.strip().split(",")
            data.append(parts)

main()

