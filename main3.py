import numpy as np

# ..........................
# Array Join 
# ...........................
# join two array
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.concatenate((arr1, arr2)) # we use concatenate to join two array
# print(arr)

# 2d array join
# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
# arr = np.concatenate((arr1, arr2), axis=1)
# print(arr)

# Joining Arrays Using Stack Functions
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.stack((arr1, arr2), axis=1)
# print(arr)

# Stacking along rows
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.hstack((arr1, arr2))
# print(arr)

# Stacking along column
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.vstack((arr1, arr2))
# print(arr)

#  Stacking along depth/height
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.dstack((arr1, arr2))
# print(arr)

# ..........................
# Splitting NumPy Arrays
# ..........................
# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 3)
# print(newarr)

# newarre = np.array_split(arr, 4)
# print(newarre)

# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 3)
# print(newarr[0])
# print(newarr[1])
# print(newarr[2])

# Split 2d array..
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)
