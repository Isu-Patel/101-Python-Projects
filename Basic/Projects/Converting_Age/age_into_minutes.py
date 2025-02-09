age_year = int(input("Enter your age in years: "))

# Calculate the approximate number of minutes the user has lived
# 1 year = 365 days, 1 day = 24 hours, 1 hour = 60 minutes
minutes = age_year * 365 * 24 * 60

# Display the result to the user
print(f"You have lived for approximately {minutes} minutes.")

# ---------------------------- Output ---------------------------- #
# Enter your age in years: 25
# You have lived for approximately 1314000 minutes.
