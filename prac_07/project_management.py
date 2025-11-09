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
from datetime import datetime

" DOCSTRINGS"


def main():
    """Menu options for loading, saving, displaying, filtering, adding and updating projects."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}.")

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
            display_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
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
    """Save projects in memory to the csv file."""
    filename = input("Enter a filename to save your projects to ")


def display_projects(projects):
    """Display incomplete and completed projects."""
    print("Incomplete projects:")
    for project in projects:
        if project.completion_percentage < 100: # Incomplete project
            print(f"{project.name}, start: {project.start_date}, priority {project.priority}, estimate: ${project.cost_estimate}, completion: {project.completion_percentage}%")

    print("Completed projects:")
    for project in projects:
        if project.completion_percentage == 100: # Complete project
            print(f"{project.name}, start: {project.start_date}, priority {project.priority}, estimate: ${project.cost_estimate}, completion: {project.completion_percentage}%")

def get_project_date(project):
    """Return the project's start date as a datetime object."""
    return datetime.strptime(project.start_date, "%d/%m/%Y")

def display_projects_by_date(projects):
    """Display projects after a certain date and sorted by date."""
    input_date = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.strptime(input_date, "%d/%m/%Y")

    filtered_projects = [project for project in projects if get_project_date(project) >= filter_date]
    filtered_projects.sort(key=get_project_date)

    for project in filtered_projects:
        print(project)

def add_new_project(projects):
    """Add a new project in memory."""
    print("Lets add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = float(input("Percent complete: "))

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)

def update_project(projects):
    """Update a chosen project in memory."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    project_choice = int(input("Project choice: "))
    chosen_project = projects[project_choice]
    print(chosen_project)

    new_completion_percentage = float(input("New Percentage: "))
    new_priority = int(input("New Priority: "))

    chosen_project.completion_percentage = new_completion_percentage
    chosen_project.priority = new_priority


main()
