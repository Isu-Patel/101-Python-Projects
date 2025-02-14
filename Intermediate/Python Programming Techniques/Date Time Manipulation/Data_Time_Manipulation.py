from datetime import datetime, date, timedelta

# Get the current date and time
now = datetime.now()  # returns the current local date and time

# Get today's date
today = datetime.today().date()  # returns the current local date

# Get a specific date
specific_date = date(2023, 5, 17)  # returns a date object for May 17, 2023

# Format the current date and time
formmated_date = now.strftime("%Y-%m-%d %H:%M:%S")  # formats the date and time as a string

# Get tomorrow's date
today = datetime.today()  # returns the current local date and time
tomorrow = today + timedelta(days=1)  # adds one day to the current date

# Print the results
print(f"Current date and time: {now}")  # prints the current date and time
print(f"Today's date is: {today}")  # prints today's date
print(f"Specific date: {specific_date}")  # prints the specific date
print(f"Formatted date: {formmated_date}")  # prints the formatted date and time
print(f"Tomorrow's Date: {tomorrow}")  # prints tomorrow's date
