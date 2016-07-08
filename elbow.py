import numpy as np
from scipy.cluster.vq import kmeans,vq
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
import csv

data = []
with open('/Users/meyhel01/Documents/Traitify Excel & Charts/traitifyNum.csv', 'rU') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        data.append(', '.join(row))

# Cluster data into K = 10....100 clusters #
K = range(1,100)
KM = [kmeans(X,k) for k in K]
centroids = [cent for (cent,var) in KM]   # cluster centroids

D_k = [cdist(X, cent, 'euclidean') for cent in centroids]
cIdx = [np.argmin(D,axis=1) for D in D_k]
dist = [np.min(D,axis=1) for D in D_k]
avgWithinSS = [sum(d)/X.shape[0] for d in dist]

# Plot elbow curve #
kIdx = 9
fig = plt.figure()
ax = fig.add_subplot(111) 
ax.plot(K, avgWithinSS/totss*100, 'b*-')
ax.plot(K[kIdx], avgWithinSS[kIdx]/totss*100, marker='o', markersize=12,
    markeredgewidth=2, markeredgecolor='r', markerfacecolor='None')
ax.set_ylim((0,100))
plt.grid(True)
plt.xlabel('Number of clusters')
plt.ylabel('Percentage of variance explained (%)')
plt.title('Elbow for KMeans clustering')


plt.legend()
plt.show()
