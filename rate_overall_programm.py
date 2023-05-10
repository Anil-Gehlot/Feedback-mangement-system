import pandas as pd
import matplotlib.pyplot as plt

teacher = 43


# Load the data from the Excel sheet
df = pd.read_excel('feedbackdata.xlsx')


# Select the specified column by name and load all values
column_data = df.iloc[:, 3+teacher+teacher+teacher+teacher+11].tolist()

# Print the column values
# print(column_data)

verygood = 0
good = 0
poor = 0

for i in column_data:
    if i.lower()=='good':
        good = good + 1
    if i.lower()=='very good':
        verygood = verygood + 1
    if i.lower()== 'poor':
        poor = poor + 1

print(good)
print(verygood)
print(poor)

total = (good + verygood + poor)

good = (good*100)/total

verygood = (verygood*100)/total

poor = (poor*100)/total



x_axis = ['Good', 'Very Good', 'Poor']
y_axis=[good, verygood, poor]

# to plot bar graph
plt.bar(x_axis, y_axis, color='red')

# Add text anverygoodtations to each bar
for i in range(len(x_axis)):
    plt.text(i , y_axis[i]+0.2, y_axis[i], ha='center', fontsize=15)


# Set the y-axis tick locations and labels
plt.yticks([10,20,30,40,50,60,70,80,90,100])

# Add labels and title
plt.xlabel('')
plt.ylabel('Values in Percentage %')
plt.title('How would you rate the overall programme ', pad=30, fontsize= 20)

# Show the graph
plt.show()