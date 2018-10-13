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

plt.scatter(X_train,y_train, color = 'red')
plt.plot(X_train,regressor.predict(X_train), color = 'Blue')
plt.title('Salary vs Experience (Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

plt.scatter(X_test,y_test, color = 'red')
plt.plot(X_test,regressor.predict(X_test), color = 'Blue')
plt.title('Salary vs Experience (Testing Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

