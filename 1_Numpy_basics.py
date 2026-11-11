import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr)
print(arr.dtype)
print(arr.ndim)
print(arr.shape)
print(arr.size)
arr2=np.array([1, 2, 3 , 4, 5, 6, 7, 8, 9, 10])
print(arr2)

# Create an array of ten zeros.
arr3=np.zeros(10)
print(arr3)

# Create an array of ten ones.
arr4=np.ones(10)
print(arr4)

# Create an array containing five 7s.
arr5=np.full(5, 7)
print(arr5)

# Create an array containing numbers from 0 to 20 using arange()
arr6=np.arange(0,20)
print(arr6)

#Create an array of even numbers from 2 to 20.
arr7=np.arange(2,20,2)
print(arr7)

 #Create an array of odd numbers from 1 to 19.
arr8=np.arange(1,19,2)
print(arr8)

# Create five equally spaced numbers between 0 and 1 using linspace().
arr9=np.linspace(0, 1, 5)
print(arr9)