''' Q2.	Create stacked bar graph of the number of candidates taken exam both at 
        day and night (Day being 06:00 AM to 09:00 PM)
'''

import pandas as pd 
from matplotlib import pyplot as plt 

data = pd.read_csv('D:/MyPython/4python_pandas/GRE_Reg_Data.csv')

data['Hour'] = data['TIME OCC'] // 100  # extracting the hour part from TIME OCC

day = list(range(6, 22))  # day list contains hours from 6 AM to 9:59 PM (6:00 to 21:59)
night = list(range(0, 6)) + list(range(22, 24))  # night list contains hours from 12 AM to 5:59 AM (0:00 to 5:59) and from 10 PM to 11:59 PM (22:00 to 23:59)

periods = []  # initializing an empty list 'periods'
for hour in data['Hour']:
    if hour in day:
        periods.append('Day')   # if the hour is in the day list, then appending 'Day' to the periods list
    else:
        periods.append('Night') # if the hour is in the night list, then appending 'Night' to the periods list

data['Period'] = periods    #  adding the periods list as a new column named 'Period'

period_frequency = data['Period'].value_counts()  # counting the number of candidates scheduled for exams during the day and night

day_count = period_frequency.get('Day', 0)      # extracting the counts for 'Day'
night_count = period_frequency.get('Night', 0)  # extracting the counts for 'Night'

# Creating a plot
fig, ax = plt.subplots()

# Plotting the day bar
day_bar = ax.bar('Day/Night', day_count, color='skyblue', label='Day')

# Plotting the night bar on top of the day bar to create a stacked bar graph
night_bar = ax.bar('Day/Night', night_count, bottom=day_count, color='green', label='Night')

# Setting the labels and title
ax.set_title('Number of Candidates Taken Exam at Day and Night')
ax.set_ylabel('Number of Candidates')
ax.bar_label(day_bar, labels=[day_count], label_type='center')
ax.bar_label(night_bar, labels=[night_count], label_type='center')

ax.legend()   # Adding a legend to differentiate between day and night bars
plt.show()    # Displaying the plot