# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)   #reader method inputs the file and reads and outputs data in the file
#     print(data) # creates an object data that has all the data in the csv file
#     temperatures = []
#     for row in data:
#         if row [1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)


# import pandas

# data = pandas.read_csv("weather_data.csv")       #this way, we can use read_csv method to input the csv file instead of performing an open operation to open the file
# print(data)         # with pandas, it prints the table in a much more cleaner way

# to get hold of a single column, we can use:
# print(data["temp"])  #calling the column name 

#pandas have 2 datastructures : Series and DataFrame. DataFrame is like the whole table in csv file, Series is like a column of the table

# reading the pandas documentation would help effectively as you can figure out what is available in the library itself.

# to create a dataframe from scratch, we create a dictionary of the values of the dataframe you want to create, say the dictionary is "students": pandas.DataFrame(students), can also convert this dataframe into a csv file using data.to_csv("new_file.csv") and it converts it into csv file
