#Name: Kedar Kale
#Roll No: SCETTYMI54
#Assignment - 2
#Linear Regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression


ds = pd.read_csv("salary.csv")
X = ds.iloc[:,:-1].values
y = ds.iloc[:,1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3.0, random_state = 0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)
X_test = input("Enter your years of experience: ")
y_pred = regressor.predict(X_test)
print "Your predicted salary is ",y_pred[0]

#Output:
#
#Enter your years of experience: 10
#Your predicted salary is  120277.90805109226
#
#Enter your years of experience: 5
#Your predicted salary is  73548.29889445825
#
#Enter your years of experience: 20
#Your predicted salary is  213737.12636436033

