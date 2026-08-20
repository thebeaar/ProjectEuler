def day_of_month(month, year):
    dictionary = {1: 31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if month in dictionary:
        return dictionary[month]
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 29
    return 28
day = 2 ## monday
for month in range(1, 13):
    day += day_of_month(month, 1900) % 7
    day %= 7

count = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if day == 1:
            count += 1
        day += day_of_month(month, 1900) % 7
        day %= 7
print(count)