# The program Days Counter aims to count the numbers of days between two given dates

# import Module Datetime
import datetime

# Date format
date_format = "%d/%m/%Y"

# Ask user for his name
# Stored in variable username
username = input("Hello, I was created to count days :)\nHow should I call you: ")


# Welcome User & Ask for starting date
class DaysCounter:
    def __init__(self):
        pass

    @staticmethod
    def get_start_date():
        while True:
            try:
                start_date_input = input(
                    f"Hello {username.capitalize()}! Enter your starting date in this format dd/mm/yyyy: ")
                start_date = datetime.datetime.strptime(start_date_input, "%d/%m/%Y")
                today = datetime.date.today()
                break
            except:
                print("Please enter date in correct format e.g: 01/01/2021")
        return start_date, start_date_input

    # Ask for end date
    @staticmethod
    def get_end_date():
        while True:
            try:
                end_date_input = input("Enter the ending date in the same format: ")
                end_date = datetime.datetime.strptime(end_date_input, "%d/%m/%Y")
                break
            except:
                print("Please enter date in correct format e.g: 01/01/2021")
        return end_date, end_date_input


startDate, startDate_input = DaysCounter.get_start_date()
endDate, endDate_input = DaysCounter.get_end_date()


def calculate_days():
    # Calculate the number of days
    number_of_days = (endDate - startDate).days
    # Display amount of days
    print(f"The number of days between {startDate_input} and {endDate_input} is: {number_of_days} days.")


calculate_days()
