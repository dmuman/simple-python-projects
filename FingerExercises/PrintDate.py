def printDate(date: str) -> str:
    return f'You were born in the year {date[-4:len(date)]}'


dateStr = input("Please, enter your birthday in the form mm/dd/yyyy: ")
print(printDate(dateStr))
