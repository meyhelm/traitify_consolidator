import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import numpy as np
import csv

Q = pd.read_csv('/Users/meyhel01/Documents/Traitify Excel/traitifyNum_withTraits.csv', sep=',', engine='c')
clust = AgglomerativeClustering(n_clusters=10)
clusters = aclust.fit(Q)
labels = clusters.labels_
np.savetxt('/Users/meyhel01/Documents/Traitify Excel/numLabels.txt', labels)


'''data = []
with open('/Users/meyhel01/Documents/Traitify Excel/traitifyNum_withTraits.csv', 'rU') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        data.append(', '.join(row))
my_dict = {}
count_dict = {}
sumArray = [0]*length
for i in alabels:
    cluster = alabels[i]
    if my_dict.has_key(cluster):
        newSum = [x + y for x, y in zip(my_dict[cluster], data[i])]
        my_dict[cluster] = newSum
        count_dict[cluster]++
    else:
        my_dict[cluster] = data[i]
        count_dict[cluster] = 0

for label in my_dict:
    my_dict[label]/count_dict[label]'''
