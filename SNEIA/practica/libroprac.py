import numpy as np
#x = np.array(8)
#x = np.array([2.3 , 4.2 , 3.3, 1.8]) 
#x = np.array([1,2,3], [4,5,61], [7,8,9]) 
#
#print ("x: ", x)
#print ("x ndim: ", x.ndim)
#print ("x shape:", x.shape)
#print ("x size: ", x.size)
#print ("x dtype: ", x.dtype) 
#
##/////////////////////////////
#
#print ("np.zeros((3,3)):1n", np.zeros((3,3)))
#print ("np.ones((3,3)):\n", np.ones((3,3)))
#print ("np.eye((3)): (identity matrix)\n", np.eye((3)))
#print ("np.random.random((3,3)):\n", np.random.random((3,3))) 
#
##/////////////////////////////
#
#x = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
#
#print (x)
#print ("x column 1: ", x[:, 1])
#print ("x row 0: ", x[0, :])
#print ("x rows 0,1 £ cols 1,2: An", x[0:2, 1:3]) 

#///////////////////////////////

a = np.array([[1,2,3], 
              [4,5,6]], dtype=np.int32)
              
b = np.array([[7,8], 
              [9,10], 
              [11, 12]], dtype=np.int32)

c =  a.dot (b)
print (f"{a.shape} : (b.shape) = {c.shape}")
print (c) 
