import numpy as np
import matplotlib.pyplot as plt; plt.ion()

## for 3d animation
from mpl_toolkits.mplot3d import Axes3D, proj3d
from matplotlib import animation

def get_arrow(index, S_X, S_Y, S_Z):
    return 0, 0, 0, S_X[index], S_Y[index], S_Z[index]

def update(index, S_X, S_Y, S_Z):
    global quiver
    quiver.remove()
    quiver = ax.quiver(*get_arrow(0, S_X, S_Y, S_Z), color='r')
    quiver = ax.quiver(*get_arrow(-1, S_X, S_Y, S_Z), color='k')
    quiver = ax.quiver(*get_arrow(index, S_X, S_Y, S_Z))

##

class Analysis:
    def __init__(self, data):
        self._data = data
        self._spin = {lbl: data['S_'+lbl] for lbl in ['X','Y','Z']}
        self._nray = self._spin['X'].shape[1]
        S = {lbl:data['S_'+lbl] for lbl in ['X','Y','Z']}
        nray = S['X'].shape[1]
        P = {lbl: np.sum(S[lbl],axis=1)/nray for lbl in ['X','Y','Z']}
