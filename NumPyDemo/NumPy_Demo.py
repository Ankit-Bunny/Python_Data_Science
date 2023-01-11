import numpy as np
from numpy.random import randint

my_list = [1, 2, 3]
arr1 = np.array(my_list)
print(arr1)

my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr2 = np.array(my_mat)
print(arr2)

arr3 = np.arange(0, 11, 2)
print(arr3)

print(np.zeros(3))
print(np.zeros((2, 5)))
print(np.ones(3))
print(np.ones((2, 5)))

print(np.linspace(0, 5, 6))

print(np.eye(3))

print(np.random.rand(3))
print(np.random.rand(2, 3))
print(np.random.randn(3))
print(np.random.randn(2, 3))

print(np.random.randint(1, 10, 3))

arr = np.arange(25)
random_array = np.random.randint(0, 50, 5)
print(arr)
print(arr.reshape(5, 5))
print(random_array)
print(random_array.max())
print(random_array.min())
print(random_array.argmax())
print(random_array.argmin())

print(arr.shape)

print(arr.dtype)
