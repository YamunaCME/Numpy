import numpy as np
arr=np.array([[1,2,3],[4,5,6]])

print(np.sqrt(arr)) #Element-wise square root of the array.
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
arr2=np.array([[1,2,-3],[-4,-5,6]])
# Calculate the absolute value of negative numbers.
print(np.abs(arr2))
print(np.round([3.14159, 2.71828], 2))
print(np.argmax(arr)) #Index of the maximum value in the array.
print(np.argmin(arr)) #Index of the minimum value in the array.
print(np.sum(arr > 3)) #Count of elements greater than 3 in the array.
print(np.sum(arr%2 == 0)) #Count of even elements in the array.
print(arr[arr % 5 == 0]) #Elements divisible by 5 in the array.
arr=np.array([[101,-2,3],[4,909,-6]])
arr[arr < 0] = 0 #Replace All Negative Values with 0
print(arr) 
arr[arr>100] =100 #Replace All Values Greater Than 100 with 100
print(arr)
percentage = (arr/arr.sum() *100) #Calculate the percentage of each element in the array.
print(percentage)