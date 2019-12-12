import numpy as np
import matplotlib.pyplot as plt; plt.ion()
from mpl_toolkits.mplot3d import Axes3D, proj3d
from matplotlib import animation

def svec(r):
    a = [r['S_X'], r['S_Y'], r['S_Z']]
    return np.array(a)

def plot_sp(ray):
    var = ['S_X','S_Y','S_Z']
    fig, ax = plt.subplots(3,1,sharex=True)
    for i, lbl in enumerate(var):
        ax[i].plot(ray['turn'], ray[lbl])
        ax[i].set_ylabel(lbl)
        ax[i].xaxis.grid()
    ax[2].set_xlabel('turn')

    fig, ax = plt.subplots(3,1)
    ax[0].plot(ray['S_Z'], ray['S_X'])
    ax[0].set_xlabel('S_Z'); ax[0].set_ylabel('S_X')
    ax[1].plot(ray['S_Z'], ray['S_Y'])
    ax[1].set_xlabel('S_Z'); ax[1].set_ylabel('S_Y')
    ax[2].plot(ray['S_X'], ray['S_Y'])
    ax[2].set_xlabel('S_X'); ax[2].set_ylabel('S_Y')

def plot_ps(ray):
    fix, ax = plt.subplots(2,1,sharex=True)
    ax[0].plot(ray['turn'], ray['X']); ax[0].set_ylabel('X')
    ax[1].plot(ray['turn'], ray['Y']); ax[1].set_ylabel('Y')
    ax[1].set_xlabel('turn')

def plot_decoh_meas(data):
    dm = {'X': data['S_X'].std(axis=1), 'Y': data['S_Y'].std(axis=1)}
    fig, ax = plt.subplots(2,1, sharex=True)
    ax[1].set_xlabel('turn')
    for i, lbl in enumerate(['X','Y']):
        ax[i].plot(data['turn'], dm[lbl])
        ax[i].set_ylabel('RMS(S_{})'.format(lbl))
    

plot = {'ps': lambda ray: plot_ps(ray), 'sp': lambda ray: plot_sp(ray)}

HOME = '/Users/alexaksentyev/REPOS/NICA-FS/'
NICA_EL_LBLS = np.insert(np.load('nica_element_names.npy'),0,'INJ')
NICA_EL_LBLS = np.array([e+' ['+ str(i) + ']' for i,e in enumerate(NICA_EL_LBLS)])
VARS = {
    'ps': list(zip(['X','A','Y','B','T','D'], [float]*6)),
    'sp': list(zip(['S_X','S_Y','S_Z'], [float]*3))
    }
d_type = lambda case: list(zip(['turn', 'PID'], [int]*2)) + VARS[case]
    
dat = {
    'sp' : np.loadtxt(HOME+'data/DECOH/TRPSPI:TR.dat', d_type('sp'), skiprows=2),
    'ps': np.loadtxt(HOME+'data/DECOH/TRPRAY:TR.dat', d_type('ps'), skiprows=2)
    }
nray = dat['sp']['PID'].max() + 1
for el in ['ps','sp']:
    dat[el].shape = (-1, nray)
    dat[el] = dat[el][:,1:]


pid = 0
plot['sp'](dat['sp'][:,pid])

