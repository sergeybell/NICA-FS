import numpy as np
import matplotlib.pyplot as plt; plt.ion()

case = ('tr', 'ps')

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


n=-1
pref = {'ps':'', 'sp':'S_'}
fig, ax = plt.subplots(2,1, sharex=True)
df = dat[:, 17:]
ax[0].plot(df[pref[case[1]]+'X'][:n])
ax[0].set_ylabel(pref[case[1]]+'X')
ax[1].plot(df[pref[case[1]]+'Y'][:n])
ax[1].set_ylabel(pref[case[1]]+'Y')
