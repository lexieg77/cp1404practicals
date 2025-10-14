"""
Emails
Estimate: 20 mins
Actual: 28 mins
"""

def main():

    email = input("Email: ")
    email_to_name = {}

    get_name_from_email(email)


def get_name_from_email(email):
    name = email.split("@")[0]
    first_name = name.split(".")[0].capitalize()
    last_name = name.split(".")[-1].capitalize()
    return first_name, last_name
main()