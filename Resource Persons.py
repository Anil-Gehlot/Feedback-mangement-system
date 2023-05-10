
import pandas as pd
import matplotlib.pyplot as plt

teacher = 43


# Load the data from the Excel sheet
df = pd.read_excel('feedbackdata.xlsx')


# Select the specified column by name and load all values
column_data = df.iloc[:, 3+teacher+teacher+teacher+teacher+2].tolist()

# Print the column values
# print(column_data)

very_competent = 0
competent = 0
not_so_competent = 0

for i in column_data:
    if i.lower()=='very competent':
        very_competent = very_competent + 1
    if i.lower()=='competent':
        competent = competent + 1
    if i.lower()== 'not so competent':
        not_so_competent = not_so_competent + 1

total = very_competent + competent + not_so_competent

very_competent = (very_competent*100)/total
competent = (competent*100)/total
not_so_competent = (not_so_competent*100)/total



x_axis = ['Very Competent', 'Competent', 'Not So Competent']
y_axis=[very_competent, competent, not_so_competent]

# to plot bar graph
plt.bar(x_axis, y_axis, color='red')

# Add text ancompetenttations to each bar
for i in range(len(x_axis)):
    plt.text(i , y_axis[i]+0.2, y_axis[i], ha='center', fontsize=15)


# Set the y-axis tick locations and labels
plt.yticks([10,20,30,40,50,60,70,80,90,100])

# Add labels and title
plt.xlabel('')
plt.ylabel('Values in Percentage %')
plt.title('Resource Persons  ', pad=30, fontsize= 20)

# Show the graph
plt.show()


