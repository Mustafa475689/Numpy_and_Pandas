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

# # Calculate the MODE, and replace any empty values with it: .... Mode = the value that appears most frequently.
# df = pd.read_csv('data.csv')
# x = df["Age"].mode()[0]
# df.fillna({"Age": x}, inplace=True)

# print(df.to_string())

# ..........................................
# Cleaning Data of Wrong Format
# ..........................................

# # Let's try to convert all cells in the 'Date' column into dates. ..
# # Pandas has a to_datetime() method for this:
# df = pd.read_csv('data1.csv')
# df['Date'] = pd.to_datetime(df['Date'], format='mixed')
# print(df.to_string())

# # Removing Rows ...
# df.dropna(subset=['Date'], inplace = True)
# print(df.to_string())

# .................................................
# Fixing Wrong Data
# .................................................

# # Replacing Values .. In our example, it is most likely a typo, and the value should be "45" instead of "450", and we could just insert "45" in row 7:
# df = pd.read_csv('data1.csv')
# df.loc[7, 'Duration'] = 45
# print(df.to_string)

# # To replace wrong data for larger data sets you can create some rules, 
# # e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.
# df = pd.read_csv('data1.csv')
# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.loc[x, "Duration"] = 120
#   print(df.to_string())
