import numpy as np 
import matplotlib.pyplot as plt  

x = np.arange(0,10, 0.1) 
y_sin = np.sin(x) 
y_cos = np.cos(x)  
y_tan = np.tan(x)
   
plt.subplot(2,2,1)
plt.plot(x, y_sin) 
plt.title('Sine wave in matplotlib')     
plt.subplot(2,2,2) 
plt.plot(x, y_cos)
plt.title('Cosine wave in matplotlib')  
plt.subplot(2,2,3) 
plt.plot(x, y_cos) 
plt.title('Tangent wave in matplotlib')  

plt.show()