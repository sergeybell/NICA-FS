import numpy as np
import matplotlib.pyplot as plt; plt.ion()
from scipy.optimize import curve_fit

dat = np.loadtxt('ERROR.txt', skiprows=1, dtype = [('EL', int), ('SYM', float), ('SNR', float)])

fig, ax = plt.subplots(2,1, sharex=True)
for i, var in enumerate(['SYM', 'SNR']):
    ax[i].plot(dat['EL'], dat[var], '-.')
    ax[i].set_ylabel(var)
    ax[i].set_yscale('log')

fig1, ax1 = plt.subplots(1,1)
ax1.plot(dat['SYM'], dat['SNR'], '.')
ax1.set_xlabel('SYM')
ax1.set_ylabel('SNR')
ax1.ticklabel_format(axis='both', style='sci', scilimits=(0,0), useMathText=True)
ax1.set_yscale('log')
ax1.set_xscale('log')
