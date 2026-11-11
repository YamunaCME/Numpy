import numpy as np

# Create a 3×3 matrix containing zeros.
arr=np.zeros((3,3))
print(arr)

# Create a 3×3 matrix containing ones.
arr=np.ones((3,3))
print(arr)

# Create a 4×4 identity matrix.
arr=np.eye(4)
print(arr)
# Create a 2D array from a nested Python list.
arr2=np.array([[1,2,3,4],[5,6,7,8]])
print(arr2)

#. Access the first element of a NumPy array.
arr=np.array([1,2,3,4,5])
print(arr[0])

# Access the last element using negative indexing.
print(arr[-1])

# Access the second row of a 2D array.
print(arr2[1])
# Access the third column of a 2D array.
print(arr2[:,2])

# Use slicing to extract the first three elements.
print(arr2[0,0:3])
print(arr2[::-1])  # Reverse the array using slicing.