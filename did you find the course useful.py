
import pandas as pd
import matplotlib.pyplot as plt

teacher = 43


# Load the data from the Excel sheet
df = pd.read_excel('feedbackdata.xlsx')


# Select the specified column by name and load all values
column_data = df.iloc[:, 3+teacher+teacher+teacher+teacher].tolist()

# Print the column values
# print(column_data)

yes = 0
no = 0
some_extent = 0

for i in column_data:
    if i.lower()=='yes':
        yes = yes + 1
    if i.lower()=='no':
        no = no + 1
    if i.lower()== 'some extent':
        some_extent = some_extent + 1

total = yes + no + some_extent

yes = (yes*100)/total
no = (no*100)/total
some_extent = (some_extent*100)/total


"""
# for two points of decimal only.
final_yes =float("{:.2f}".format(yes))
final_no = float("{:.2f}".format(no))
final_some_extent = float("{:.2f}".format(some_extent))
"""


x_axis = ['Yes', 'No', 'Some Extent']
# y_axis = [final_yes, final_no, final_some_extent]     # for two points of decimal only.
y_axis=[yes, no, some_extent]

# to plot bar graph
plt.bar(x_axis, y_axis, color='red')

# Add text annotations to each bar
for i in range(len(x_axis)):
    plt.text(i , y_axis[i]+0.2, y_axis[i], ha='center', fontsize=15)


# Set the y-axis tick locations and labels
plt.yticks([10,20,30,40,50,60,70,80,90,100])

# Add labels and title
plt.xlabel('')
plt.ylabel('Values in Percentage %')
plt.title('Did you find the course useful ? ', pad=30, fontsize= 20)

# Show the graph
plt.show()


