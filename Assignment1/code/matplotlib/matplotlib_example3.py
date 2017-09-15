import numpy as np 
import matplotlib.pyplot as plt  

plt.title("plottng a sine wave using matplotlib") 
x_axis=np.arange(0,10, 0.1) 
y_axis=np.sin(x_axis) 
plt.plot(x_axis, y_axis) 
plt.show() 