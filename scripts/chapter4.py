import math

v1  = [1, 2, 3, 4]
v2  = [4, 3, 2, 1]
v3  = [5, 6, 7, 8]
v4  = [2, 5, 8, 11]
v5  = [3, 4]
v6  = [4, 5]
v7  = [1, 1]
def compwise_operation(f, v1, v2):
    """ Performs the inputted function component wise. """
    return [f(i, j) for i,j in zip(v1, v2)]

# Vector Addition
# Method 1
def add(v1, v2):
    """ Adds two vectors. """
    return [i + j for i,j in zip(v1, v2)]

assert add(v1, v2) == [5, 5, 5, 5]

# Method 2
assert compwise_operation(lambda i,j: i + j, v1, v2) == [5, 5, 5, 5]


# Multi-Vector Addition
def addm(vectors):
    """ Adds multiple Vectors. """
    return [sum(vector[i] for vector in vectors) for i in range(len(vectors[0]))]

assert addm([v1, v2, v3]) == [10, 11, 12, 13]

# Vector Subtraction
# Method 1
def sub(v1, v2):
    """ Subtracts two Vectors. """
    return [i - j for i,j in zip(v1, v2)]

assert sub(v1, v2) == [-3, -1, 1, 3]

# Method 2
assert compwise_operation(lambda i,j: i - j, v1, v2) == [-3, -1, 1, 3]

# Multiply Vector by scalar
def mult_by_scalar(v, scalar):
    return [scalar * i for i in v]

assert mult_by_scalar(v1, 3) == [3, 6, 9, 12]

# Vector mean
def vector_mean(vectors):
    return mult_by_scalar(addm(vectors), 1/len(vectors))

assert vector_mean([v1, v2, v3, v4]) == [3, 4, 5, 6]

# Vector dot product
def dot_product(v1, v2):
    return sum(compwise_operation(lambda i,j: i * j, v1, v2))

assert dot_product(v1, v2) == 20

# Vector sum of squares
def sum_of_squares(v):
    return dot_product(v, v)

assert sum_of_squares(v1) == 30

# Magnitude
def magnitude(v):
    return math.sqrt(sum_of_squares(v))

assert magnitude(v5) == 5

# Distance
def distance(v1, v2):
    return magnitude(sub(v1, v2))

assert distance(v6, v7) == 5
