"""
Emails
Estimate: 20 mins
Actual: 15 mins
"""


# ADD IN DOCSTRINGS

def main():
    """ Display and create a dictionary of name and email pairs"""
    email = input("Email: ")
    email_to_name = {}

    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("What is your name then: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """ Extract name from email. """
    name = email.split("@")[0]
    parts = name.split(".")
    name = " ".join(parts).title()
    return name


main()
