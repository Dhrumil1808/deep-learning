import pandas as pd

unsorted_data = pd.DataFrame({'student_id':[123,456,789],'Name':['Andrew','Mike','John'],'Age':[15,17,16]})
sorted_data = unsorted_data.sort_values(by='Age').sum();
print unsorted_data.describe();