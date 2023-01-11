import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}
panda1 = pd.Series(data=my_data)
print(panda1)
panda2 = pd.Series(data=my_data, index=labels)
panda3 = pd.Series(my_data, labels)
print(panda2)
panda4 = pd.Series(arr)
panda5 = pd.Series(d)
print(panda5)

ser1 = pd.Series([1, 2, 3, 4], ['USA', 'Germany', 'USSR', 'Japan'])
ser2 = pd.Series([1, 2, 5, 4], ['USA', 'Germany', 'Italy', 'Japan'])
print(ser2['USA'])
ser3 = pd.Series(data=labels)
print(ser3)
print(ser1 + ser2)

