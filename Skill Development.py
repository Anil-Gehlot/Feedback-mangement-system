
import pandas as pd
import matplotlib.pyplot as plt

teacher = 43


# Load the data from the Excel sheet
df = pd.read_excel('feedbackdata.xlsx')


# Select the specified column by name and load all values
column_data = df.iloc[:, 3+teacher+teacher+teacher+teacher+6].tolist()

# Print the column values
# print(column_data)

adequate = 0
no_so_adequate = 0
not_at_all_adequate = 0

for i in column_data:
    if i.lower()=='adequate':
        adequate = adequate + 1
    if i.lower()=='no so adequate':
        no_so_adequate = no_so_adequate + 1
    if i.lower()== 'not at all adequate':
        not_at_all_adequate = not_at_all_adequate + 1
        
print(adequate)
print(no_so_adequate)
print(not_at_all_adequate)

total = adequate + no_so_adequate + not_at_all_adequate

adequate = (adequate*100)/total
not_so_adequate = (no_so_adequate*100)/total
not_at_all_adequate = (not_at_all_adequate*100)/total



x_axis = ['Adequate', 'No So Adequate', 'Not At All Adequate']
y_axis=[adequate, not_so_adequate, not_at_all_adequate]

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
plt.title('Skill Development', pad=30, fontsize= 20)

# Show the graph
plt.show()


