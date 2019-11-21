import numpy as np
import matplotlib.pyplot as plt; plt.ion()

HOME = '/Users/alexaksentyev/REPOS/NICA-FS/'

d_type = list(zip(['iteration','EID', 'ray'], [int]*3)) + list(zip(['X','A','Y','B','T','D'], [float]*6))
dat = np.loadtxt(HOME+'data/TEST/TRPRAY:RUN.dat', d_type, skiprows=2)
nray = dat['ray'].max() + 1
dat.shape = (-1, nray)


fig, ax = plt.subplots(2,1, sharex=True)
df = dat[:, 19:]
ax[0].plot(#df['EID'][:19],
               df['X'][:19])
ax[0].set_xlabel('EID'); ax[0].set_ylabel('X')
ax[1].plot(#df['EID'][:19],
               df['Y'][:19])
ax[1].set_xlabel('EID'); ax[1].set_ylabel('Y')
