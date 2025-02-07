import json
import os

FILE_NAME = "employees.json"

def load_data():
    """Loads employee data from the JSON file."""
    if not os.path.exists(FILE_NAME):
        return {}
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}

def save_data(data):
    """Saves employee data to the JSON file."""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def add_employee():
    """Adds a new employee record."""
    data = load_data()
    emp_id = input("Enter Employee ID: ").strip()
    if emp_id in data:
        print("Employee ID already exists.")
        return
    name = input("Enter Name: ").strip()
    position = input("Enter Position: ").strip()
    salary = input("Enter Salary: ").strip()
    data[emp_id] = {"name": name, "position": position, "salary": salary}
    save_data(data)
    print("Employee added successfully.")

def view_employees():
    """Displays all employee records."""
    data = load_data()
    if not data:
        print("No records found.")
        return
    for emp_id, details in data.items():
        print(f"{emp_id}: {details}")

def search_employee():
    """Searches for an employee by ID."""
    data = load_data()
    emp_id = input("Enter Employee ID to search: ").strip()
    if emp_id in data:
        print(f"Employee Found: {emp_id}: {data[emp_id]}")
    else:
        print("Employee not found.")

def update_employee():
    """Updates an employee's information."""
    data = load_data()
    emp_id = input("Enter Employee ID to update: ").strip()
    if emp_id not in data:
        print("Employee not found.")
        return
    print(f"Current Record: {data[emp_id]}")
    name = input("Enter new Name: ").strip()
    position = input("Enter new Position: ").strip()
    salary = input("Enter new Salary: ").strip()
    data[emp_id] = {"name": name, "position": position, "salary": salary}
    save_data(data)
    print("Employee updated successfully.")

def delete_employee():
    """Deletes an employee record."""
    data = load_data()
    emp_id = input("Enter Employee ID to delete: ").strip()
    if emp_id in data:
        del data[emp_id]
        save_data(data)
        print("Employee deleted successfully.")
    else:
        print("Employee not found.")

def main():
    """Main menu function."""
    while True:
        print("\nMenu:")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()