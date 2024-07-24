# q1. create an array with 10 equal spaced number between 0 and 1
import numpy as np
# array=np.linspace(0,1,10)
# print(array)
# # Q2 . create a 1D array of 20 random integers between 0 and 1
# array=np.random.randint(0,2,20)
# print(array)
# Q3.create a 2D array with the shape(4,4) filled with the value 7
# array=np.full((4,4),7)
# print(array)
# #Q4.create a 1D array of 10 elements with the same value 3.14
# array=np.full(10,3.14)
# print(array)
# create a 2D array with the shape (3,3) with values ranging from 1 to 9
# array=np.arange(1,10).reshape(3,3)
# print(array)
# Array
# Q 1. create two arrays a = [1,3,5,7,9],b=[2,4,6,8,10].perform element-wise subtraction
# ar1=[1,3,5,7,9]
# ar2=[2,4,6,8,10]
# print(np.subtract(ar1,ar2))
# Q2. Multiply array a by 3 a=[2,4,6,8,]
# a=np.array([2,4,6,8])
# print(a*3)
# # Q3. divide array a by 2 a=[10,20,30,40]
# ar2=np.array([10,20,30,40])
# print(ar2/2)
# Q4. Find the element type modulus of two arrrats a=[5,10,15], b=[2,3,4]
# a=np.array([5,10,15])
# b=np.array([2,3,4])
# print(np.mod(a,b))
# Creat two array: a=[1,2,3],b=[4,5,6]. Compute the dot product
# a=np.array([1,2,3])
# b=np.array([4,5,6])
# print(np.dot(a,b))
# Matrix Multiplication
# Q 1.Create two matrices:a=[[2,3],[4,5]] and b=[[1,0],[0,1]] perform matrix multiplication
# a=np.array([[1,2],[4,5]])
# b=np.array([[1,0],[0,1]])
# z = a @ b
# print(z)
# Q2. Multiply a 3*3 matrix with a 3*1 vector
# matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
# vector=np.array([[1],[2],[3]])
# print(np.dot(matrix,vector))
#Q3. create a 4*4 identity matrix and multiply it by a 4*4 matrix and multiply filled with random integer
# array=np.identity(4)
# print(array)
# array2=np.random.randint(1,10,size=(4,4))
# print(array2)
# print(np.dot(array,array2))
# Q4.perform matrix multiplication of two 3*3 matrices a=[[1,2,3],[4,5,6],[7,8,9]] and b=[[9,8,7],[6,5,4],[3,2,1]]
# ar3=np.array([[1,2,3],[4,5,6],[7,8,9]])
# ar4=np.array([[9,8,7],[6,5,4],[3,2,1]])
# print(np.dot(ar3,ar4))
# ************************ Broadcasting***********************
# Statistical operation
# Q 1. Create a mediean of the array : date=[1,2,3,4,5,6,7,8,9,10]
# array1=np.array([1,2,3,4,5,6,7,8,9,10])
# print(np.median(array1))
# # Q2. Create the mode of the array : data=[1,2,2,3,4,4,4,5,6]
# # import numpy as np
# # from collections import Counter
# #
# # array3 = np.array([1, 2, 2, 3, 4, 4, 4, 5, 6])
# #
# # # Use Counter to find the mode
# # counts = Counter(array3)
# # mode = counts.most_common(1)[0][0]
# #
# # print("Mode:", mode)
# Q 3. Calculate the range of the array : data=[10,20,30,40,50]
# data=np.array([10,20,30,40,50])
# print(np.ptp(data))
# Q4.Calculate the 25th percentile of the array : data=[1,2,3,4,5,6,7,8,9,10]
# data=np.array([1,2,3,4,5,6,7,8,9,10])
# print("the percentile of data",np.percentile(data,25))
# # Q5. Calculate the correlation coefficient between two arrays a=[1,2,3,4,5] and b=[2,4,6,8,10]
# a=np.array([1,2,3,4,5])
# b=np.array([2,4,6,8,10])
# correlation = np.corrcoef(a, b)
# correlation_coefficient = correlation[0, 1]
# print("Correlation Coefficient between a and b:", correlation_coefficient)
# # Reshape array
# # Q1.reshape a 1D array of 12 elements to 3*4 array
# # arr=np.arange(12)
# # reshap_arr=arr.reshape((3,4))
# # print("Original array:")
# # print(arr)
# # print("\nReshaped array:")
# # print(reshap_arr)
# # Q2. Reshape a 2D array of shape(6,2) to (3,4)
# arr=np.arange(12)
# reshap_arr=arr.reshape(6,2)
# Again_reshap=arr.reshape(3,4)
# print("Reshap first")
# print(reshap_arr)
# print("Reshap Second")
# print(Again_reshap)
# # flattend method-> is used to convert 2D -> 1D'
# # Q3. Create a 4*4 array and flatten
# arr=np.arange(16).reshape((4,4))
# print(arr)
# flatten=arr.flatten()
# print(flatten)
# # Q4. Reshape a 3D array of shape (2,3,4) to (4,3,2)
# arr=np.arange(24).reshape((2,3,4))
# reshape_arr=arr.reshape((4,3,2))
# print("Orignal array")
# print(arr)
# print("reshape array")
# print(reshape_arr)
# # Q5. Reshpe a 1D to a 2D array with 1 row and many columns
# array_1d = np.arange(12)
# array_2d = array_1d.reshape((1, -1))
# print("1D array:")
# print(array_1d)
# print("\nReshaped 2D array with 1 row and many columns:")
# print(array_2d)
# Element wise operation
# Q 1.create two arrays a=[1,3,5] and b=2,4,6] perform element-wise division
a=np.array([1,3,5])
b=np.array([2,4,6])
print(a/b)
# Q2.create two arrays a=[1,3,5] and b=2,4,6] perform element-wise modulus
a=np.array([1,3,5])
b=np.array([2,4,6])
print(a%b)
# Q3.Add 10 to each element in the array a =[1,2,3,4,5]
a=np.array([1,2,3,4,5])
result=a+10
print("the orignal value : ",a)
print(" the 10 add value : ",result)
# Q4. Substrect 5 from each element in the array : b=[10,20,30,40,50]
a=np.array([10,20,30,40,50])
result=a-5
print("the orignal value : ",a)
print(" the 5 sub. value : ",result)
# Q5. Square each element in the array : c=[1,2,3,4,5]
a=np.array([1,2,3,4,5])
result=a**5
print("the orignal value : ",a)
print(" the square value : ",result)
# SLicing and indexing
# Q1. Create a 3D array: array_3d = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]. Access
# the element at [1,1,1].
array_3d = np.array([[[1, 2, 3], [4, 5, 6]],
                     [[7, 8, 9], [10, 11, 12]]])
sliced_array = array_3d[1, :, :]
print("Sliced array (array_3d[1, :, :]):")
print(sliced_array)
# Q3.Slice the first layer of a 3D array: array_3d = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11,
# 12]]].
array_3d = np.array([[[1, 2, 3], [4, 5, 6]],
                     [[7, 8, 9], [10, 11, 12]]])
first_layer = array_3d[0]
print("First layer of the 3D array:")
print(first_layer)
# Q3. Access all elements in the last row of the array: array_2d = [[10, 20, 30], [40, 50, 60],
# [70, 80, 90]].
# Create the 2D NumPy array
array = np.array([[10, 20, 30],
                     [40, 50, 60],
                     [70, 80, 90]])
last_row = array[-1]
print("All elements in the last row:")
print(last_row)
# 4. Access all elements in the first column of the array: array_2d = [[10, 20, 30], [40, 50,
# 60], [70, 80, 90]].
array_2d = np.array([[10, 20, 30],
                     [40, 50, 60],
                     [70, 80, 90]])
first_column = array_2d[:, 0]

print("All elements in the first column:")
print(first_column)
#  Slice the last two rows and columns of the array: array_2d = [[10, 20, 30], [40, 50,
# 60],[70, 80, 90]])
array_2d = np.array([[10, 20, 30],
                     [40, 50, 60],
                     [70, 80, 90]])
last_two_rows_columns = array_2d[-2:, -2:]

print("Last two rows and columns:")
print(last_two_rows_columns)
# Q1.Generate a random array of 20 elements with values between 0 and 1:
random_array_0_1 = np.random.rand(20)
print("Random array with values between 0 and 1:")
print(random_array_0_1)
# Q2.Create a 4x4 array with random integers between 10 and 20:
random_array_0_1 = np.random.randint(10,20,size=(4,4))
print("Random array with values between 10 and 20:")
print(random_array_0_1)
# Q3.Create a 3x3 array with random floats between -1 and 1:
# Create a 3x3 array with random floats between -1 and 1
random = np.random.uniform(-1, 1, size=(3, 3))
print("\n3x3 array with random floats between -1 and 1:")
print(random)
# Q4.Generate an array of 15 random integers between 100 and 200:
random= np.random.randint(100,201,size=(15))
print("Random array with values between 10 and 20:")
print(random)
# Q5.Create a 5x5 array with random floats between 0 and 10:
# Stacking and concatenation
# Q1. Vertically stack two arrays: a = [[1, 2], [3, 4]] and b = [[5, 6], [7, 8]].
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
vertically_stacked = np.vstack((a, b))
print("Vertically stacked arrays:")
print(vertically_stacked)
# Q2.Horizontally stack two arrays: a = [[1, 2], [3, 4]] and b = [[5, 6], [7, 8]].
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
horizontally_stacked = np.hstack((a, b))
print("\nHorizontally stacked arrays:")
print(horizontally_stacked)
# Q3. Concatenate two 1D arrays: a = [1, 2, 3] and b = [4, 5, 6].
# Define the 1D arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
concatenated_1d = np.concatenate((a, b))
print("\nConcatenated 1D arrays:")
print(concatenated_1d)
# Q4. Concatenate two 3x3 arrays along rows: a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] and b = [[10,
# 11, 12], [13, 14, 15], [16, 17, 18]].
# Define the 3x3 arrays
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
concatenated_rows = np.concatenate((a, b), axis=0)
print("\nConcatenated along rows:")
print(concatenated_rows)
# Q5. Concatenate two 3x3 arrays along columns: a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] and b =
# [[10, 11, 12], [13, 14, 15],=[16,17,18]].
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
concatenated = np.concatenate((a, b), axis=1)
print("\nConcatenated along columns:")
print(concatenated)