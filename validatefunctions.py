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
