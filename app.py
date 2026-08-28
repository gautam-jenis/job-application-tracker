from datetime import datetime
import csv
import os

fieldnames = ["company", "job_title", "location",
              "status", "date_applied", "notes"]


def display_application(application):
    print(f"Company: {application['company']}")
    print(f"Job Title: {application['job_title']}")
    print(f"Location: {application['location']}")
    print(f"Status: {application['status']}")
    print(f"Date Applied: {application['date_applied']}")
    print(f"Notes: {application['notes']}")


def view_applications():
    print("Viewing all applications...")
    try:
        with open("applications.csv", "r") as file:
            reader = csv.DictReader(file)
            applications = list(reader)

            if not applications:
                print("No applications found. Add an application first.")
                return

            applications.sort(
                key=lambda application: datetime.strptime(
                    application["date_applied"], "%m/%d/%Y"
                ),
                reverse=True
            )

            for row in applications:
                print("\n----- Application -----")
                display_application(row)

    except FileNotFoundError:
        print("No application found. Add an application first.")


def add_application():
    company = input("Company: ").strip()

    while company == "":
        print("You must enter a company name.")
        company = input("Company: ").strip()

    job_title = input("Job Title: ").strip()
    while job_title == "":
        print("You must enter a job title.")
        job_title = input("Job Title: ").strip()

    location = input("Location: ").strip()
    while location == "":
        print("You must enter a location.")
        location = input("Location: ").strip()

    application_status = input("Application status: ").strip()
    while application_status == "":
        print("You must enter an application status.")
        application_status = input("Application status: ").strip()

    while True:
        date_applied = input("Date applied (MM/DD/YYYY): ").strip()

        try:
            datetime.strptime(date_applied, "%m/%d/%Y")
            break

        except ValueError:
            print("Invalid date. Please use MM/DD/YYYY.")

    notes = input("Notes: ").strip()

    application = {
        "company": company,
        "job_title": job_title,
        "location": location,
        "status": application_status,
        "date_applied": date_applied,
        "notes": notes
    }

    with open("applications.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if os.path.getsize("applications.csv") == 0:
            writer.writeheader()

        writer.writerow(application)

    print("Adding a new application...")


def update_status():
    company_to_update = input("Enter company name: ").strip()
    job_title_to_update = input("Enter job title: ").strip()

    try:
        with open("applications.csv", "r") as file:
            reader = csv.DictReader(file)
            applications = list(reader)

        found = False

        for application in applications:
            if (
                application["company"].lower() == company_to_update.lower()
                and application["job_title"].lower() == job_title_to_update.lower()
            ):
                new_status = input("Enter new status: ").strip()
                while new_status == "":
                    print("You must enter a status.")
                    new_status = input("Enter new status: ").strip()
                application["status"] = new_status
                found = True
        with open("applications.csv", "w") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(applications)

        if found:
            print("Status updated successfully.")
        else:
            print("Application not found.")

    except FileNotFoundError:
        print("No applications found.")


def search_application():
    company_to_search = input("Enter company name: ").strip()
    job_title_to_search = input("Enter Job Title: ").strip()

    try:
        with open("applications.csv", "r") as file:
            reader = csv.DictReader(file)

            found = False

            for application in reader:
                if (
                    application["company"].lower(
                    ) == company_to_search.lower()
                    and application["job_title"].lower() == job_title_to_search.lower()
                ):
                    print("\n----- Application Found -----")
                    display_application(application)
                    found = True
        if not found:
            print("Application not found.")
    except FileNotFoundError:
        print("No applications found.")


def delete_application():
    company_to_delete = input("Enter Company name: ").strip()
    job_title_to_delete = input("Enter job title: ").strip()

    try:
        with open("applications.csv", "r") as file:
            reader = csv.DictReader(file)
            applications = list(reader)

        remaining_applications = []
        found = False

        for application in applications:
            if (application["company"].lower() == company_to_delete.lower()
                    and application["job_title"].lower() == job_title_to_delete.lower()):
                found = True
            else:
                remaining_applications.append(application)

        with open("applications.csv", "w") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(remaining_applications)

        if found:
            print("Application deleted successfully.")
        else:
            print("Application not found.")

    except FileNotFoundError:
        print("Application not found.")


def filter_by_status():
    status_to_filter = input("What status are you looking for? ").strip()
    try:
        with open("applications.csv", "r") as file:
            reader = csv.DictReader(file)
            found = False

            for application in reader:
                if application["status"].lower() == status_to_filter.lower():
                    print("\n----- Application -----")
                    display_application(application)
                    found = True
        if not found:
            print("No applications found with that status.")
    except FileNotFoundError:
        print("No applications found. Add an application first.")


while True:
    print("===== Job Application Tracker =====\n")
    print("1. Add a new application")
    print("2. View all applications")
    print("3. Update application status")
    print("4. Search applications")
    print("5. Delete application")
    print("6. Filter applications by status")
    print("7. Exit")
    try:
        choice = int(input("Choose an option:"))
    except ValueError:
        print("Please enter a number.")
        continue
    if choice == 1:
        add_application()

    elif choice == 2:
        view_applications()

    elif choice == 3:
        update_status()

    elif choice == 4:
        search_application()

    elif choice == 5:
        delete_application()

    elif choice == 6:
        filter_by_status()

    elif choice == 7:
        print("Exiting...")
        break

    else:
        print("Invalid option")
