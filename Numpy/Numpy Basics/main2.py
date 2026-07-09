import numpy as np

# Copy and view
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# v = arr.view()
# v[1] = 6 # make changes in the view
# arr[0] = 42

# print(arr)
# print(x)
# print(v)

# # Check if array owns its data
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# v = arr.view()
# print(x.base)
# print(v.base)

# ..........................
# Array shapes
# ..............................
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# print(arr.shape)
# The example above returns (2, 4), 
# which means that the array has 2 dimensions, where the first dimension has 2 elements and the second has 4.

# arr = np.array([1,2,3,4,5], ndmin=5)
# print(arr)
# print('shape of array :', arr.shape)

# ............................................
# Array Reshape
# ............................................
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# # newarr = arr.reshape(4, 3) # reshape in 2d
# # print(newarr)
# # print(newarr.ndim)
# newarry = arr.reshape(2, 3, 2)
# print(newarry)

# Check if the returned array is a copy or a view:
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# print(arr.reshape(2, 4).base)

# Unknown Dimension
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newarr = arr.reshape(2, 2, -1)
# print(newarr)

# Convert the array into a 1D array:
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# newarr = arr.reshape(-1)
# print(newarr)

# Iterating Arrays..............
# arr = np.array([1, 2, 3])

# for x in arr:
#   print(x)
# 2d
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# for x in arr:
#   print(x)
# 3d
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# for x in arr:
#   print(x)

# itreating array in different data types
# arr = np.array([1, 2, 3])

# for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
#   print(x)

# ...................................
# Iterating With Different Step Size
# .........................................
# Iterate through every scalar element of the 2D array skipping 1 element:
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# for x in np.nditer(arr[:, ::2]):
#     print(x)

# Enumerated Iteration Using ndenumerate()......................
# arr = np.array([1, 2, 3])
# for idx, x in np.ndenumerate(arr):
#     print(idx, x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]]) #2d
for idx, x in np.ndenumerate(arr):
    print(idx, x)
