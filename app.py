import csv
import os

fieldnames = ["company", "job_title", "location",
              "status", "date_applied", "notes"]


def view_applications():
    print("Viewing all applications...")
    try:
        with open("applications.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                print("\n----- Application -----")
                print(f"Company: {row['company']}")
                print(f"Job Title: {row['job_title']}")
                print(f"Location: {row['location']}")
                print(f"Status: {row['status']}")
                print(f"Date Applied: {row['date_applied']}")
                print(f"Notes: {row['notes']}")
    except FileNotFoundError:
        print("No application found. Add an application first.")


def add_application():
    company = input("Company: ")
    job_title = input("Job Title: ")
    location = input("Location: ")
    application_status = input("Application status: ")
    date_applied = input("Date applied: ")
    notes = input("Notes: ")
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
    company_to_update = input("Enter company name: ")
    job_title_to_update = input("Enter job title: ")

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
                new_status = input("Enter new status: ")
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
    company_to_search = input("Enter company name: ")
    job_title_to_search = input("Enter Job Title: ")

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
                    print(f"Company: {application['company']}")
                    print(f"Job Title: {application['job_title']}")
                    print(f"Location: {application['location']}")
                    print(f"Status: {application['status']}")
                    print(f"Date Applied: {application['date_applied']}")
                    print(f"Notes: {application['notes']}")
                    found = True
        if not found:
            print("Application not found.")
    except FileNotFoundError:
        print("No applications found.")


def delete_application():
    company_to_delete = input("Enter Company name: ")
    job_title_to_delete = input("Enter job title: ")

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


while True:
    print("===== Job Application Tracker =====\n")
    print("1. Add a new application")
    print("2. View all applications")
    print("3. Update application status")
    print("4. Search applications")
    print("5. Delete application")
    print("6. Exit")
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
        print("Exiting...")
        break

    else:
        print("Invalid option")
