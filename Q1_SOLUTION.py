''' Q1. Which hour has the highest frequency of candidates scheduled to take up exams? 
        Show the plot diagram of the frequencies.
'''

import pandas as pd 
from matplotlib import pyplot as plt 

data = pd.read_csv('D:/MyPython/4python_pandas/GRE_Reg_Data.csv')

data['HOUR'] = data['TIME OCC'] // 100    # extracting the hour part from TIME OCC
freq = data['HOUR'].value_counts()       # counting the frequency of each hour in a day
freq = freq.sort_index()   # sorting the series by its index (which is the hour here) to ensure that the bars in the bar chart will be displayed in the correct order of the hours in a day
max_hour = freq.idxmax()   # determining the hour that has the highest frequency of candidates scheduled to take exams

# Constructing the bar chart
bars = plt.bar(freq.index, freq.values, color=['green' if hour != max_hour else 'red' for hour in freq.index])

# Setting the labels and title
plt.title(' Frequency of Candidates Scheduled to Take up Exams by Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Frequency of Candidates')
plt.xticks(range(24))   # ensures the x-axis shows all 24 hours of the day
plt.bar_label(bars, label_type='edge')

plt.show()  # Displaying the chart

print('hour having the highest frequency of candidates scheduled to take up exams:',max_hour)