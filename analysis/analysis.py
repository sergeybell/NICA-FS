import numpy as np
import matplotlib.pyplot as plt; plt.ion()

HOME = '/Users/alexaksentyev/REPOS/NICA-FS/'
VARS = list(zip(['X','A','Y','B','T','D'], [float]*6))
d_type_trel = list(zip(['iteration','EID', 'ray'], [int]*3)) + VARS
d_type_tr = list(zip(['turn', 'PID'], [int]*2)) + VARS
dat = np.loadtxt(HOME+'data/TEST/TRPRAY:RUN.dat', d_type_tr, skiprows=2)
nray = dat['PID'].max() + 1
dat.shape = (-1, nray)


n=30
fig, ax = plt.subplots(2,1, sharex=True)
df = dat[:, 17:]
ax[0].plot(#df['EID'][:19],
               df['X'][:n])
#ax[0].set_xlabel('EID');
ax[0].set_ylabel('X')
ax[1].plot(#df['EID'][:19],
               df['Y'][:n])
#ax[1].set_xlabel('EID');
ax[1].set_ylabel('Y')
fig, ax = plt.subplots(2,1)
ax[0].plot(df['X'][:n], df['A'][:n], '.')
ax[1].plot(df['Y'][:n], df['B'][:n], '.')
