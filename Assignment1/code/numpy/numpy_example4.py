import numpy as np 
a = np.array([[3,4,5],[6,7,8],[1,2,3]]) 

print 'Original array:' 
print a 
  

z = a[1:4,1:3] 

y = a[2:3,[1,2]] 

print 'Array after Slicing' 
print y