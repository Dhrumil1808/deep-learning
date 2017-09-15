import numpy as np 
from matplotlib import pyplot as plt 

x = np.arange(1,5) 
y = 3 * x
plt.title("Matplotlib example 1")
plt.xlabel("x axis") 
plt.ylabel("y axis") 
plt.plot(x,y) 
plt.show()