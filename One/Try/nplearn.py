import numpy as np
# my_array = np.array([1, 2, 3, 4, 5]) 
# print(my_array)
my_array=np.ones([2,3],dtype=np.float)
print(2*my_array)
# array2=np.ones([10,1],dtype=np.float)
print(np.transpose(my_array))
print(np.dot(my_array,np.transpose(my_array)))
# 要进行矩阵乘法或矩阵向量乘法，我们使用np.dot()方法。
# w = np.dot(A,v)