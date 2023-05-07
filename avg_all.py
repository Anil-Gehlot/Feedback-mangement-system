
import pandas as pd
import matplotlib.pyplot as plt
import re           # regex




teacher = int(input('enter total no. of teacher : '))
list1=[]
for i in range(teacher):

    # Load the Excel sheet into a Pandas DataFrame
    df = pd.read_excel('feedbackdata.xlsx')

    # Extract the column you want as a Python list
    # the iloc attribute is used to select all rows (:) and the first column (0) of the DataFrame, used to convert the selected column data to a Python list.
    column_data = df.iloc[:, 3+i].tolist()

    """the re.search() function is used to search each cell in the 'Column_Name' column for a pattern of one or more numeric characters (\d+). The group(0) method is used to extract the first (and only) matching group from the search result, which should be the numeric portion of the cell. The resulting list of numeric strings is then converted to float (or the appropriate data type) using a list comprehension.
    Note that this example assumes that each cell in the 'Column_Name' column contains at least one numeric character. If there are cells in the column that do not contain any numeric characters, the re.search() function will raise an exception. You can modify the regular expression pattern to handle different types of input data as needed."""
    column_data = [re.search(r'\d+', str(x)).group(0) for x in column_data]

    # Convert the resulting list to float (or the appropriate data type)
    column_data = [int(x) for x in column_data]
    # print(column_data)      # Print the resulting list

    average1= sum(column_data)/len(column_data)
    # print(average1)         # average of communication of 1st column.


    #************for 2nd skill average***************#
    column_data = df.iloc[:, 3+i+teacher].tolist()
    column_data = [re.search(r'\d+', str(x)).group(0) for x in column_data]
    column_data = [int(x) for x in column_data]
    average2= sum(column_data)/len(column_data)
    # print(average2)  

    #************for 3rd skill average***************#
    column_data = df.iloc[:, 3+i+teacher+teacher].tolist()
    column_data = [re.search(r'\d+', str(x)).group(0) for x in column_data]
    column_data = [int(x) for x in column_data]
    average3= sum(column_data)/len(column_data)
    # print(average3) 

    #************for 4th skill average***************#
    column_data = df.iloc[:, 3+i+teacher+teacher+teacher].tolist()
    column_data = [re.search(r'\d+', str(x)).group(0) for x in column_data]
    column_data = [int(x) for x in column_data]
    average4= sum(column_data)/len(column_data)
    # print(average4) 

    average_rating = (average1+average2+average3+average4)/4
    list1.append(average_rating)

# print(list1)
# print(len(list1))

# Create a bar graph of the data
plt.bar(range(len(list1)), list1)

# Set the x-axis tick labels
plt.xticks(range(len(list1)), [str(i+1) for i in range(len(list1))])

# Set the x-axis label
plt.xlabel('Resource Person Name')

# Set the y-axis label
plt.ylabel('Ratings')

# Show the plot
plt.show()