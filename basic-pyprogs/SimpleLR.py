#Importing the Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("E:/23MSIT059 SEM-2/MS224_APP_Python/Salary_Data.csv")
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

#Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0) #1/3 insted of 0.2

#Training the Simple Linear Regrssion model on the Training set
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train, y_train)

#Predicting the Test set results
y_pred = regression.predict(X_test)
print(y_pred)

#Visualizing the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regression.predict(X_train), color='blue')
plt.title('Salary vs Experience(Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

#Visualizing the Test set results
plt.scatter(X_test, y_test, color = "red")
plt.plot(X_test, regression.predict(X_test), color = 'blue')
plt.title('Salary vs Experience(Test set)')
plt.xlabel('Salary')
plt.show()

from sklearn.metrics import r2_score
# Calculate R-squared
r2 = r2_score(y_test, y_pred)
print(r2)