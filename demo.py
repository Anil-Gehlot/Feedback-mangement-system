import pandas as pd

# Load the Excel sheet into a Pandas DataFrame
data = pd.read_excel('feedbackdata.xlsx')
teacher = 43
mylist= list(data.columns)

list2 = []

for string in mylist:
    end = string.find('[')
    fin = string.find('(')
    csk = string[end+1:fin]
    list2.append(csk)

# print(list2)            # all column name
# print(len(list2))       # 189 all column


final =list2[3:teacher+3]
print(final)
# print(len(final))           #43
 
