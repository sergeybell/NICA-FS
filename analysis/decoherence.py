import numpy as np
import matplotlib.pyplot as plt; plt.ion()
from importlib import reload
import analysis as ana
reload(ana)
from scipy.optimize import curve_fit

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

def plot_decoh_meas(data):
    dm = {'X': data['S_X'].std(axis=1), 'Y': data['S_Y'].std(axis=1)}
    fig, ax = plt.subplots(2,1, sharex=True)
    ax[1].set_xlabel('turn')
    for i, lbl in enumerate(['X','Y']):
        ax[i].plot(data['turn'], dm[lbl])
        ax[i].set_ylabel('RMS(S_{})'.format(lbl))


HOME = '/Users/alexaksentyev/REPOS/NICA-FS/'
NICA_EL_LBLS = np.insert(np.load('nica_element_names.npy'),0,'INJ')
NICA_EL_LBLS = np.array([e+' ['+ str(i) + ']' for i,e in enumerate(NICA_EL_LBLS)])
VARS = {
    'ps': list(zip(['X','A','Y','B','T','D'], [float]*6)),
    'sp': list(zip(['S_X','S_Y','S_Z'], [float]*3))
    }
d_type = lambda case: list(zip(['turn', 'PID'], [int]*2)) + VARS[case]
    
dat = {
    'sp' : np.loadtxt(HOME+'data/DECOH/SHORT/TRPSPI:TR.dat', d_type('sp'), skiprows=2)#,
    # 'ps': np.loadtxt(HOME+'data/DECOH/TRPRAY:TR.dat', d_type('ps'), skiprows=2)
    }
nray = dat['sp']['PID'].max() + 1
for el in ['sp']:#,'sp']:
    dat[el].shape = (-1, nray)
    dat[el] = dat[el][:,1:]


a = ana.Analysis(dat['sp'])
# where = np.arange(0, 1001, 100)
# rays = np.arange(0, 20, 1)
# S_X, S_Y, S_Z = (a.S[lbl][where][:, rays] for lbl in ['X','Y','Z'])

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.set_xlabel('X')
# ax.set_ylabel('Z')
# ax.set_zlabel('Y')
# ax.set_xlim(-1, 1)
# ax.set_ylim(-1, 1)
# ax.set_zlim(-1, 1)

# quiver = ax.quiver(*get_arrow(0, S_X, S_Z, S_Y))

# anim = animation.FuncAnimation(fig, update, fargs=(S_X, S_Z, S_Y), interval=10, blit=False, frames=S_X.shape[0])
# anim.save('../reports/decoherence_10e6.gif')

fig, ax = plt.subplots(1,1)
nn = np.arange(0,a.Pval.shape[0])
yy = a.Pval[nn]
ftr = 1 # turns/point
ax.plot(nn*ftr, yy, '--.')
ax.ticklabel_format(axis='both', style='sci', scilimits=(0,0), useMathText=True)
ax.set_ylabel('P')
ax.set_xlabel('turn #')
popt = yy[1], (yy[-1]-yy[1])/(nn[-1]-nn[1])/ftr
# popt, pcov = curve_fit(lambda x, a,b: a + b*x, nn, yy)
ax.plot(nn*ftr, popt[0] + popt[1]*nn*ftr, 'r-', label=r'$(\beta_0 = {:4.2e}, \beta_1 = {:4.2e})$'.format(*popt))
ax.legend()

