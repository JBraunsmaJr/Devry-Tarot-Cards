from calendar import monthrange

# we are including abbreviated month names as well...
months = {
    "january": 1,
    "jan": 1,
    "february": 2,
    "feb": 2,
    "march": 3,
    "mar": 3,
    "april": 4,
    "apr": 4,
    "may": 5,
    "june": 6,
    "jun": 6,
    "july": 7,
    "jul": 7,
    "august": 8,
    "aug": 8,
    "september": 9,
    "sept": 9,
    "october": 10,
    "oct": 10,
    "november": 11,
    "nov": 11,
    "december": 12,
    "dec": 12
}

def input_day_of_month(prompt, month, year, error_message = "The spirits do not understand, please try again."):
    """
    we want to ensure our day selection is accurate... 31 days in feb should never happen!
    """
    # acquire the number version of the month
    month_num = months[month]

    # month range returns a tuple, we want the last item which represents the days in month
    max = monthrange(year, month_num)[-1]

    while True:
        try:
            value = int(input(prompt))
            if value <= max:
                return value
            else:
                # inform the user how many days are in the month they picked.. for that year
                print("There are only {} days in {} for the year {}".format(max, month, year))
        except ValueError:
            print(error_message)


def input_number(prompt, error_message="The spirits do not understand, please try again."):
	"""
		We want a number input
		Ensure we receive valid input, provide user with an error message if invalid
	"""

	value = -1 # default value of -1... assuming functions relying on this assume the result WILL be a number

	while True:
		try:
			value = int(input(prompt))
			return value
		except ValueError:
			print(error_message)


def input_month(prompt, error_message = "The spirits do not understand, please try again."):
    """
    Force user to enter a correct month
    """
    while True:
        input_month = input(prompt).lower()

        if input_month in months.keys():
            return input_month
        else:
            print(error_message)


def input_bool(prompt, error_message = "The spirits do not understand, please try again."):
    while True:
        answer = input(prompt).lower()

        if answer == "yes" or answer == "y" or answer == "true":
            return True
        elif answer == "no" or answer == "n" or answer == "false":
            return False
        else:
            print(error_message)
