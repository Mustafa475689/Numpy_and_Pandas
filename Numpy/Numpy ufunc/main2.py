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
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr, n=2)
print(newarr)
