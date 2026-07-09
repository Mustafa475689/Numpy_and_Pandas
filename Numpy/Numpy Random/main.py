from numpy import random
# Random # 
# .........................................#
# Generate Randomnumbers ..................# Generate a random integer from 0 to 100:
# x = random.randint(100)
# print(x)

# Generate RAndom float ....................
# x = random.rand()
# print(x)
# The rand() method also allows you to specify the shape of the array.
# x = random.rand(5)
# print(x)
# # 2d random float array
# x = random.rand(3, 5)   
# print(x)

# Generate Random Array................ The randint() method takes a size parameter where you can specify the shape of an array.
# x=random.randint(100, size=(5))
# print(x)
# # 2d random array
# x = random.randint(100, size=(3, 5))
# print(x)

# Generate Random Number From Array ............
x = random.choice([3, 5, 7, 9])
print(x)

# 2d random array........ The choice() method also allows you to return an array of values....
# Add a size() parameter to specify the shape of the array.
x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)
