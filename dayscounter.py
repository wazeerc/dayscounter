# The program Days Counter aims to count the numbers of days between two given dates

# import Module Datetime
import datetime

# Date format
date_format = "%d/%m/%Y"

# Ask user for his name
# Stored in variable username
username = input("Hello, Please enter your name: ")
# Welcome User & Ask for starting date
while True:
    try:
        start_date_input = input(f"Hello {username.capitalize()}! Enter your starting date in this format dd/mm/yyyy: ")
        start_date = datetime.datetime.strptime(start_date_input, "%d/%m/%Y")
        break
    except:
        print("Please enter date in correct format e.g: 01/01/2021")
# Ask for end date
while True:
    try:
        end_date_input = input("Enter the ending date in the same format: ")
        end_date = datetime.datetime.strptime(end_date_input, "%d/%m/%Y")
        break
    except:
        print("Please enter date in correct format e.g: 01/01/2021")
# Days counter
number_of_days = (end_date - start_date).days
# Display amount of days
print(f"The number of days between {start_date_input} and {end_date_input} is: {number_of_days} days.")
