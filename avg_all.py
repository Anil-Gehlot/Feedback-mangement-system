
import pandas as pd
import matplotlib.pyplot as plt
import re           # regex

# Load the Excel sheet into a Pandas DataFrame
df = pd.read_excel('feedbackdata.xlsx')

teacher = int(input('enter total no. of teacher : '))

#---------------------------------------------------------
# Extracting the teachers name : 
mylist= list(df.columns)
list2 = []
total_marks =[]

for string in mylist:
    end = string.find('[')
    fin = string.find('(')
    csk = string[end+1:fin]
    list2.append(csk)


final =list2[3:teacher+3]         # all teacher name.
# print(final)
#---------------------------------------------------------


avg_all=[]
for i in range(teacher):

    # Extract the column you want as a Python list
    # the iloc attribute is used to select all rows (:) and the first column (0) of the DataFrame, used to convert the selected column data to a Python list.
    column_data = df.iloc[:, 3+i].tolist()

    """the re.search() function is used to search each cell in the 'Column_Name' column for a pattern of one or more numeric characters (\d+). The group(0) method is used to extract the first (and only) matching group from the search result, which should be the numeric portion of the cell. The resulting list of numeric strings is then converted to float (or the appropriate data type) using a list comprehension.
    Note that this example assumes that each cell in the 'Column_Name' column contains at least one numeric character. If there are cells in the column that do not contain any numeric characters, the re.search() function will raise an exception. You can modify the regular expression pattern to handle different types of input data as needed."""
    column_data = [re.search(r'\d+', str(x)).group(0) for x in column_data]

    # Convert the resulting list to float (or the appropriate data type)
    column_data = [int(x) for x in column_data]
    # print(column_data)      # Print the resulting list
    total1 = sum(column_data)
    average1= sum(column_data)/len(column_data)
    # print(average1)         # average of communication of 1st column.


    #************for 2nd skill average***************#
    column_data = df.iloc[:, 3+i+teacher].tolist()
    column_data = [re.search(r'\d+', str(x)).group(0) for x in column_data]
    column_data = [int(x) for x in column_data]
    total2 = sum(column_data)
    average2= sum(column_data)/len(column_data)
    # print(average2)  

    #************for 3rd skill average***************#
    column_data = df.iloc[:, 3+i+teacher+teacher].tolist()
    column_data = [re.search(r'\d+', str(x)).group(0) for x in column_data]
    column_data = [int(x) for x in column_data]
    total3 = sum(column_data)
    average3= sum(column_data)/len(column_data)
    # print(average3) 

    #************for 4th skill average***************#
    column_data = df.iloc[:, 3+i+teacher+teacher+teacher].tolist()
    column_data = [re.search(r'\d+', str(x)).group(0) for x in column_data]
    column_data = [int(x) for x in column_data]
    total4 = sum(column_data)
    average4= sum(column_data)/len(column_data)
    # print(average4) 5

    average_rating = (average1+average2+average3+average4)/4
    float_num = "{:.2f}".format(average_rating)
    avg_all.append(float(float_num))

    total = total1+total2+total3+total4
    total_marks.append(total)

# print(total_marks)            # total marks of teacher.
# print(avg_all)                # average of all teachers.
#---------------------------------------------------------


# create the bar chart
fig, ax = plt.subplots()
ax.bar(final, avg_all)

# Add text annotations to each bar
for i in range(len(final)):
    plt.text(i, avg_all[i]+0.01, avg_all[i], ha='center', fontsize=7)

# Set the y-axis range to 2 to 5
plt.ylim([2, 5])
# Set the y-axis tick locations and labels
plt.yticks([2.0,2.2,2.4,2.6,2.8,3.0,3.2,3.4,3.6,3.8,4.0,4.2,4.4,4.6,4.8,5.0])

# set the tick labels for the x-axis
plt.xticks(rotation='vertical')

# Adjust the bottom margin of the subplot
fig.subplots_adjust(bottom=0.30)

# show the plot
plt.show()


#---------------------------------------------------------

# name of all teacher = final 
# total marks of all teachers = total_marks
# average rating of all teacher =  avg_all
