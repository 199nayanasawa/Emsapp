import mysql
from mysql.connector import connect, Error
# import re
import datetime
import csv

# Define global variables for cursor and connection
cursor = None
connection = None

def connect_to_mysql(host, user, password, database):
    try:
        connection = connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection  # Return the connection object
        else:
            print("Failed to connect to MySQL database")
            return None
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None


# Function to create MySQL table
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS emss1 (
                Name VARCHAR(255),
                Age INT,
                Address VARCHAR(255),
                Mobile_Number VARCHAR(255),
                Gender VARCHAR(10),
                Education_Details VARCHAR(50),
                Salary INT,
                DOJ DATE,
                Department VARCHAR(255),
                Position VARCHAR(255),
                Project_Name VARCHAR(255),
                Tech_Stack VARCHAR(255),
                Manager VARCHAR(255)
            )
        """)
        print("Table created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")
    finally:
        if connection.is_connected():
            cursor.close()


# Function to insert data from CSV file into MySQL table
def insert_data_from_csv(connection, file_path):
    try:
        cursor = connection.cursor()
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                cursor.execute("""
                    INSERT INTO emss1(Name, Age, Address, Mobile_Number, Gender,
                                           Education_Details, Salary, DOJ, Department,
                                           Position, Project_Name, Tech_Stack, Annual_Salary,Manager)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
                """, row)
            connection.commit()
        print("Data inserted successfully")
    except Error as e:
        print(f"Error inserting data into MySQL table: {e}")


# Function to validate name input
def validate_name(name):
    if not name.replace(" ", "").isalpha():
        print("Give me a valid name.")
        return False
    elif len(name) > 20:
        print("Name length should not exceed 20 characters.")
        return False
    else:
        return True


# Function to validate age input
def validate_age(age):
    if not age.isdigit():
        print("Give me a valid age.")
        return False
    else:
        return True


# Function to validate address
def validate_address(address):
    num_count = sum(c.isdigit() for c in address)
    if num_count < 1 or num_count > 2:
        print("Address should start with one or two numbers.")
        return False
    elif not address[num_count:].replace(" ", "").isalpha():
        print("Address should only contain letters (and spaces) after the initial numbers.")
        return False
    else:
        return True


# Function to validate mobile number input
def validate_mobile_number(mobile_number):
    if not mobile_number.startswith("+91"):
        print("Mobile number should start with +91.")
        return False
    elif len(mobile_number) != 13 or not mobile_number[3:].isdigit():
        print("Mobile number should contain only digits after +91.")
        return False
    elif not set(mobile_number[3:4]) <= set("6789"):
        print("Mobile number should contain only one digit from 8, 7, 6, 9 after +91.")
        return False
    else:
        return True


# Function to validate gender input
def validate_gender(gender):
    gender = gender.strip()  # Remove leading and trailing whitespace
    if len(gender) != 1 or not gender.isalpha() or gender.upper() not in ["M", "F"]:
        print("Gender should be either 'M' or 'F', without spaces, digits, or special characters.")
        return False
    else:
        return True


# Function to validate education details input
def validate_education_details(education):
    if not education.replace(" ", "").isalpha():
        print("Education details should only contain alphabets.")
        return False
    else:
        return True


# Function to validate salary
def validate_salary(salary):
    # Check if the salary contains only digits
    if salary.isdigit():
        return True
    else:
        print("Salary should contain only digits.")
        return False


import datetime


def validate_date_of_joining(doj):
    # Check if the date of joining follows the format YYYY-MM-DD
    if len(doj) != 10 or doj[4] != '-' or doj[7] != '-':
        print("Date of joining should follow the format YYYY-MM-DD.")
        return False

    # Extract year, month, and day from the date of joining
    try:
        year, month, day = map(int, doj.split('-'))
    except ValueError:
        print("Invalid date format.")
        return False

    # Get the current date
    current_date = datetime.date.today()

    # Check if the year is not greater than the current year
    if year > current_date.year:
        print("Year should not be greater than the current year.")
        return False

    # Check if the month is not greater than 12
    if month > 12:
        print("Month should not be greater than 12.")
        return False

    # Check if the day is not greater than 31
    if day > 31:
        print("Day should not be greater than 31.")
        return False

    return True


# Function to validate department input
def validate_department(department):
    if not department.replace(" ", "").isalpha():
        print("Department should only contain alphabets.")
        return False
    else:
        return True


# Function to validate position input
def validate_position(position):
    if not position.replace(" ", "").isalpha():
        print("Position should only contain alphabets.")
        return False
    else:
        return True


# Function to validate project name input
def validate_project_name(project_name):
    if not project_name.replace(" ", "").isalpha():
        print("Project name should only contain alphabets.")
        return False
    else:
        return True


# Function to validate tech stack input
def validate_tech_stack(tech_stack):
    if not tech_stack.replace(" ", "").isalpha():
        print("Tech stack should only contain alphabets.")
        return False
    else:
        return True


# Function to validate annual salary input
def validate_annual_salary(annual_salary):
    if not annual_salary.isdigit():
        print("Annual salary should contain only numbers.")
        return False
    else:
        return True


# Function to validate education details input
def validate_manager(manager):
    if not manager.replace(" ", "").isalpha():
        print("manager details should only contain alphabets.")
        return False
    else:
        return True


def add_new_employee(connection):
    if connection is None:
        print("No connection to MySQL database.")
        return

    try:
        cursor = connection.cursor()
        # Get employee details from user input
        name = input("Enter name: ")
        if not validate_name(name):
            return

        age = input("Enter age: ")
        if not validate_age(age):
            return

        address = input("Enter address: ")
        if not validate_address(address):
            return

        mobile_number = input("Enter mobile number: ")
        if not validate_mobile_number(mobile_number):
            return

        gender = input("Enter gender: ")
        if not validate_gender(gender):
            return

        education_details = input("Enter education details: ")
        if not validate_education_details(education_details):
            return

        salary = input("Enter salary: ")
        if not validate_salary(salary):
            return

        doj = input("Enter date of joining (YYYY-MM-DD): ")
        if not validate_date_of_joining(doj):
            return

        department = input("Enter department: ")
        if not validate_department(department):
            return

        position = input("Enter position: ")
        if not validate_position(position):
            return

        project_name = input("Enter project name: ")
        if not validate_project_name(project_name):
            return

        tech_stack = input("Enter tech stack: ")
        if not validate_tech_stack(tech_stack):
            return

        annual_salary = input("Enter annual salary: ")
        if not validate_annual_salary(annual_salary):
            return
        manager = input("Enter Manager name: ")
        if not validate_manager(manager):
            return

        # Insert new employee data into MySQL table
        cursor.execute("""
            INSERT INTO emss1 (Name, Age, Address, Mobile_Number, Gender, Education_Details, Salary, DOJ, Department, Position, Project_Name, Tech_Stack, Annual_Salary,manager)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
        """, (
            name, age, address, mobile_number, gender, education_details, salary, doj, department, position,
            project_name, tech_stack, annual_salary, manager))

        connection.commit()
        print("New employee added successfully")

    except Error as e:
        print(f"Error adding new employee: {e}")
        # Handle the error appropriately

    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()


# Function to view a particular employee's details
def view_employee_details(connection):
    cursor = connection.cursor()

    # Get the name of the employee whose details to view
    employee_name = input("Enter the name of the employee: ")

    # Query the database to retrieve the distinct details of the employee
    try:
        cursor.execute("""
            SELECT * FROM emss1 WHERE Name = %s
        """, (employee_name,))

        # Fetch all results
        employee_details = cursor.fetchall()

        if employee_details:
            print(f"Distinct Details for Employee {employee_name}:")
            distinct_details = set()
            for employee in employee_details:
                detail = (employee[0], employee[1], employee[2], employee[3],
                          employee[4], employee[5], employee[6], employee[7],
                          employee[8], employee[9], employee[10], employee[11], employee[12], employee[13])
                distinct_details.add(detail)

            for idx, detail in enumerate(distinct_details, start=1):
                print(f"\nEmployee Details {idx}:")
                print("Name:", detail[0])
                print("Age:", detail[1])
                print("Address:", detail[2])
                print("Mobile Number:", detail[3])
                print("Gender:", detail[4])
                print("Education Details:", detail[5])
                print("Salary:", detail[6])
                print("Date of Joining:", detail[7])
                print("Department:", detail[8])
                print("Position:", detail[9])
                print("Project Name:", detail[10])
                print("Tech Stack:", detail[11])
                print("Annual Salary:", detail[12])
                print("Manager:", detail[13])
        else:
            print("Employee not found.")

    except Error as e:
        print(f"Error retrieving employee details: {e}")

    finally:
        cursor.close()


## Function to update employee information (excluding name)
def update_employee(connection):
    cursor = connection.cursor()
    # Get the name of the employee whose details to update
    employee_name = input("Enter the name of the employee to update: ")

    try:
        # Check if the employee exists in the database
        cursor.execute("SELECT * FROM emss1 WHERE Name = %s", (employee_name,))
        employee = cursor.fetchone()

        if employee:
            # Display current details of the employee
            print("\nCurrent Employee Details:")
            print("Name:", employee[0])
            print("Age:", employee[1])
            print("Address:", employee[2])
            print("Mobile Number:", employee[3])
            print("Gender:", employee[4])
            print("Education Details:", employee[5])
            print("Salary:", employee[6])
            print("Date of Joining:", employee[7])
            print("Department:", employee[8])
            print("Position:", employee[9])
            print("Project Name:", employee[10])
            print("Tech Stack:", employee[11])
            print("Annual Salary:", employee[12])
            print("Manager:", employee[13])

            # Consume any unread result before executing another statement
            cursor.fetchall()

            # Get updated information from user input
            age = input("Enter new age: ")
            address = input("Enter new address: ")
            mobile_number = input("Enter new mobile number: ")
            gender = input("Enter new gender: ")
            education_details = input("Enter new education details: ")
            salary = input("Enter new salary: ")
            doj = input("Enter new date of joining (YYYY-MM-DD): ")
            department = input("Enter new department: ")
            position = input("Enter new position: ")
            project_name = input("Enter new project name: ")
            tech_stack = input("Enter new tech stack: ")
            annual_salary = input("Enter new annual salary: ")
            manager = input("Enter new manager: ")

            # Update employee information in the database
            cursor.execute("""
                           UPDATE emss1
                           SET Age = %s, Address = %s, Mobile_Number = %s, Gender = %s,
                               Education_Details = %s, Salary = %s, DOJ = %s, Department = %s, Position = %s,
                               Project_Name = %s, Tech_Stack = %s, Annual_Salary = %s,manager = %s
                           WHERE Name = %s
                       """, (age, address, mobile_number, gender, education_details,
                             salary, doj, department, position, project_name, tech_stack, annual_salary, manager,
                             employee_name))
            connection.commit()
            print("Employee information updated successfully.")
        else:
            print("Employee not found.")


    except Error as e:

        print(f"Error updating employee information: {e}")


    finally:
        if connection.is_connected():
            cursor.close()


# Function to delete employee records who worked less than 1 month
def delete_inactive_emss1(connection):
    cursor = connection.cursor()

    try:
        # Calculate today's date
        current_date = datetime.date.today()
        # Calculate the date 1 month ago
        one_month_ago = current_date - datetime.timedelta(days=30)
        # Delete employee records where DOJ is within the last month
        cursor.execute("DELETE FROM emss1 WHERE DOJ >= %s AND DOJ <= %s", (one_month_ago, current_date))
        connection.commit()
        print("Inactive employee records deleted successfully")
    except Error as e:
        print(f"Error deleting employee records: {e}")
    finally:
        if connection.is_connected():
            cursor.close()


# Function to list all employees in the organization with department, position, gender, and employee name
# Function to list all employees in the organization
def list_all_emss1(connection):
    cursor = connection.cursor()
    try:
        # Query the database to retrieve all employees' details
        cursor.execute("SELECT Distinct Name, Department, Position, Gender FROM emss1")
        # Fetch all results
        all_emss1 = cursor.fetchall()

        if all_emss1:
            print("\nAll Employees in the Organization:")
            for idx, employee in enumerate(all_emss1, start=1):
                print(f"\nEmployee {idx}:")
                print("Name:", employee[0])
                print("Department:", employee[1])
                print("Position:", employee[2])
                print("Gender:", employee[3])
        else:
            print("No employees found in the organization.")

    except Error as e:
        print(f"Error listing all emss1: {e}")

    finally:
        if connection.is_connected():
            cursor.close()


def calculate_total_monthly_salary(connection):
    cursor = connection.cursor()

    try:
        # Query to retrieve the total monthly salary for each distinct employee
        cursor.execute("""
            SELECT DISTINCT Name, Annual_Salary / 12 AS Monthly_Salary
            FROM emss1
        """)

        # Fetch all results
        results = cursor.fetchall()

        if results:
            print("Total Monthly Salary for Each Employee:")
            for idx, employee in enumerate(results, start=1):
                print(f"\nEmployee {idx}:")
                print("Name:", employee[0])
                print("Total Monthly Salary:", employee[1])
        else:
            print("No employees found.")

    except Error as e:
        print(f"Error calculating total monthly salary: {e}")

    finally:
        cursor.close()


import csv


# Function to export employee data to a CSV file
def export_employee_data_to_csv(connection, csv_file_path):
    try:
        cursor = connection.cursor()

        # SQL query to select all employee data
        query = """
            SELECT Name, Age, Address, Mobile_Number, Gender, Education_Details, Salary, DOJ, Department, Position, Project_Name, Tech_Stack, Annual_Salary,manager
            FROM emss1
        """
        # Execute the query
        cursor.execute(query)
        # Fetch all results
        results = cursor.fetchall()
        # Write data to CSV file
        with open(csv_file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Write header row
            writer.writerow(['Name', 'Age', 'Address', 'Mobile_Number', 'Gender', 'Education_Details', 'Salary', 'DOJ',
                             'Department', 'Position', 'Project_Name', 'Tech_Stack', 'Annual_Salary', 'manager'])
            # Write data rows
            writer.writerows(results)

        print(f"Employee data exported to '{csv_file_path}' successfully.")

    except Error as e:
        print(f"Error exporting employee data to CSV: {e}")

    finally:
        if connection.is_connected():
            cursor.close()


def assign_projects(connection):
    try:
        cursor = connection.cursor()

        # SQL query to select employees without assigned projects
        select_query = """
            SELECT Name
            FROM emss1
            WHERE Project_Name IS NULL
        """
        # Execute the select query
        cursor.execute(select_query)
        # Fetch all results
        emss1_without_projects = cursor.fetchall()
        if emss1_without_projects:
            for employee in emss1_without_projects:
                # SQL query to select a project not assigned to any employee
                update_query = """
                    UPDATE emss1
                    SET Project_Name = (
                        SELECT Project_Name
                        FROM (
                            SELECT DISTINCT Project_Name
                            FROM emss1
                            WHERE Project_Name NOT IN (
                                SELECT Project_Name
                                FROM emss1
                                WHERE Name = %s
                            )
                        ) AS temp
                        LIMIT 1
                    )
                    WHERE Name = %s
                """
                # Execute the update query
                cursor.execute(update_query, (employee[0], employee[0]))
                connection.commit()

            print("Projects assigned successfully.")

        else:
            print("All employees already have projects assigned.")

    except Error as e:
        print(f"Error assigning projects: {e}")

    finally:
        if connection.is_connected():
            cursor.close()


def view_employee_projects(connection):
    cursor = connection.cursor()

    # Get employee's name
    employee_name = input("Enter the name of the employee: ")

    try:
        # Retrieve current project details for the employee
        cursor.execute("""
            SELECT Project_Name, Tech_Stack, Annual_Salary
            FROM emss1
            WHERE Name = %s
        """, (employee_name,))
        present_projects = cursor.fetchall()

        # Retrieve past project details for the employee
        cursor.execute("""
            SELECT Project_Name
            FROM emss1
            WHERE Name = %s
        """, (employee_name,))
        past_projects = cursor.fetchall()

        # Display present project details
        if present_projects:
            print("\nPresent Projects:")
            for project in present_projects:
                print(f"Project Name: {project[0]}, Tech Stack: {project[1]}, Annual Salary: {project[2]}")
        else:
            print("No present projects found for the employee.")

        # Display past project details
        if past_projects:
            print("\nPast Projects:")
            for project in past_projects:
                print(f"Project Name: {project[0]}")
        else:
            print("No past projects found for the employee.")

    except Error as e:
        print(f"Error viewing employee projects: {e}")
    finally:
        cursor.close()


def update_employee_project(connection):
    cursor = connection.cursor()

    # Get employee's name
    employee_name = input("Enter the name of the employee: ")

    # Get the new project details
    new_project_name = input("Enter the new project name: ")
    new_tech_stack = input("Enter the new tech stack: ")
    new_annual_salary = input("Enter the new annual salary: ")

    try:
        # Retrieve past project details for the employee
        cursor.execute("""
            SELECT Project_Name
            FROM emss1
            WHERE Name = %s
        """, (employee_name,))
        past_projects = cursor.fetchall()

        # Update the employee's current project
        cursor.execute("""
            UPDATE emss1
            SET Project_Name = %s, Tech_Stack = %s, Annual_Salary = %s
            WHERE Name = %s
        """, (new_project_name, new_tech_stack, new_annual_salary, employee_name))

        connection.commit()

        print("Employee's project details updated successfully.")

        # Display past project details
        if past_projects:
            print("\nPast Projects:")
            for project in past_projects:
                print(f"Project Name: {project[0]}")
        else:
            print("No past projects found for the employee.")
    except Error as e:
        connection.rollback()
        print(f"Error updating project details: {e}")
    finally:
        cursor.close()


def add_tech_stack_for_employee(connection):
    cursor = connection.cursor()

    # Get employee's name
    employee_name = input("Enter the name of the employee: ")

    # Get the tech stack
    tech_stack = input("Enter the tech stack for the employee: ")

    try:
        # Update the employee's tech stack
        cursor.execute("""
            UPDATE emss1
            SET tech_stack = %s
            WHERE Name = %s
        """, (tech_stack, employee_name))

        connection.commit()

        print("Tech stack added successfully.")

    except Error as e:
        connection.rollback()
        print(f"Error adding tech stack: {e}")

    finally:
        cursor.close()


def view_employee_tech_stack(connection):
    cursor = connection.cursor()
    # Get employee's name
    employee_name = input("Enter the name of the employee: ")

    try:
        # Query to retrieve department and tech stack based on employee's name
        cursor.execute("""
            SELECT Department, Tech_Stack
            FROM emss1
            WHERE Name = %s
        """, (employee_name,))

        employee_info = cursor.fetchone()

        if employee_info:
            department, tech_stack = employee_info
            if department.lower() == 'engineering' or department.upper() == 'ENGINEERING':
                print(f"Tech Stack of {employee_name}: {tech_stack}")
            else:
                print(f"{employee_name} does not belong to the engineering department.")
        else:
            print("Employee not found.")

        # Consume or close the result set
        cursor.close()

    except Error as e:
        print(f"Error retrieving employee's information: {e}")


def search_employee_by_name(connection):
    cursor = connection.cursor()

    # Get the name to search for
    search_name = input("Enter the name of the employee to search: ")

    try:
        # Query to search for employees by name
        cursor.execute("""
            SELECT DISTINCT Name, Age, Address, Mobile_Number, Gender, Education_Details, Salary, DOJ, Department, Position, Project_Name, Tech_Stack, Annual_Salary
            FROM emss1
            WHERE Name LIKE %s
        """, ('%' + search_name + '%',))  # Using wildcard to search for partial matches

        # Fetch all matching results
        results = cursor.fetchall()

        if results:
            print("Search Results:")
            for idx, employee in enumerate(results, start=1):
                print(f"\nEmployee {idx}:")
                print("Name:", employee[0])
                print("Age:", employee[1])
                print("Address:", employee[2])
                print("Mobile Number:", employee[3])
                print("Gender:", employee[4])
                print("Education Details:", employee[5])
                print("Salary:", employee[6])
                print("Date of Joining:", employee[7])
                print("Department:", employee[8])
                print("Position:", employee[9])
                print("Project Name:", employee[10])
                print("Tech Stack:", employee[11])
                print("Annual Salary:", employee[12])
        else:
            print("No matching employees found.")

    except Error as e:
        print(f"Error searching for employees: {e}")

    finally:
        cursor.close()


def search_employee_by_tech_stack(connection):
    cursor = connection.cursor()

    # Get the tech stack to search for
    tech_stack = input("Enter the tech stack to search: ")

    try:
        # Query to search for employees by tech stack
        cursor.execute("""
            SELECT DISTINCT Name, Age, Address, Mobile_Number, Gender, Education_Details, Salary, DOJ, Department, Position, Project_Name, Tech_Stack, Annual_Salary
            FROM emss1
            WHERE Tech_Stack LIKE %s
        """, ('%' + tech_stack + '%',))  # Using wildcard to search for partial matches

        # Fetch all matching results
        results = cursor.fetchall()

        if results:
            print("Search Results:")
            for idx, employee in enumerate(results, start=1):
                print(f"\nEmployee {idx}:")
                print("Name:", employee[0])
                print("Age:", employee[1])
                print("Address:", employee[2])
                print("Mobile Number:", employee[3])
                print("Gender:", employee[4])
                print("Education Details:", employee[5])
                print("Salary:", employee[6])
                print("Date of Joining:", employee[7])
                print("Department:", employee[8])
                print("Position:", employee[9])
                print("Project Name:", employee[10])
                print("Tech Stack:", employee[11])
                print("Annual Salary:", employee[12])
        else:
            print("No matching employees found.")

    except Error as e:
        print(f"Error searching for employees: {e}")

    finally:
        cursor.close()


def search_employee_by_project_name(connection):
    cursor = connection.cursor()

    # Get the project name to search for
    project_name = input("Enter the project name to search: ")

    try:
        # Query to search for employees by project name
        cursor.execute("""
            SELECT DISTINCT Name, Age, Address, Mobile_Number, Gender, Education_Details, Salary, DOJ, Department, Position, Project_Name, Tech_Stack, Annual_Salary
            FROM emss1
            WHERE Project_Name LIKE %s
        """, ('%' + project_name + '%',))  # Using wildcard to search for partial matches

        # Fetch all matching results
        results = cursor.fetchall()

        if results:
            print("Search Results:")
            for idx, employee in enumerate(results, start=1):
                print(f"\nEmployee {idx}:")
                print("Name:", employee[0])
                print("Age:", employee[1])
                print("Address:", employee[2])
                print("Mobile Number:", employee[3])
                print("Gender:", employee[4])
                print("Education Details:", employee[5])
                print("Salary:", employee[6])
                print("Date of Joining:", employee[7])
                print("Department:", employee[8])
                print("Position:", employee[9])
                print("Project Name:", employee[10])
                print("Tech Stack:", employee[11])
                print("Annual Salary:", employee[12])
        else:
            print("No matching employees found.")

    except Error as e:
        print(f"Error searching for employees: {e}")

    finally:
        cursor.close()


def sort_emss1_by_salary(connection):
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT DISTINCT Name, Annual_Salary
            FROM emss1
            WHERE Annual_Salary IS NOT NULL
            ORDER BY Annual_Salary DESC
        """)
        sorted_emss1 = cursor.fetchall()

        if sorted_emss1:
            for employee in sorted_emss1:
                print(f"Name: {employee[0]}, Annual Salary: {employee[1]}")
        else:
            print("No employees found.")

        # Fetch all remaining rows to ensure the result set is completely read
        cursor.fetchall()

    except Error as e:
        print(f"Error sorting employees by salary: {e}")
    finally:
        cursor.close()


def assign_managers(connection):
    try:
        cursor = connection.cursor()

        # SQL query to select employees without assigned managers
        select_query = """
            SELECT Name
            FROM emss1
            WHERE Manager IS NULL
        """

        # Execute the select query
        cursor.execute(select_query)

        # Fetch all results
        employees_without_managers = cursor.fetchall()

        if employees_without_managers:
            for employee in employees_without_managers:
                # SQL query to select a manager not assigned to any other employee
                update_query = """
                    UPDATE emss1 AS e1
                    JOIN (
                        SELECT Manager
                        FROM emss1
                        WHERE Manager IS NOT NULL
                        GROUP BY Manager
                        HAVING COUNT(*) = 1
                        LIMIT 1
                    ) AS e2 ON e1.Manager = e2.Manager
                    SET e1.Manager = e2.Manager
                    WHERE e1.Name = %s
                    AND e1.Manager IS NULL
                """
                # Execute the update query
                cursor.execute(update_query, (employee[0],))
                connection.commit()

            print("Managers assigned successfully.")

        else:
            print("All employees already have managers assigned.")

    except Error as e:
        print(f"Error assigning managers: {e}")

    finally:
        if connection.is_connected():
            cursor.close()


def view_manager_details(connection):
    try:
        cursor = connection.cursor()
        employee_name = input("Enter the name of the employee: ")

        # SQL query to view manager details of the specified employee along with mentees
        query = """
            SELECT 
                Manager,
                Name
            FROM 
                emss1
            WHERE 
                (Manager IS NOT NULL AND Manager != 'None' AND Name != Manager)
                AND Name = %s
            UNION
            SELECT 
                Manager,
                Name
            FROM 
                emss1
            WHERE 
                Name = Manager AND Name = %s
        """

        # Execute the query with the employee name as parameter
        cursor.execute(query, (employee_name, employee_name))

        # Fetch all results
        manager_details = cursor.fetchall()

        # Print the results
        if manager_details:
            print(f"Manager Details for {employee_name}:")
            for manager, mentee in manager_details:
                print(f"Manager: {manager}, Mentee: {mentee}")
        else:
            print(f"No manager details found for employee: {employee_name}")

    except mysql.connector.Error as error:
        print(f"Error viewing manager details: {error}")

    finally:
        if connection.is_connected():
            cursor.close()


# Function to import employee data from a CSV file
def import_employee_data(file_path):
    employee_data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            employee_data.append(row)
    return employee_data


def main():
    host = "127.0.0.1"
    user = "root"
    password = "Nayan@12345"
    database = "ems3project"

    # Connect to MySQL database
    connection = connect_to_mysql(host, user, password, database)
    if connection:
        create_table(connection)
        insert_data_from_csv(connection, '/home/nineleaps/Downloads/all.csv')

    while True:
        print("\nMenu:")
        print("1.  Add a new employee")
        print("2.  View a particular employee's details")
        print("3.  Update employee information")
        print("4.  Delete employee record ")
        print("5.  List all employees in the organization")
        print("6.  Calculate total monthly salary for each employee")
        print("7.  Export employee data to a CSV file")
        print("8.  Assign projects to employees ")
        print("9.  View employee projects ")
        print("10  Update employee project ")
        print("11. Add tech stack for employees")
        print("12. View employee's known tech stack")
        print("13. Search by employee name ")
        print("14. Search employees by tech stack")
        print("15  Search employee by project name")
        print("16 sort employees by salary ")
        print("17 Assign Manager")
        print("18 View Manager Details")
        print("19. Import employee data from a CSV file")
        print("20. Exit")
        option = input("Enter your choice (1, 2, 3, 4, 5, 6, 7, 8 ,9 , 10 ,11, 12 , 13 , 14 ,15, 16 , 17, 18,19,20): ")

        if option == '1':
            add_new_employee(connection)
        elif option == '2':
            view_employee_details(connection)
        elif option == '3':
            update_employee(connection)
        elif option == '4':
            delete_inactive_emss1(connection)
        elif option == '5':
            list_all_emss1(connection)
        elif option == '6':
            calculate_total_monthly_salary(connection)
        elif option == '7':
            export_employee_data_to_csv(connection, csv_file_path="/home/nineleaps/Downloads/useme.csv")
        elif option == '8':
            assign_projects(connection)
        elif option == '9':
            view_employee_projects(connection)
        elif option == '10':
            update_employee_project(connection)
        elif option == '11':
            add_tech_stack_for_employee(connection)
        elif option == '12':
            view_employee_tech_stack(connection)
        elif option == '13':
            search_employee_by_name(connection)
        elif option == '14':
            search_employee_by_tech_stack(connection)
        elif option == '15':
            search_employee_by_project_name(connection)
        elif option == '16':
            sort_emss1_by_salary(connection)
        elif option == '17':
            assign_managers(connection)
        elif option == '18':
            view_manager_details(connection)
        elif option == '19':
            file_path = input("Enter the path to the CSV file: ")
            employee_data = import_employee_data(file_path)
            # You can process the imported employee data here
            print("Employee data imported successfully.")
        elif option == '20':
            break
        else:
            print("Invalid option. Please try again.")

    if connection.is_connected():
        connection.close()
        print("MySQL connection closed.")


if __name__ == "__main__":
    main()

