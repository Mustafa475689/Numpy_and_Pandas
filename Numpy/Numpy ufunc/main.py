import numpy as np

# Create Your Own ufunc
# def myadd(x, y):
#   return x+y
# myadd = np.frompyfunc(myadd, 2, 1)
# print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

# print(type(np.add))

# ...... Check if add() function is ufunc or not
# if type(np.add) == np.ufunc:
#   print('add is ufunc')
# else:
#   print('add is not ufunc')

# Simple arithmetic
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2)
sub = np.subtract(arr1, arr2)
print(newarr)
print(sub)
