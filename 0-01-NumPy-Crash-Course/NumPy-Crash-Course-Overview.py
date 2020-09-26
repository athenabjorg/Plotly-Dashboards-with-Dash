############################
### Numpy Crash Course #####
############################
import numpy as np

my_list = [0,1,2,3,4]

arr = np.array(my_list)

print(arr)
# [0 1 2 3 4]

# arange integers, takes in start,stop, and step size

a = np.arange(0,10)
print(a)
# [0 1 2 3 4 5 6 7 8 9]

a= np.arange(0,10,2)
print(a)
# [0 2 4 6 8]

# Create an array of zeros

a = np.zeros((5,5))
print(a)
# [[0. 0. 0. 0. 0.]
 # [0. 0. 0. 0. 0.]
 # [0. 0. 0. 0. 0.]
 # [0. 0. 0. 0. 0.]
 # [0. 0. 0. 0. 0.]]

# Create an array of ones

a = np.ones((2,4))
print(a)
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

# Create an array of random integers (uniform distribution between limits)

a = np.random.randint(0,10)
print(a)
# 4

# Create 2d matrix of random ints

a = np.random.randint(0,10,(3,3))
print(a)
# [[8 7 5]
#  [5 8 1]
#  [3 6 9]]

# Create linearly spaced array
a = np.linspace(0,10,6)
print(a)
# [ 0.  2.  4.  6.  8. 10.]


a = np.linspace(0,10,101)
print(a)
# [ 0.   0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1.   1.1  1.2  1.3
#   1.4  1.5  1.6  1.7  1.8  1.9  2.   2.1  2.2  2.3  2.4  2.5  2.6  2.7
#   2.8  2.9  3.   3.1  3.2  3.3  3.4  3.5  3.6  3.7  3.8  3.9  4.   4.1
#   4.2  4.3  4.4  4.5  4.6  4.7  4.8  4.9  5.   5.1  5.2  5.3  5.4  5.5
#   5.6  5.7  5.8  5.9  6.   6.1  6.2  6.3  6.4  6.5  6.6  6.7  6.8  6.9
#   7.   7.1  7.2  7.3  7.4  7.5  7.6  7.7  7.8  7.9  8.   8.1  8.2  8.3
#   8.4  8.5  8.6  8.7  8.8  8.9  9.   9.1  9.2  9.3  9.4  9.5  9.6  9.7
#   9.8  9.9 10. ]


################################
#### Numpy Operations #########
##############################

# Setting a seed allows you to get the same "random" numbers that we do
# This is really nice for testing, so you can compare results
np.random.seed(101) # watch video for details
arr = np.random.randint(0,100,10)
print(arr)
# [95 11 81 70 63 87 75  9 77 40]

# If you call this again, you will get a different set of random integers than
# the first time you called it. But both sets will be the same to someone else's
# who also ran these 2 calls immediately after setting the same seed.
arr2 = np.random.randint(0,100,10)
print(arr2)
# [ 4 63 40 60 92 64  5 12 93 40]


# Simple operations

print(arr.max())
# 95

print(arr.min())
# 9

print(arr.mean())
# 60.8

# Index location of min
print(arr.argmin())
# 7

print(arr.argmax())
# 0

print(arr.reshape(2,5))
# [[95 11 81 70 63]
#  [87 75  9 77 40]]

###########################
#### Indexing ############
#########################

# You can use .reshape() to change the shape of a 1d array to a 2d,3d, etc.. array
# Keep in mind, we will mainly be working with 2d tabular data.
mat = np.arange(0,100).reshape(10,10)
print(mat)
# [[ 0  1  2  3  4  5  6  7  8  9]
#  [10 11 12 13 14 15 16 17 18 19]
#  [20 21 22 23 24 25 26 27 28 29]
#  [30 31 32 33 34 35 36 37 38 39]
#  [40 41 42 43 44 45 46 47 48 49]
#  [50 51 52 53 54 55 56 57 58 59]
#  [60 61 62 63 64 65 66 67 68 69]
#  [70 71 72 73 74 75 76 77 78 79]
#  [80 81 82 83 84 85 86 87 88 89]
#  [90 91 92 93 94 95 96 97 98 99]]

row = 0
col = 1

# Selecting an individual number:
print(mat[row,col])
# 1

# Select an entire column (all row entries of this column "col")
print(mat[:,col])
# [ 1 11 21 31 41 51 61 71 81 91]

# Select an entire column (all row entries of this column "col")
print(mat[row,:])
# [0 1 2 3 4 5 6 7 8 9]


#######################
##### Masking #########
#######################
# Masking allows you to use conditional filters to grab elements
# we'll see this idea used in pandas.

print(mat > 50)
# [[False False False False False False False False False False]
#  [False False False False False False False False False False]
#  [False False False False False False False False False False]
#  [False False False False False False False False False False]
#  [False False False False False False False False False False]
#  [False  True  True  True  True  True  True  True  True  True]
#  [ True  True  True  True  True  True  True  True  True  True]
#  [ True  True  True  True  True  True  True  True  True  True]
#  [ True  True  True  True  True  True  True  True  True  True]
#  [ True  True  True  True  True  True  True  True  True  True]]

print(mat[mat>50])
# [51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74
#  75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98
#  99]

# That is all for NumPy! NumPy is a really large library that does a lot
# more than what we showed here. But for our use cases in visualization, these
# are the basics we need to know for now. Later on we may introduce other
# NumPy concepts.
