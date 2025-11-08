FILENAME = "projects.txt"

from prac_07.project import Project

def main():
    filename = input("Please enter a file name to load projects from: ")
    projects = load_data_file(filename)
    print(projects)

def load_data_file(filename):
    """Load data from file name."""
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            clean_line = line.replace("\t", " ").replace("\n", "")
            projects.append(clean_line)
        return projects

main()
