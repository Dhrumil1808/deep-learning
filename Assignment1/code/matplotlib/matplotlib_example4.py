from matplotlib import pyplot as plt 
z= [1,3,5] 
y = [4,5,6]
plt.title('Bar graph plot using matplotlib') 
x1 = [2,4,6] 
y1 = [10,11,12] 
plt.bar(z, y, color='r', align = 'center') 
plt.bar(x1, y1, color = 'b', align = 'center') 
plt.ylabel('Y axis') 
plt.xlabel('X axis')  
plt.show()