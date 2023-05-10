# Do you have the confidence in developing research proposal and writing research articles?  

import pandas as pd
import matplotlib.pyplot as plt

teacher = 43


# Load the data from the Excel sheet
df = pd.read_excel('feedbackdata.xlsx')


# Select the specified column by name and load all values
column_data = df.iloc[:, 3+teacher+teacher+teacher+teacher+9].tolist()

# Print the column values
# print(column_data)

greatextent = 0
someextent = 0
notatall = 0

for i in column_data:
    if i.lower()=='to some extent':
        someextent = someextent + 1
    if i.lower()=='to a great extent':
        greatextent = greatextent + 1
    if i.lower()== 'not at all':
        notatall = notatall + 1

print(greatextent)
print(someextent)
print(notatall)

total = (someextent + greatextent + notatall)

someextent = (someextent*100)/total

greatextent = (greatextent*100)/total

notatall = (notatall*100)/total



x_axis = ['To a great extent', 'To some extent', 'Not at all']
y_axis=[greatextent,someextent, notatall]

# to plot bar graph
plt.bar(x_axis, y_axis, color='red')

# Add text anverysomeextenttations to each bar
for i in range(len(x_axis)):
    plt.text(i , y_axis[i]+0.2, y_axis[i], ha='center', fontsize=15)


# Set the y-axis tick locations and labels
plt.yticks([10,20,30,40,50,60,70,80,90,100])

# Add labels and title
plt.xlabel('')
plt.ylabel('Values in Percentage %')
plt.title('Do you have the confidence in developing research proposal and writing research articles?', pad=30, fontsize= 20)

# Show the graph
plt.show()