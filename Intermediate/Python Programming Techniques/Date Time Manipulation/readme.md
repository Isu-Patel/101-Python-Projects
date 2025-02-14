# Date and Time Manipulation in Python

This repository explores date and time manipulation in Python using the `datetime` module.  It covers various techniques for working with dates, times, timedeltas, and time zones, providing clear examples and explanations.

## What is Date and Time Manipulation?

Date and time manipulation involves working with dates and times in various ways, such as:

* Creating date and time objects
* Formatting dates and times
* Performing calculations with dates and times (e.g., finding the difference between two dates)
* Handling time zones
* Converting between different date and time formats

## The `datetime` Module

Python's built-in `datetime` module provides classes for working with dates, times, and timedeltas.

### Date Objects

```python
import datetime

# Get the current date
today = datetime.date.today()
print(f"Today's date: {today}")

# Create a date object
my_date = datetime.date(2024, 10, 26)  # Year, month, day
print(f"My date: {my_date}")

# Accessing date components
year = my_date.year
month = my_date.month
day = my_date.day
print(f"Year: {year}, Month: {month}, Day: {day}")

# Formatting dates
formatted_date = my_date.strftime("%Y-%m-%d")  # Example format
print(f"Formatted date: {formatted_date}")

# Parsing dates from strings
date_string = "2024-10-26"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
print(f"Parsed date: {parsed_date}")
