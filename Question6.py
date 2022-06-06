import pandas as pd
import matplotlib.pyplot as plt

data = [
        ['E001', 'M', 34, 123, 'Normal', 350, 31],
        ['E002', 'F', 40, 114, 'Overweight', 450, 35],
        ['E003', 'F', 37, 135, 'Obesity', 169, 34],
        ['E004', 'M', 30, 139, 'Underweight', 189, 36],
        ['E005', 'F', 44, 117, 'Underweight', 183, 30],
        ['E006', 'M', 36, 121, 'Normal', 80, 38],
        ['E007', 'M', 32, 132, 'Obesity', 166, 34],
        ['E008', 'F', 26, 140, 'Normal', 120, 37],
        ['E009', 'M', 32, 131, 'Normal', 75, 35],
        ['E0010', 'M', 36, 133, 'Underweight', 40, 36]]

df = pd.DataFrame(data, columns = ['EMPID', 'Gender', 'Age', 'Sales', 'BMI', 'Income', 'Loss'])

"""
# Indexing of the list of variables
Amount = pd.Series(index=[1,2,3,4,5,6,7,8,9,10],data= df.Sales,name='Sales')
print(Amount)

# Counting the value of variables && Plotting a Pie Chart
count = Amount.value_counts()
print(count)
count.plot(kind = 'pie')
Sales = df.Gender.value_counts()
Sales.plot.pie()
"""

# Define the ratio of gap of each fragment
colors = ['red','orange']
explode = (0.05,0.05)
df.groupby(['Gender']).sum().plot(kind = 'pie', y = 'Sales', autopct = '%1.0f%%', colors = colors, explode=explode, shadow =True, startangle = 60)

# Plotting a Bar Graph
df.plot.bar()
plt.bar(df['Income'],df['Sales'])
plt.xlabel("Income")
plt.ylabel("Sales")
plt.show()

