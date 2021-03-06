import pandas as pd
from sklearn.cluster import KMeans
import numpy as np


X = pd.read_csv('/Users/meyhel01/Documents/Traitify Excel/traitifyNum.csv', sep=',', engine='c')
kmeans = KMeans(n_clusters=10)
clusters = kmeans.fit(X)
labels = clusters.labels_
centers = clusters.cluster_centers_

np.savetxt('/Users/meyhel01/Documents/Traitify Excel/centroids.txt', centers)
np.savetxt('/Users/meyhel01/Documents/Traitify Excel/numLabels.txt', labels)
