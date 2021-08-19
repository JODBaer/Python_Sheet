import numpy as np

arr1 = np.array([[1, 2, 3],[ 4, 5, 6]])
print(arr1)
arr2 = np.arange(1,2,0.3)
print(arr2)
arr3 = np.asarray(arr1, dtype= float)
print(arr3)
arr4 = np.copy(arr1)
print(arr4 is arr1)
arr5 =np.empty((4, 2))
print(arr5)
