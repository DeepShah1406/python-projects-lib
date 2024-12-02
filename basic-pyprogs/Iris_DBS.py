#Importing the Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import io

from sklearn.discriminant_analysis import StandardScaler

iris_df = pd.read_csv("E:/23MSIT059 SEM-2/MS224_APP_Python/Iris.csv")
iris_df.info()

# Display the first few rows of the dataset
print("Original dataset:")
print(iris_df.head())

# Separate features and target variable
X = iris_df.drop('Species', axis=1) 
y = iris_df['Species']

# Initialize the StandardScaler
scaler = StandardScaler()

# Fit and transform the features
X_scaled = scaler.fit_transform(X)

# Convert the scaled features back to a DataFrame
X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns)

# Display the first few rows of the scaled features
print("\nScaled features:")
print(X_scaled_df.head(10))

"""specific_data=iris_df[["Id","SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm","SibSp","Species"]] 
#data[["column_name1","column_name2","column_name3"]] 
  
#now we will print the first 10 columns of the specific_data dataframe. 
print(specific_data.X_scaled_df.head(10))"""