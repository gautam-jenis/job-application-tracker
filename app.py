import csv
import os
while True:
    print("===== Job Application Tracker =====\n")
    print("1. Add a new application")
    print("2. View all applications")
    print("3. Exit")
    try:
        choice = int(input("Choose an option:"))
    except ValueError:
        print("Please enter a number.")
        continue
    if choice == 1:
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
        fieldnames = ["company", "job_title", "location",
                      "status", "date_applied", "notes"]
        with open("applications.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if os.path.getsize("applications.csv") == 0:
                writer.writeheader()

            writer.writerow(application)

        print("Adding a new application...")
    elif choice == 2:
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

    elif choice == 3:
        print("Exiting...")
        break

    else:
        print("Invalid option")
