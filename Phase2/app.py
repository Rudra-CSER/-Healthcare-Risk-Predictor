import pandas as pd

titanic_data = pd.read_csv("Titanic-Dataset.csv")

# print(titanic_data.head())

# print(titanic_data.describe())
# # This will give us a statistical summary of the numerical columns in the dataset.
# print(titanic_data.info())

# Select 2 coloumns and filter 6 rows
print(titanic_data[["Name", "Age" , "Ticket"]].head(8))