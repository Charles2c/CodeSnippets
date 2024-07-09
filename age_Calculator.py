from datetime import datetime


now_Year = (datetime.now().year)
now_Month = (datetime.now().month)
now_day = (datetime.now().day)

birth_year = int(input("Enter your Birth Year "))
if birth_year > now_Year:
    print('You are born in the future?')
    birth_year = int(input("Enter your correct Birth Year "))
else:
    birth_month = int(input("Enter your Birth Month "))
    if birth_month > 12:
        print('there are only 12 months in a year')
    else:
        birth_day = int(input("Enter your Birth Date "))
        if birth_day > 31:
            print('Max 31')
        elif birth_day < 1:
            print('Min 1')
        else:
            birth_day


now_Year = (datetime.now().year)
now_Month = (datetime.now().month)
now_day = (datetime.now().day)

current_day = 0
if now_day > birth_day:
    current_day = now_day - birth_day
else:
    birth_day > now_day
    current_day = birth_day - now_day

current_month = 0
if now_Month > birth_month:
    current_month = now_Month - birth_month
else:
    birth_month > now_Month
    current_month = birth_month - birth_day
# current_age = (now_Year - birth_year), ' years ', current_month, ' months ', ' and ' , current_day, ' days'
print('Your Current Age is: ', (now_Year - birth_year), 'years ', current_month, 'months ', ' and ' , current_day, 'days')