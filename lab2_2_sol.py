import re
from datetime import datetime
users = {}
projects = []
def validate_date_format(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def register():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    if not validate_email(email):
        print("Invalid email format.")
        return
    password = input("Password: ")
    confirm_password = input("Confirm Password: ")
    if password != confirm_password:
        print("Passwords do not match.")
        return
    phone = input("Phone: ")
    if not validate_phone(phone):
        print("Invalid Egyptian phone number.")
        return
    users[email] = {"first_name": first_name, "last_name": last_name, "password": password, "phone": phone, "activated": False}
    print("Registered successfully. Awaiting activation.")

def activate_account(email):
    if email in users:
        users[email]["activated"] = True
        print("Account activated.")
    else:
        print("User not found.")

def login():
    email = input("Email: ")
    password = input("Password: ")
    if email in users and users[email]["password"] == password:
        if not users[email]["activated"]:
            print("Account not activated.")
            return None
        print("Login successful.")
        return email
    print("Invalid credentials.")
    return None

def create_project(user_email):
    title = input("Project Title: ")
    details = input("Details: ")
    target = input("Total Target (EGP): ")
    start_date = input("Start Date (YYYY-MM-DD): ")
    end_date = input("End Date (YYYY-MM-DD): ")
    if not validate_date_format(start_date) or not validate_date_format(end_date):
        print("Invalid date format.")
        return
    projects.append({"owner": user_email, "title": title, "details": details, "target": target, "start_date": start_date, "end_date": end_date})
    print("Project created successfully.")

def view_projects():
    for p in projects:
        print(f"Title: {p['title']}, Target: {p['target']}, Start: {p['start_date']}, End: {p['end_date']}")

def search_project_by_date():
    date = input("Enter date (YYYY-MM-DD): ")
    if not validate_date_format(date):
        print("Invalid date format.")
        return
    for p in projects:
        if p['start_date'] <= date <= p['end_date']:
            print(f"Title: {p['title']}, Target: {p['target']}")

def main():
    while True:
        print("1. Register\n2. Activate\n3. Login\n4. Create Project\n5. View Projects\n6. Search Project\n7. Exit")
        choice = input("Choose: ")
        if choice == "1":
            register()
        elif choice == "2":
            email = input("Enter email to activate: ")
            activate_account(email)
        elif choice == "3":
            user_email = login()
            if user_email:
                while True:
                    print("1. Create Project\n2. View Projects\n3. Search Project\n4. Logout")
                    sub_choice = input("Choose: ")
                    if sub_choice == "1":
                        create_project(user_email)
                    elif sub_choice == "2":
                        view_projects()
                    elif sub_choice == "3":
                        search_project_by_date()
                    elif sub_choice == "4":
                        break
        elif choice == "7":
            break

if __name__ == "__main__":
    main()
