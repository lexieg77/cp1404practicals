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
            display_projects(projects)
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
    """Load project data from a file and return a list of Project objects."""
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            clean_line = line.strip().split("\t")  # split tab-separated values
            name, start_date, priority, cost_estimate, completion_percentage = clean_line
            project = Project(
                name,
                start_date,
                int(priority),
                float(cost_estimate),
                int(completion_percentage)
            )
            projects.append(project)
    return projects

def save_projects():
    filename = input("Enter a filename to save your projects to ")


def display_projects(projects):
    print("Incomplete projects:")
    for project in projects:
        incomplete = project.get_incomplete_projects()
        if incomplete:
            print(incomplete)

    print("Completed projects:")
    for project in projects:
        complete = project.get_complete_projects()
        if complete:
            print(complete)



main()
