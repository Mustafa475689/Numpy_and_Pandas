
import numpy as np

# .............................. #
# NumPy Trigonometric Functions
# .............................. #
# x = np.sin(np.pi/2)
# print(x)

# # Find sine values for all of the values in arr:
# arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
# x = np.sin(arr)
# print(x)

# # Convert Degrees Into Radians
# arr = np.array([90, 180, 270, 360])
# x = np.deg2rad(arr)
# print(x)

# # Radians to Degrees
# arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
# x = np.rad2deg(arr)
# print(x)

# .. Finding Angles
# Finding angles from values of sine, cos, tan. E.g. sin, cos and tan inverse (arcsin, arccos, arctan).
# NumPy provides ufuncs arcsin(), arccos() and arctan() that produce radian values for corresponding sin, cos and tan values given.
# x = np.arcsin(1.0)
# print(x)

# # Angles of Each Value in Arrays
# arr = np.array([1, -1, 0.1])
# x = np.arcsin(arr)
# print(x)

# # Hypotenues
# # Finding hypotenues using pythagoras theorem in NumPy.
# base = 3
# perp = 4
# x = np.hypot(base, perp)
# print(x)

# .............................. #
# NumPy Hyperbolic Functions
# .............................. #
# # Hyperbolic Functions
# # NumPy provides the ufuncs sinh(), cosh() and tanh() that take values in radians and produce the corresponding sinh, cosh and tanh values..
# x = np.sinh(np.pi/2)
# print(x)

# # Find cosh values for all of the values in arr:
# arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
# x = np.cosh(arr)
# print(x)

# # Finding Angles ..............
# # Numpy provides ufuncs arcsinh(), arccosh() and arctanh() that produce radian values for corresponding sinh, cosh and tanh values given.
# x = np.arcsinh(1.0)
# print(x)

# # Angles of Each Value in Arrays
# arr = np.array([0.1, 0.2, 0.5])
# x = np.arctanh(arr)
# print(x)

# .............................. #
# NumPy Set Operations
# .............................. #
# Create Sets in NumPy.... We can use NumPy's unique() method to find unique elements from any array
# arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
# x = np.unique(arr)
# print(x)

# # Finding Union ... To find the unique values of two arrays, use the union1d() method.
# arr1 = np.array([1, 2, 3, 4])
# arr2 = np.array([3, 4, 5, 6])

# newarr = np.union1d(arr1, arr2)

# print(newarr)

# # Finding Intersection ... To find only the values that are present in both arrays, use the intersect1d() method.
# arr1 = np.array([1, 2, 3, 4])
# arr2 = np.array([3, 4, 5, 6])

# newarr = np.intersect1d(arr1, arr2, assume_unique=True)

# print(newarr)

# # Finding Difference ... To find only the values in the first set that is NOT present in the seconds set, use the setdiff1d() method.
# set1 = np.array([1, 2, 3, 4])
# set2 = np.array([3, 4, 5, 6])

# newarr = np.setdiff1d(set1, set2, assume_unique=True)

# print(newarr)

# Finding Symmetric Difference ... To find only the values that are NOT present in BOTH sets, use the setxor1d() method.
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr = np.setxor1d(set1, set2, assume_unique=True)

print(newarr) 
