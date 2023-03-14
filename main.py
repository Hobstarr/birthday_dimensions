import random
from datetime import date, datetime, timedelta
import calendar
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

def create_n_random_dates(n = 100, years = 100):
    days_per_year = 365.24
    hundred_years_datetime = timedelta(days=(years*days_per_year))

    end = datetime.now()
    start = end - hundred_years_datetime

    date_list = []
    for i in range(n):
        random_date = start + (end-start) * random.random()
        date_edit = [random_date.day, random_date.month, 
                     random_date.year, random_date.weekday()]
        date_list.append(date_edit)

    return date_list

big_dates = create_n_random_dates(n = 100)
plt.title('histogram of birthdays of the week')
plt.hist([x[3]+1 for x in big_dates], 7)
plt.show()

plt.title('histogram of birthdays of the month')
plt.hist([x[0]+1 for x in big_dates], 31)
plt.show()

plt.title('scatter plot of birthdays of the day, and month')
plt.scatter(x = [x[0]+1 for x in big_dates], 
            y = [x[1]+1 for x in big_dates])
plt.xlabel('days of the month')
plt.ylabel('months of the year')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_title('scatter plot of birthdays of the day, month, year')
ax.scatter([x[0]+1 for x in big_dates], 
            [x[1]+1 for x in big_dates],
            [x[2] for x in big_dates])

ax.set_xlabel('days of the month')
ax.set_ylabel('months of the year')
ax.set_zlabel('year')
plt.show()