import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[1,2,3],[4,5,6]])
print(arr+arr2)  # Element-wise addition of two arrays.
print(arr-arr2) #Element-wise subtraction of two arrays.
print(arr*arr2) #Element-wise multiplication of two arrays.
print(arr/arr2) #Element-wise division of two arrays.
print(np.sqrt(arr)) #Element-wise square root of the array.
print(np.sqrt(arr2)) #Element-wise square root of the array.
print(np.power(arr, 3)) #Element-wise cube of the array.
print(arr.sum()) #Sum of all elements in the array.
print(arr.mean()) #Mean of all elements in the array.
print(np.median(arr)) #Median of all elements in the array.
print(arr.max()) #Mkaximum value in the array.
print(arr.min()) #Minimum value in the array.
print(arr.std()) #Standard deviation of all elements in the array.
print(arr.var()) #Variance of all elements in the array.
print(arr.cumsum()) #Cumulative sum of all elements in the array.
print(arr.cumprod()) #Cumulative product of all elements in the array.
