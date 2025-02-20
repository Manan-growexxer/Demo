from datetime import date
import re
try:
    
    birth_date_input = input("Enter your birthdate (YYYY-MM-DD): ")

    
    year, month, day = map(int, birth_date_input.split('-'))

    if not re.match(r'^\d{4}-\d{2}-\d{2}$', birth_date_input):
        raise ValueError("Invalid date format. Please enter the date as YYYY-MM-DD.")

    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12.")
    if not (1 <= day <= 31):
        raise ValueError("Day must be between 1 and 31.")
    if month == 2 and day > 29:
        raise ValueError("February cannot have more than 29 days.")
    if month in {4, 6, 9, 11} and day > 30:
        raise ValueError(f"Month {month} cannot have more than 30 days.")

    
    current_year = date.today().year
    current_month = date.today().month
    current_day = date.today().day

    
    age = current_year - year
    if (current_month, current_day) < (month, day):
        age -= 1

    if age < 18:
        print("Age must be at least 18 to be eligible for a driving license.")
    elif age > 65:
        print("Age must be 65 or younger to be eligible for a driving license.")
    else:
        print("You are eligible for a driving license.")

except ValueError as ve:
    print(f"Invalid input: {ve}")

  

