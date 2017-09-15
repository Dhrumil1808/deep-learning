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