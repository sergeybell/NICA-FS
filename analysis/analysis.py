import numpy as np
import matplotlib.pyplot as plt; plt.ion()

d_type = list(zip(['TURN','PID'], [int]*2)) + list(zip(['X','A','Y','B','T','D'], [float]*6))
dat = np.loadtxt('data/TEST/TRPRAY:RUN.dat', d_type, skiprows=2)
nray = dat['PID'].max() + 1
dat.shape = (-1, nray)


fig, ax = plt.subplots(2,1, sharex=True)
ax[0].plot(dat['X'][:,1])
ax[0].set_ylabel('X')
ax[1].plot(dat['Y'][:, 1])
ax[1].set_ylabel('Y')
