import numpy as np

arr = np.arange(0, 11)
print(arr)
print(arr[3])
print(arr[1:5])
arr[1:3] = 51
print(arr)
arr = np.arange(0, 11)
slice_of_arr = arr[0:5]
print(slice_of_arr)
slice_of_arr[:] = 31
print(slice_of_arr)
print(arr)
arr_copy = arr.copy()
arr_copy[:] = 51
print(arr)
print(arr_copy)

arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print(arr_2d)
print(arr_2d[1][1])
print(arr_2d[1, 1])
print(arr_2d[:2, :2])

arr = np.arange(0, 11)
boolean_array = arr > 5
print(boolean_array)
print(arr[boolean_array])
print(arr[arr > 5])
print(arr[arr < 3])

arr_2d = np.arange(50).reshape(5, 10)
print(arr_2d)
print(arr_2d[1:3, 4:6])
print(arr_2d[arr_2d > 25])

# NumPy Operations

arr = np.arange(11)
print(arr)
print(arr+arr)
print(arr-arr)
print(arr*arr)
print(arr+100)
# print(arr/arr)
print(np.sqrt(arr))
print(np.max(arr))
print(np.sin(arr))
# print(np.log(arr))
