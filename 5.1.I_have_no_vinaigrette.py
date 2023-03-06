import datetime
import random


def main():
    """
    This function prompts the user to enter two dates and generates a random date between them.
    It then checks the day of the week of the random date and prints a message if it is Monday.

    Args:
    None.

    Returns:
    None. The function prints a message to the console if the random date is a Monday.
    """
    try:
        # Gets user input
        date1 = input("Please enter a  first date (YYYY-MM-DD): ")
        date2 = input("Please enter a second date (YYYY-MM-DD): ")

        # Converts to date objects
        date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")

        # if date1 is later than date2
        if date1 > date2:
            temp = date1
            date1 = date2
            date2 = temp

        # Generates random date between the 2 days
        random_date_between = date1 + (date2 - date1) * random.random()

        # Checks it's day of the week
        day_of_week = random_date_between.strftime('%A')

        if day_of_week == 'Monday':
            print("I have no vinaigrette!")

    except ValueError:
        print("Check your input")


if __name__ == "__main__":
    main()
