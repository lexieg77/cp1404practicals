FILENAME = "projects.txt"

MENU = """
 - (L)oad projects
 - (S)ave projects
 - (D)isplay projects
 - (F)ilter projects by date
 - (A)dd new project
 - (U)pdate project
 - (Q)uit
"""

from prac_07.project import Project

def main():

    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}.")

    # Menu
    print(MENU)
    choice = input(">>> ").upper()

    # Menu options
    while choice != "Q":
        if choice == "L":
            filename = input("Please enter a file name to load projects from: ")
            projects = load_projects(filename)
            print(projects)
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()


def load_projects(filename):
    """Load project data form user input."""
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            clean_line = line.replace("\t", " ").replace("\n", "")
            projects.append(clean_line)
        return projects

def save_projects():
    filename = input("Enter a filename to save your projects to ")


main()
