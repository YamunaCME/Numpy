import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr.reshape(3,4))  # Reshape the array to 3 rows and 4 columns.

arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
print(arr.reshape(4,4))  # Reshape the array to 4 rows and 4 columns.
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr.flatten())  # Flatten the 2D array to a 1D array.
print(arr.ravel())  # Flatten the 2D array to a 1D array.
print(arr.T)  # Transpose the 2D array.

# Swap the first and last rows of a matrix.
arr[[0, -1]] = arr[[-1, 0]]
print(arr)
arr[:,[0,-1]]=arr[:,[-1,0]]  # Swap the first and last columns of a matrix.
print(arr)
arr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
#Extract a 2×2 sub-matrix from a 4×4 matrix.
sub_matrix = arr[1:3, 1:3]
print(sub_matrix)