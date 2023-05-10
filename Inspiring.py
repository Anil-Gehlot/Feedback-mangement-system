
import pandas as pd
import matplotlib.pyplot as plt

teacher = 43


# Load the data from the Excel sheet
df = pd.read_excel('feedbackdata.xlsx')


# Select the specified column by name and load all values
column_data = df.iloc[:, 3+teacher+teacher+teacher+teacher+5].tolist()

# Print the column values
# print(column_data)

to_a_great_extent = 0
to_some_extent = 0
not_at_all = 0

for i in column_data:
    if i.lower()=='to a great extent':
        to_a_great_extent = to_a_great_extent + 1
    if i.lower()=='to some extent':
        to_some_extent = to_some_extent + 1
    if i.lower()== 'not at all':
        not_at_all = not_at_all + 1
        
print(to_a_great_extent)
print(to_some_extent)
print(not_at_all)

total = to_a_great_extent + to_some_extent + not_at_all

to_a_great_extent = (to_a_great_extent*100)/total
to_some_extent = (to_some_extent*100)/total
not_at_all = (not_at_all*100)/total



x_axis = ['To A Great Extent', 'To Some Extent', 'Not At All']
y_axis=[to_a_great_extent, to_some_extent, not_at_all]

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
plt.title('Inspiring', pad=30, fontsize= 20)

# Show the graph
plt.show()


