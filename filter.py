# NumPy Filter Array
# ..........................
import numpy as np

# arr = np.array([41, 42, 43, 44])
# x = [True, False, True, False]
# newarr = arr[x]
# print(newarr)

# .... Creating the Filter Array ............
arr = np.array([1, 3, 4 ,6, 8])
filter_arr = []

for element in arr:
    if element > 5:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

