''' Q3.	Identify the number of candidates scheduled to write exam in different age groups, 
        with age group labels "0-17", "18-25", "26-34", "35-44", "45-54", "55-64", and "65+"
        as the index and the frequency of candidates scheduled as the values.
'''

import pandas as pd 
from matplotlib import pyplot as plt 

data = pd.read_csv('D:/MyPython/4python_pandas/GRE_Reg_Data.csv')

#3
# initializing a dictionary named 'age_groups' with age group labels as keys and their corresponding values set to 0
age_groups = {"0-17": 0, "18-25": 0, "26-34": 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0}

# iterating over the age column, checking the age falls in which age group and incrementing the corresponding age_group
for age in data['Age']:
    if age <= 17:
        age_groups["0-17"] += 1
    elif 18 <= age <= 25:
        age_groups["18-25"] += 1
    elif 26 <= age <= 34:
        age_groups["26-34"] += 1
    elif 35 <= age <= 44:
        age_groups["35-44"] += 1
    elif 45 <= age <= 54:
        age_groups["45-54"] += 1
    elif 55 <= age <= 64:
        age_groups["55-64"] += 1
    else:
        age_groups["65+"] += 1

# Constructing the bar chart
bars = plt.bar(age_groups.keys(), age_groups.values(), color='skyblue')

# Setting the labels and title
plt.title('Number of Candidates in Different Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Frequency of Candidates')
plt.bar_label(bars, label_type='edge')

plt.show()  # Displaying the plot