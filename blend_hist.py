#plot histogram for blend

%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

def histogram():
    my_data = pd.read_csv('/Users/meyhel01/Documents/traitifydata.csv', sep=',', engine='c')

    personalities = my_data['Blend']
    letter_counts = Counter(personalities)
    df = pd.DataFrame.from_dict(letter_counts, orient='index')
    df.plot(kind='bar')

    ax = df.plot(kind='bar')
    fig = ax.get_figure()
    fig.savefig('/Users/meyhel01/Documents/histogram.pdf',bbox_inches='tight')
