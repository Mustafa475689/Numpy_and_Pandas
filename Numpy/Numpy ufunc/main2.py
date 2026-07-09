import numpy as np

# ......................... #
# NumPy Products
# ......................... #
# arr = np.array([1, 2, 3, 4])
# x = np.prod(arr)
# print(x)

# Find the product of the elements of two arrays ......
# arr1 = np.array([1, 2, 3, 4])
# arr2 = np.array([5, 6, 7, 8])

# x = np.prod([arr1, arr2])
# print(x)

# Product Over an Axis .........
# arr1 = np.array([1, 2, 3, 4])
# arr2 = np.array([5, 6, 7, 8])

# newarr = np.prod([arr1, arr2], axis=1)
# print(newarr)

# Cummulative Product
# arr = np.array([5, 6, 7, 8])

# newarr = np.cumprod(arr)
# print(newarr)

# ......................... #
# NumPy Differences
# ......................... #
# Differences ..... A discrete difference means subtracting two successive elements.
# E.g. for [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]........ use the diff() function.

# arr = np.array([10, 15, 25, 5])
# newarr = np.diff(arr)
# print(newarr)

# Compute discrete difference of the following array twice: ..... We can perform this operation repeatedly by giving parameter n.
# arr = np.array([10, 15, 25, 5])
# newarr = np.diff(arr, n=2)
# print(newarr)

# .................................. #
#  NumPy LCM Lowest Common Multiple
# .................................. #
# Finding LCM

# num1 = 4
# num2 = 6
# x = np.lcm(num1, num2)
# print(x)

# Finding LCM in Arrays ... To find the Lowest Common Multiple of all values in an array, you can use the reduce() method.
# The reduce() method will use the ufunc, in this case the lcm() function, on each element, and reduce the array by one dimension.

# arr = np.array([3, 6, 9])
# x = np.lcm.reduce(arr)
# print(x)

# # Find the LCM of all values of an array where the array contains all integers from 1 to 10:

# arr = np.arange(1, 11)
# x = np.lcm.reduce(arr)
# print(x)
