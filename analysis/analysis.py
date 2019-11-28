import numpy as np
import matplotlib.pyplot as plt; plt.ion()

def plot_sp(ray):
    fig, ax = plt.subplots(3,1,sharex=True)
    ax[0].plot(ray['S_X']); ax[0].set_ylabel('S_X')
    ax[1].plot(ray['S_Y']); ax[1].set_ylabel('S_Y')
    ax[2].plot(ray['S_Z']); ax[2].set_ylabel('S_Z')

    fig, ax = plt.subplots(2,1, sharex=True)
    ax[0].plot(ray['S_Z'], ray['S_X'])
    ax[0].set_ylabel('S_X')
    ax[1].plot(ray['S_Z'], ray['S_Y'])
    ax[1].set_ylabel('S_Y')
    ax[1].set_xlabel('S_Z')

def plot_ps(ray):
    fix, ax = plt.subplots(2,1,sharex=True)
    ax[0].plot(ray['X']); ax[0].set_ylabel('X')
    ax[1].plot(ray['Y']); ax[1].set_ylabel('Y')
    ax[1].set_xlabel('turn')

case = 'tr'

HOME = '/Users/alexaksentyev/REPOS/NICA-FS/'
VARS = {
    'ps': list(zip(['X','A','Y','B','T','D'], [float]*6)),
    'sp': list(zip(['S_X','S_Y','S_Z'], [float]*3))
    }
d_type = {
    'trel': lambda case: list(zip(['iteration','EID', 'PID'], [int]*3)) + VARS[case],
    'tr': lambda case: list(zip(['turn', 'PID'], [int]*2)) + VARS[case]
    }
    
dat = {
    'sp' : np.loadtxt(HOME+'data/TEST/TRPSPI:{}.dat'.format(case.upper()), d_type[case]('sp'), skiprows=2),
    'ps': np.loadtxt(HOME+'data/TEST/TRPRAY:{}.dat'.format(case.upper()), d_type[case]('ps'), skiprows=2)
    }
nray = dat['sp']['PID'].max() + 1
for el in ['ps','sp']:
    dat[el].shape = (-1, nray)
    dat[el] = dat[el][:,1:]

ray = {el : dat[el][:,5] for el in ['ps','sp']}

    
