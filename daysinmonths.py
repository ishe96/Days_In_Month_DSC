def is_leap(year):
    leap = 0
    
    if year% 4 == 0:

        if year% 100 == 0:

            if year% 400 == 0:
                print("Leap year.")
            else:
                print("Not leap year.")
        else:
            print("Leap year.")
    else:
        print("Not leap year.")

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_month_days = [0, 29]

    while month in {1, 3, 5, 7, 8, 10, 12}:
        if is_leap(year):
            return
        return 31
        
    while month in (4, 6, 9, 11):
        if is_leap(year):
            return
        return 30

    if month == 2 and is_leap(year):
        print(leap_month_days[month == 2])
    return month_days[month == 2]
    
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)