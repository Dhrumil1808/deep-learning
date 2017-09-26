
# coding: utf-8

# 1) Variables
# 
# Variables are elements which are assigned a particular value. They reserve memory locations to store value.
# 
# Programming question:
# Write a Python Program to print values 2 and 3.
# 

# In[57]:

a=2;
b=3;

print(a);
print(b);


# 2) Objects
# 
# Objects refer to an instance of class.  It is a location in memory having a value and it can be a variable, a function or a method.
# 
# Programming question:
# Write a python program to call a function in class through an object.
#     

# In[58]:

class basic:
    def function(self):
        print ("this is called from a function")
        
object1=basic(); #object of class "basic" is created
object1.function()   #function called with the help of object


# 3) Function
# 
# Function is a procedure through which a specific task is accomplished. In Python functions are defined by "def" keyword.
# 
# Programming question:
# Write a Python program to add two numbers.

# In[59]:

def sum(a,b): # function to add two numbers
    c = a + b
    print c

sum(2,3)    
    


# 4)  Events
# 
# Events are used to communicate between threads. They are responsible for synchronizing two or more thread operations.
# 
# Programming Question:
# Write a Python program to create 4 threads and use event's wait and set function to handle those threads.

# In[81]:

import threading #library for the thread and events

e = threading.Event() #event is created
thread = [] # array of threads

#function to handle the threads

def main_thread():
    thread_name = threading.current_thread().name
    print 'Thread waiting for event: %s' % thread_name
    e.wait(3) #waits for 3 seconds
    print 'Thread got event: %s' % thread_name
    e.set() #thread is set
    print 'Thread set: %s' % thread_name

for threads in range(4):
    threads = threading.Thread(target=main_thread)
    thread.append(threads)
    threads.start() # creates the thread and calls the "main_thread" function


# 5) Arrays
# 
# An array is a data structure which stores all the values of same data type. 
# 
# Programming Question:
# Create an array in Python and print all the values of array.
# 

# In[82]:

a=[1,2,3,4,5]
for i in range(len(a)):
    print(a[i])


# 6) Conditions
# 
# Condition consists of group of statements and it gives different output according to the input given by the user.
# 
# Programming Question:
# Write a Python program to check whether a given number is less than, equal to or greater than 10.

# In[62]:

a=10;
if(a <10): #evaluated when input is less than 10
    print "a is less than 10"
elif( a ==10): #evaluated when input equals 10
    print "a is equal to 10"
else: #evaulated when input is greater than 10
    print "a is greater than 10"


# 7) Errors
# 
# Errors are any types of issues which prevents the program from getting the desired output.
# 
# Programming Question :  Write a Python program to demonstrate syntax error and logical error
# 

# In[63]:

def func(a,b):
	print(a + b) #syntax error due to indentation

a=1
b=2

func(a,b)



# In[64]:

a=100
b=100 

if( a < b):
    print "a is less than b"
else:
    print " a is greater than b"   #logical error as it prints "a is greater than b" even though a=b


# 8) Type Conversions
# 
# Type conversion is basically changing a variable's data type. For example, changing integer data type to float.
# 
# Programming Question: Write a Python Program to demonstrate type conversion in python.
# 
# 

# In[65]:

string = "100"
integer= int("100")  
bases=int(string,2) # converted the string to base 2
decimal= 3
decimal= float(integer)  #type casted from integer to float

print(integer)
print(decimal)
print(bases)


# 9) Numpy Library
# 
# Numpy is a package for performing scientific computation in Python. It is mainly used for performing operations on multi dimensional arrays and matrices
# 
# Programming Question 1:  Write a Python program to declare array with numpy library

# In[66]:

import numpy as np
arr=np.array([1,2,3,4]) #declaring array with numpy
print(arr)


# Programming Question 2: Write a Python Program to shape and reshape arrays using numpy library.

# In[67]:

import numpy as np 
a = np.arange(24)  
print a
print a.shape

b = a.reshape(2,4,3)  #reshaped array
print b 


# Programming Question 3: Write a Python program to calculate the sum of two arrays of different sizes.
# 

# In[68]:

import numpy as np 
first = np.array([[0.0,1.0,2.0],[6.0,7.0,8.0]]) 
second = np.array([1.0,2.0,3.0])  
   
print ' First Array'
print first

print 'Second Array'
print second

print 'resultant array'
print first + second


# Programming Question 4:  Write a program to slice the array using numpy library.

# In[83]:

import numpy as np 
a = np.array([[3,4,5],[6,7,8],[1,2,3]]) 

print 'Original array:' 
print a 
  

z = a[1:4,1:3] 

y = a[2:3,[1,2]] 

print 'Array after Slicing' 
print y


# Programming Question 5: Write a Python program to compute the trignometric ratios of given angles

# In[70]:

import numpy as np 
arr = np.array([0,30,45,60,90,120,135,150,180]) 
print 'Sine value of the angles' 
print np.sin(arr*np.pi/180) 
print 'Cosine values of the given angles' 
print np.cos(arr*np.pi/180) 
print 'Tangent values of given values' 
print np.tan(arr*np.pi/180) 


# 10) Pandas Library
# 
# Pandas is a library which provides high performance data structures and data analysis tools for Python Programming Language. 
# 
# Programming Question 1: Write a Python program to create series using pandas library

# In[86]:

import pandas as pd
import numpy as np
a = np.array(['a','b','c','d'])
s = pd.Series(a)
print s


# Programming Question 2: Write a Python Program to draw a table with three columns "student id", "name" and "age".
# 

# In[72]:

import pandas as pd
arr=[[123,'Andrew',15],[456,'Mike',17],[789,'John',16]]
df = pd.DataFrame(arr,columns=['Student Id','Name','Age'])
print df


# Programming Question 3: Write a Python Program to create a basic panel.
# 

# In[73]:

import pandas as pd
import numpy as np

panel = np.random.rand(1,2,3)
panel = pd.Panel(panel)
print panel


# Programming Question 4: Take the data from question 2, and sort the values with respect to columns "Student ID", "Name" and "Age"

# In[74]:

import pandas as pd

unsorted_data = pd.DataFrame({'student_id':[123,456,789],'Name':['Andrew','Mike','John'],'Age':[15,17,16]})
sorted_data_age = unsorted_data.sort_values(by='Age') #sorted according to age
sorted_data_name = unsorted_data.sort_values(by='Name') #sorted according to Name
sorted_data_studentid = unsorted_data.sort_values(by='student_id') #sorted according to student id

print "Sorted Data according to Age"
print sorted_data_age
print " "
print "Sorted Data according to Name"
print sorted_data_name
print " " 
print "Sorted Data according to Student Id"
print sorted_data_studentid


# Programming Question 5: Using the same data in the previous question, use the describe method for the dataframes and watch the output.

# In[75]:

import pandas as pd

unsorted_data = pd.DataFrame({'student_id':[123,456,789],'Name':['Andrew','Mike','John'],'Age':[15,17,16]})
sorted_data = unsorted_data.sort_values(by='Age').sum();
print unsorted_data.describe();


# 11) Matplotlib Lirary
# 
# Matplotlib Library is plotting library for Python. 
# 
# Programming Question 1: Plot a staight line of equation y= 3 * x;
# 

# In[76]:

import numpy as np 
from matplotlib import pyplot as plt 

x = np.arange(1,5) 
y = 3 * x
plt.title("Matplotlib example 1")
plt.xlabel("x axis") 
plt.ylabel("y axis") 
plt.plot(x,y) 
plt.show()


# Programming Question 2: Create a histogram using matplotlib library.

# In[77]:

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


# Programming Question 3: Plot a sine wave using matplotlib

# In[85]:

import numpy as np 
import matplotlib.pyplot as plt  

plt.title("plottng a sine wave using matplotlib") 
x_axis=np.arange(0,10, 0.1) 
y_axis=np.sin(x_axis) 
plt.plot(x_axis, y_axis) 
plt.show() 


# Programming Question 4: Create bar graph using matplotlib library

# In[79]:

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


# Programming Question 5: Using subplot function plot the sine, cosine and tangent wave.

# In[80]:

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


# In[ ]:



