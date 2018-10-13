#Name: Kedar Kale
#Roll No: SCETTYMI54
#Assignment - 1
#Data Processing and cleaning of dataset using Python


import pandas as pd

data =  pd.read_csv("student.csv")      	#Command to read the .csv (Comma Separated Values) file

print (data.head())				#Print the first 5 rows from the .csv file

#    roll       name  marks  age
# 0     1      Tejas  32.44   20
# 1     2     Sanket  47.21   20
# 2     3      Atish  94.65   19
# 3     4      Kedar  44.26   21
# 4     5  Rushikesh  59.21   19

print (data.tail())				#Print the last 5 rows from the .csv file

#    roll     name   marks  age
# 5     6   Pratik  100.00   20
# 6     7  Sankeit   85.00   20
# 7     8  Shubham   99.99   20
# 8     9  Saurabh   85.21   19
# 9    10   Suprit   64.21   21


print (data.head(1))				#Prints only the first row

#    roll   name  marks  age
# 0     1  Tejas  32.44   20

			
print (data.tail(1))				#Prints only the last row

#    roll    name  marks  age
# 9    10  Suprit  64.21   21


print (data.shape)				#Prints the number of rows and columns in the .csv file

# (10, 4)


print (data.loc[:,["name", "age", "marks"]])	#Prints all rows of only the specified columns

#         name  age   marks
# 0      Tejas   20   32.44
# 1     Sanket   20   47.21
# 2      Atish   19   94.65
# 3      Kedar   21   44.26
# 4  Rushikesh   19   59.21
# 5     Pratik   20  100.00
# 6    Sankeit   20   85.00
# 7    Shubham   20   99.99
# 8    Saurabh   19   85.21
# 9     Suprit   21   64.21


print (data.iloc[0:4,0:2]) 			#Prints first 4 rows of only the first two columns

#    roll    name
# 0     1   Tejas
# 1     2  Sanket
# 2     3   Atish
# 3     4   Kedar


print (data.iloc[0:4,:])			#Prints all columns of first 4 rows

#    roll    name  marks  age
# 0     1   Tejas  32.44   20
# 1     2  Sanket  47.21   20
# 2     3   Atish  94.65   19
# 3     4   Kedar  44.26   21


print (data.iloc[4:5,:])			#Prints all columns of only the 4th row

#    roll       name  marks  age
# 4     5  Rushikesh  59.21   19


print (data["marks"].mean())			#Prints the mean of all marks

# 71.218


print (data.corr())				#Prints correlation of all the columns of numeric data type

#            roll     marks       age
# roll   1.000000  0.545990  0.124341
# marks  0.545990  1.000000 -0.358761
# age    0.124341 -0.358761  1.000000


print (data.std())				#Prints the standard deviation of all columns of numeric data type

# roll      3.027650
# marks    24.924698
# age       0.737865


print (data.median())				#Prints the median of all columns of numeric data type

# roll      5.500
# marks    74.605
# age      20.000


print (data.count())				#Prints the count of each columns

# roll     10
# name     10
# marks    10
# age      10


print (data.max())				#Prints the maximum values from each columns

# roll        10
# name     Tejas
# marks      100
# age         21


print (data.min())				#Prints the minimum values from each columns

# roll         1
# name     Atish
# marks    32.44
# age         19


print (data[data["marks"]>=60])			#Only prints rows where marks is greater than or equal to 60

#    roll     name   marks  age
# 2     3    Atish   94.65   19
# 5     6   Pratik  100.00   20
# 6     7  Sankeit   85.00   20
# 7     8  Shubham   99.99   20
# 8     9  Saurabh   85.21   19
# 9    10   Suprit   64.21   21


print (data[data["age"]>=20])			#Only prints rows where age is greater than or equal to 20

#    roll     name   marks  age
# 0     1    Tejas   32.44   20
# 1     2   Sanket   47.21   20
# 3     4    Kedar   44.26   21
# 5     6   Pratik  100.00   20
# 6     7  Sankeit   85.00   20
# 7     8  Shubham   99.99   20



