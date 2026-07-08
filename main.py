# import pandas
import numpy as np
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }



# arr = np.array([1, 2, 3, 4, 5])

# print(arr)
# print(type(arr))

# tuple = np.array((2,4,6,8))
# print(tuple)

# 2d array
# td = np.array([[1,3,5,7],[2,4,6,8]])
# print(td)

# 3d array
# trd = np.array([[[1,3,5,7],[2,4,6,8]],[[1,2,3,4],[5,6,7,8]]])
# # use ndim to know the dimension of array
# print(trd)
# print(trd.ndim)

# here we can make more than 3 dimansions array
# arr = np.array([1, 2, 3, 4], ndmin=5)

# print(arr)
# print('number of dimensions :', arr.ndim)

# Array indexing
# arr = np.array([1, 2, 3, 4])
# print(arr[1])
# print(arr[1] + arr[3])

# 2d and 3d array indeing
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[1, 3])
print(arr[1, 3] - arr[0, 4])
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) # 3d 
print(arr[1, 0, 2])
