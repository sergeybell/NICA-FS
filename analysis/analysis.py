import numpy as np
import matplotlib.pyplot as plt; plt.ion()

class Analysis:
    def __init__(self, data):
        self._data = data
        self._spin = {lbl: data['S_'+lbl] for lbl in ['X','Y','Z']}
        self._nray = self._spin['X'].shape[1]
        S = {lbl:data['S_'+lbl] for lbl in ['X','Y','Z']}
        nray = S['X'].shape[1]
        P = {lbl: np.sum(S[lbl],axis=1)/nray for lbl in ['X','Y','Z']}
        self._Pvec = P
        self._Pval = np.sqrt(self._Pvec['X']**2 + self._Pvec['Y']**2 + self._Pvec['Z']**2)

    @property
    def Pvec(self):
        return self._Pvec
    @property
    def Pval(self):
        return self._Pval
    @property
    def S(self):
        return self._spin
