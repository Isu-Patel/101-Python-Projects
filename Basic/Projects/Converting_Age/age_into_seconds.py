# Prompt the user to enter their age in years
age_year = int(input("Enter your age in years: "))

# Calculate the number of seconds in the given age
# 1 year = 365 days, 1 day = 24 hours, 1 hour = 60 minutes, 1 minute = 60 seconds
seconds = age_year * 365 * 24 * 60 * 60

# Output the result to the user
print(f"You have lived for approximately {seconds} seconds.")

# ---------------------------- Output ---------------------------- #
# Enter your age in years: 25
# You have lived for approximately 788400000 seconds.
