# Step 1: Import necessary Python libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# Step 2: Load the Ice cream dataset
file_path = "D:/sem(2)/Python PPT/Ice Cream Sales.csv"
ice_cream_data = pd.read_csv(file_path)

# Step 3: Split the dataset into training and test sets
X = ice_cream_data[['Temperature']]  # Features
Y = ice_cream_data['Ice Cream Profits']           # Target variable

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Step 5: Print the datasets to understand the split
print("X_train:\n", X_train)
print("X_test:\n", X_test)
print("Y_train:\n", Y_train)
print("Y_test:\n", Y_test)

# Step 6: Apply feature scaling using StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 7: Print scaled training and test sets
print("Scaled X_train:\n", X_train_scaled)
print("Scaled X_test:\n", X_test_scaled)

# Step 8: Implement Simple Linear Regression model
# Create and fit the model
model = LinearRegression()
model.fit(X_train_scaled, Y_train)

# Predict on test set
Y_pred = model.predict(X_test_scaled)

# Print the coefficients
print("Coefficients: ", model.coef_)
print("Intercept: ", model.intercept_)
