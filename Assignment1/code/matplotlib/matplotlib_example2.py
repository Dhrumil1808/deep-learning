from matplotlib import pyplot as plt 
import numpy as np  
from random import randint

a=np.array([]);   
for i in range(1,11):
    r=randint(1,50)
    a=np.append(a,r)


print a    
plt.hist(a, bins = [0,10,20,30,40,50]) 
plt.title("histogram sample matlplotlib") 
plt.show()