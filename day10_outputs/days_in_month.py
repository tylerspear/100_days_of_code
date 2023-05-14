def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  return month_days[month-1]

user_choice_month = int(input("What month to know the days for? "))
if user_choice_month == 2:
    user_choice_year = int(input("What year? "))
    if is_leap(user_choice_year):
        print(f"That month has 29 days in it.")
    else:
        print(f"That month has 28 days in it.")

else:
    print(f"That month has {days_in_month(user_choice_month)} days in it.")
