import numpy as np
import matplotlib.pyplot as plt; plt.ion()

case = ('trel', 'sp')

filename = {'ps':'TRPRAY', 'sp':'TRPSPI'}
HOME = '/Users/alexaksentyev/REPOS/NICA-FS/'
VARS = {
    'ps': list(zip(['X','A','Y','B','T','D'], [float]*6)),
    'sp': list(zip(['S_X','S_Y','S_Z'], [float]*3))
    }
d_type = {
    'trel': list(zip(['iteration','EID', 'PID'], [int]*3)) + VARS[case[1]],
    'tr': list(zip(['turn', 'PID'], [int]*2)) + VARS[case[1]]
    }
dat = np.loadtxt(HOME+'data/TEST/{}:{}.dat'.format(filename[case[1]], case[0].upper()), d_type[case[0]], skiprows=2)
nray = dat['PID'].max() + 1
dat.shape = (-1, nray)

dat = dat[:,1:]
ray = dat[:,2]
fig, ax = plt.subplots(3,1,sharex=True)
ax[0].plot(ray['S_X']); ax[0].set_ylabel('S_X')
ax[1].plot(ray['S_Y']); ax[1].set_ylabel('S_Y')
ax[2].plot(ray['S_Z']); ax[2].set_ylabel('S_Z')

fig, ax = plt.subplots(2,1, sharex=True)
ax[0].plot(ray['S_X'], ray['S_Z'])
ax[0].set_ylabel('S_Z')
ax[1].plot(ray['S_X'], ray['S_Y'])
ax[1].set_ylabel('S_Y')
ax[1].set_xlabel('S_X')
