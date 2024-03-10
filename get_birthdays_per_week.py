from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    today = datetime.today().date()
    birthdays = {}  # Empty dictionary

    for user in users:
        birthday = user["birthday"].date()
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        delta_days = (birthday - today).days
        if delta_days < 7:
            weekday = (today + timedelta(days=delta_days)).strftime("%A")
            birthdays.setdefault(weekday, []).append(user["name"] + " " + user["surname"])

    for weekday, names in birthdays.items():
        print(f"{weekday}: {', '.join(names)}")

users = [
    {"name": "John", "surname": "Forbes Nash Jr.", "birthday": datetime(1928, 6, 13)},
    {"name": "Andrew", "surname": "Wiles", "birthday": datetime(1953, 4, 11)},
    {"name": "Guido", "surname": "van Rossum", "birthday": datetime(1956, 1, 31)},
    {"name": "Satya", "surname": "Nadella", "birthday": datetime(1967, 8, 19)},
    {"name": "Demis", "surname": "Hassabis", "birthday": datetime(1976, 7, 27)},
]

get_birthdays_per_week(users)
