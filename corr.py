import pandas as pd

my_data = pd.read_csv('Users/meyhel01/Documents/Traitify Excel/traitifydata.csv'', sep=',', engine='c')

labels=[]
for i in sorted(traits):
    labels.append(i)

frame = pd.DataFrame(my_data, columns=labels)
frame = frame.corr()

frame.to_csv('corr_matrix.csv')
