# Given your birthday, in the format "DD-MM-YYYY", write a function that calculates how many days have passed since your birthday (without counting the days in your birth year and the current year, so just whole years).
# The function takes your birthday as a parameter in string format.
# Do not import anything, use only what we learned in class
def days_since_birthday(birthday):
    """
    Calculates how many days have passed since the birth year
    (excluding the birth year and current year), including leap years.

    :param birthday: A string in "DD-MM-YYYY" format.
    :return: Number of days passed.
    """
    # Extract birth year from the input string
    birth_year = int(birthday[-4:])  # The last 4 characters represent the year

    # Ask the user for the current year
    current_year = int(input("Enter the current year: "))

    # Calculate whole years in between (excluding birth year & current year)
    whole_years = current_year - birth_year - 1

    # Count the number of leap years in the range
    leap_years = 0
    for year in range(birth_year + 1, current_year):  # Exclude birth year and current year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years += 1  # Count leap years

    # Calculate total days (365 days for normal years, 366 for leap years)
    total_days = (whole_years * 365) + leap_years

    return total_days

# Example usage
birthday = "09-05-2005"
print("Days passed:", days_since_birthday(birthday))