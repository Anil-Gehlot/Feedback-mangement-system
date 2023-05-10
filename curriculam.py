import pandas as pd
import matplotlib.pyplot as plt

teacher = 43


# Load the data from the Excel sheet
df = pd.read_excel('feedbackdata.xlsx')


# Select the specified column by name and load all values
column_data = df.iloc[:, 3+teacher+teacher+teacher+teacher+10].tolist()

# Print the column values
# print(column_data)

sufficient = 0
notsufficient = 0
notatall_sufficient = 0

for i in column_data:
    if i.lower()=='sufficient':
        sufficient = sufficient + 1
    if i.lower()=='not sufficient':
        notsufficient = notsufficient + 1
    if i.lower()== 'not at all sufficient':
        notatall_sufficient = notatall_sufficient + 1

print(sufficient)
print(notsufficient)
print(notatall_sufficient)

total = (sufficient + notsufficient + notatall_sufficient)

sufficient = (sufficient*100)/total

notsufficient = (notsufficient*100)/total

notatall_sufficient = (notatall_sufficient*100)/total



x_axis = ['sufficient', 'Very sufficient', 'Poor']
y_axis=[sufficient, notsufficient, notatall_sufficient]

# to plot bar graph
plt.bar(x_axis, y_axis, color='red')

# Add text anverysufficienttations to each bar
for i in range(len(x_axis)):
    plt.text(i , y_axis[i]+0.2, y_axis[i], ha='center', fontsize=15)


# Set the y-axis tick locations and labels
plt.yticks([10,20,30,40,50,60,70,80,90,100])

# Add labels and title
plt.xlabel('')
plt.ylabel('Values in Percentage %')
plt.title('Curriculum of the Course ', pad=30, fontsize= 20)

# Show the graph
plt.show()