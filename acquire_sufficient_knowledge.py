# Did you acquire sufficient knotsoadequatewledge regarding your role and responsibilities in higher education?

import pandas as pd
import matplotlib.pyplot as plt

teacher = 43


# Load the data from the Excel sheet
df = pd.read_excel('feedbackdata.xlsx')


# Select the specified column by name and load all values
column_data = df.iloc[:, 3+teacher+teacher+teacher+teacher+8].tolist()

# Print the column values
# print(column_data)

# adequate = 0
# notsoadequate = 0
# notatalladequate = 0

for i in column_data:
    if i.lower()=='adequate':
        adequate = adequate + 1
    if i.lower()=='no so adequate':
        notsoadequate = notsoadequate + 1
    if i.lower()== 'not at all adequate':
        notatalladequate = notatalladequate + 1

print(adequate)
print(notsoadequate)
print(notatalladequate)

total = (adequate + notsoadequate + notatalladequate)

adequate = (adequate*100)/total

notsoadequate = (notsoadequate*100)/total

notatalladequate = (notatalladequate*100)/total


x_axis = ['Adequate', 'No so Adequate', 'Not at all Adequate']

y_axis=[adequate, notsoadequate, notatalladequate]

# to plot bar graph
plt.bar(x_axis, y_axis, color='red')

# Add text annotsoadequatetations to each bar
for i in range(len(x_axis)):
    plt.text(i , y_axis[i]+0.2, y_axis[i], ha='center', fontsize=15)


# Set the y-axis tick locations and labels
plt.yticks([10,20,30,40,50,60,70,80,90,100])

# Add labels and title
plt.xlabel('')
plt.ylabel('Values in Percentage %')
plt.title('Did you acquire sufficient knotsoadequatewledge regarding your role and responsibilities in higher education? ', pad=30, fontsize= 20)

# Show the graph
plt.show()