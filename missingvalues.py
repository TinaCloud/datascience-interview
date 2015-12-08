import pandas
import numpy as np

# dataframe
df = pandas.read_csv('products.csv')
newdf = pandas.DataFrame()

for i in df.index:
    row = df.ix[i]
    # find the average
    avg = row[4:8].mean(axis=1)
    if np.isnan(avg):
        avg = 0
        
    if np.isnan(row[4]):
        row[4] = avg
    
    if np.isnan(row[5]):
        row[5] = avg
      
    if np.isnan(row[6]):
        row[6] = avg
        
    if np.isnan(row[7]):
        row[7] = avg    
        
    newdf = newdf.append(row,ignore_index=True)    

newdf.to_csv('new_products.csv')

        