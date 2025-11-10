from datetime import datetime, date

birthday = input("Enter your birthday (YYYY-MM-DD): ")
bday = datetime.strptime(birthday, "%Y-%m-%d").date()

today = date.today()
next_bday = date(today.year, bday.month, bday.day)

if next_bday < today:
    next_bday = date(today.year + 1, bday.month, bday.day)

remaining = next_bday - today
print(f"Days remaining: {remaining.days}")
