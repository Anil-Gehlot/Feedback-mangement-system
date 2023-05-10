
import pandas as pd
import matplotlib.pyplot as plt

teacher = 43


# Load the data from the Excel sheet
df = pd.read_excel('feedbackdata.xlsx')


# Select the specified column by name and load all values
column_data = df.iloc[:, 3+teacher+teacher+teacher+teacher+3].tolist()

# Print the column values
# print(column_data)

too_long = 0
just_all_right = 0
too_short = 0

for i in column_data:
    if i.lower()=='too long':
        too_long = too_long + 1
    if i.lower()=='just all right':
        just_all_right = just_all_right + 1
    if i.lower()== 'too short':
        too_short = too_short + 1
        
print(too_long)
print(just_all_right)
print(too_short)

total = too_long + just_all_right + too_short

too_long = (too_long*100)/total
just_all_right = (just_all_right*100)/total
too_short = (too_short*100)/total



x_axis = ['Too Long', 'Just All Right', 'Too Short']
y_axis=[too_long, just_all_right, too_short]

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
plt.title('Duration', pad=30, fontsize= 20)

# Show the graph
plt.show()


