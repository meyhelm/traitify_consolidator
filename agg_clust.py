import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import numpy as np
import csv

def agg_clust(num_clust):
    X = pd.read_csv('/Users/meyhel01/Documents/Traitify Excel/traitifyNum_withTraits.csv', sep=',', engine='c')
    clust = AgglomerativeClustering(n_clusters=num_clust)
    clusters = clust.fit(X)
    labels = clusters.labels_
    #np.savetxt('/Users/meyhel01/Documents/Traitify Excel/numLabels.txt', labels)
