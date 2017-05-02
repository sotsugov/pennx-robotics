import math
import numpy as np


# Find vectors orthogonal to [-1, 2]
v = [-1, 2]
w_n = [
    [1, 2],
    [10, 5],
    [2/math.sqrt(5), 1/math.sqrt(5)],
    [2/math.sqrt(5), -(1/math.sqrt(5))]]
# print[np.dot(v, w) for w in w_n]


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# print np.dot(a, b)


x = np.array([1, 3, 2])
y = np.array([3, -1, 0])
z = np.array([1, 3, -5])
# print (x + y) + z == x + (y + z)
# print np.dot(z, x)


x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print x*x+2*x*y+y*y
# print np.dot(x+y, x+y)

