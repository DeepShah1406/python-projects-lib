#Importing the Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
import missingno as mi
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("Z:/My Drive/23MSIT059/Sem-2/MS224 APP Python/Practicals/titanic_dataset.csv")
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
df.isnull().any()

df.isnull()
#if there is data is missing, it will display True else False.

vc = df["Embarked"].value_counts() 
print(vc)
mean_data = df["Age"].mean()
print("Mean:", mean_data) 

min_data=df["Age"].min() 
max_data=df["Age"].max()
print("Minimum:",min_data, "\nMaximum:", max_data)

# Handling missing values
# Replace missing values in 'Age' column with the median age
imputer = SimpleImputer(strategy='median')
df['Age'] = imputer.fit_transform(df[['Age']])

print(df["Age"])


# Display the first few rows of the dataframe
print("Before preprocessing:")
print(df.head())

# Handling missing values
# Replace missing values in 'Age' column with the median age
imputer = SimpleImputer(strategy='median')
df['Age'] = imputer.fit_transform(df[['Age']])

# Replace missing values in 'Cabin' column with a placeholder value
df['Cabin'].fillna('Unknown', inplace=True)

# Replace missing values in 'Embarked' column with the most common value
most_common_embarked = df['Embarked'].mode()[0]
df['Embarked'].fillna(most_common_embarked, inplace=True)

# Handling categorical variables
# Encode 'Sex' column (male/female) into numerical values
label_encoder = LabelEncoder()
df['Sex'] = label_encoder.fit_transform(df['Sex'])

# Encode 'Embarked' column (C/Q/S) into numerical values
df['Embarked'] = label_encoder.fit_transform(df['Embarked'])

# Display the first few rows of the preprocessed dataframe
print("\nAfter preprocessing:")
print(df.head(10))

# specific_data=df[["Survived","Pclass","Name","Sex","Age","SibSp","Parch","Ticket","Fare", "Cabin","Embarked"]] 
# #data[["column_name1","column_name2","column_name3"]] 
  
# #now we will print the first 10 columns of the specific_data dataframe. 
# print(specific_data.head(10))