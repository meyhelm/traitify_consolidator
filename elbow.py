import numpy as np
from scipy.cluster.vq import kmeans,vq
from scipy.spatial.distance import cdist, pdist
import matplotlib.pyplot as plt
import csv
import pandas as pd


X = pd.read_csv('/Users/meyhel01/Documents/Traitify Excel & Charts/traitifyNum.csv', sep=',', engine='c')

''' with open('/Users/meyhel01/Documents/Traitify Excel & Charts/traitifyNum.csv', 'rU') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        X.append(', '.join(row)) '''

# Cluster data into K = 10....100 clusters #
K = range(1,100)
KM = [kmeans(X,k) for k in K]
centroids = [cent for (cent,var) in KM]   # cluster centroids

D_k = [cdist(X, cent, 'euclidean') for cent in centroids]
cIdx = [np.argmin(D,axis=1) for D in D_k]
dist = [np.min(D,axis=1) for D in D_k]

tot_withinss = [sum(d**2) for d in dist]  # Total within-cluster sum of squares
totss = sum(pdist(X)**2)/X.shape[0]       # The total sum of squares
betweenss = totss - tot_withinss          # The between-cluster sum of squares

# Plot elbow curve #
kIdx = 9
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(K, betweenss/totss*100, 'b*-')
ax.plot(K[kIdx], betweenss[kIdx]/totss*100, marker='o', markersize=12,
    markeredgewidth=2, markeredgecolor='r', markerfacecolor='None')
ax.set_ylim((0,100))
plt.grid(True)
plt.xlabel('Number of clusters')
plt.ylabel('Percentage of variance explained (%)')
plt.title('Elbow for KMeans clustering')


plt.legend()
plt.show()
