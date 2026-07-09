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

# .......................... Simple arithmetic ............................
# arr1 = np.array([10, 11, 12, 13, 14, 15])
# arr2 = np.array([20, 21, 22, 23, 24, 25])

# newarr = np.add(arr1, arr2)
# sub = np.subtract(arr1, arr2)
# multi = np.multiply(arr1, arr2)
# divid = np.divide(arr1, arr2)
# modulus = np.mod(arr1, arr2)
# remn = np.remainder(arr1, arr2)

# print("the addition of array are ", newarr)
# print("the Subtraction of array are ", sub)
# print("the multition of array are ", multi)
# print("the division of array are ", divid)
# print("the modulus of array are ", modulus)
# print("the Remaining of array are ", remn)

# Quotient and Mod
# arr1 = np.array([10, 20, 30, 40, 50, 60])
# arr2 = np.array([3, 7, 9, 8, 2, 33])

# quot = np.divmod(arr1, arr2)
# print("the Quotient of array are ", quot)

# Absolute Values
# arr = np.array([-1, -2, 1, 2, 3, -4])
# newarr = np.absolute(arr)

# print(newarr)

# ............................... #
# Rounding Decimals
# ............................... #
# Truncation
# Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.
# arr = np.trunc([-3.1666, 3.6667])
# print(arr)

# # ...... fix() ........
# arr = np.fix([-3.1666, 3.6667])
# print(arr)

# .... Rounding .....
# The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.
# arr = np.around(3.1666, 2) 
# print(arr)

# ......... Floor ......
# The floor() function rounds off decimal to nearest lower integer.
arr = np.floor([-3.1666, 3.6667])
print(arr)
