import numpy as np
import matplotlib.pyplot as plt


class Helper():
    def __init__(self):
        return

    def plot_attr(self, df, y_train, attr, trunc=.01):
	    X = df[attr]
	    
	    # Remove outliers, to improve clarity
	    mask = (X > X.quantile(trunc)) & (X < X.quantile(1-trunc))
	    X_trunc, y_trunc = X[ mask  ], y_train[ mask ]

	    bins = np.linspace( int(X_trunc.min()), int(X_trunc.max() +1), 30)
	    
	    fig, ax = plt.subplots( figsize=(8,4))
	    color = 'tab:green'
	    ax.set_xlabel(attr)
	    ax.set_ylabel('count', color=color)
	    data = X_trunc[ y_trunc == 0 ]
	    ax.hist( data, bins, alpha=0.5, label='0', color=color, weights=np.ones(len(data)) / len(data))
	    ax.tick_params(axis='y', labelcolor=color)

	    ax2 = ax.twinx()  # instantiate a second axes that shares the same x-axis

	    color = 'tab:red'
	    ax2.set_xlabel(attr)
	    ax2.set_ylabel('count', color=color)
	    data =  X_trunc[ y_trunc == 1 ]
	    ax2.hist( data, bins, alpha=0.5, label='1', color=color, weights=np.ones(len(data)) / len(data))
	    ax2.tick_params(axis='y', labelcolor=color)

    
