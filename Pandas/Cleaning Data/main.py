import pandas as pd

# # Pandas - Cleaning Empty Cells
# # .................................... One way to deal with empty cells is to remove rows that contain empty cells.

# df = pd.read_csv('data.csv')
# new_df = df.dropna()

# print(new_df.to_string())

# # Remove all rows with NULL values:
# df = pd.read_csv('data.csv')
# df.dropna(inplace = True)

# print(df.to_string())

# # Replace NULL values in the "Age" columns with the Age 30:
# df = pd.read_csv('data.csv')

# df.fillna({
#     "Age": 30,
#     "Name": "Muskan",
#     "City": "Hyderabad"
#  }, inplace=True)
# print(df.to_string())

# ..........................................
# Replace Using Mean, Median, or Mode .... 
# ..........................................
# Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:

# # Calculate the MEAN, and replace any empty values with it: ......
# df = pd.read_csv('data.csv')
# x = df["Age"].mean()
# df.fillna({"Age": x}, inplace=True)

# print(df.to_string())

# # Calculate the MEDIAN, and replace any empty values with it: ..... Median = the value in the middle, after you have sorted all values ascending.
# df = pd.read_csv('data.csv')
# x = df["Age"].median()
# df.fillna({"Age": x}, inplace=True)

# print(df.to_string())

# Calculate the MODE, and replace any empty values with it: .... Mode = the value that appears most frequently.
df = pd.read_csv('data.csv')
x = df["Age"].mode()[0]
df.fillna({"Age": x}, inplace=True)

print(df.to_string())