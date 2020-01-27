import numpy as np
import matplotlib.pyplot as plt; plt.ion()
import analysis as ana
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
    dm = {'X': data['S_X'].std(axis=1), 'Y': data['S_Y'].std(axis=1), 'Z': data['S_Z'].std(axis=1)}
    fig, ax = plt.subplots(3,1, sharex=True)
    ax[1].set_xlabel('EID')
    for i, lbl in enumerate(['X','Y', 'Z']):
        ax[i].plot(data['EID'], dm[lbl])
        ax[i].set_ylabel('RMS(S_{})'.format(lbl))
    ax[2].set_xlabel('EID')
    plt.xticks(ticks=data['EID'][:,0], labels=NICA_EL_LBLS[data['EID'][:,0]], rotation=45)

    fig, ax = plt.subplots(1,1)
    ax.set_xlabel('RMS(S_X)')
    ax.set_ylabel('RMS(S_Y)')
    ax.plot(dm['X'], dm['Y'], '.')
    ax.ticklabel_format(axis='both', style='sci', scilimits=(0,0), useMathText=True)

HOME = '/Users/alexaksentyev/REPOS/NICA-FS/'
DIR  = 'data/TEST/TREL/LONGIT_SPIN/'

VARS = list(zip(['S_X','S_Y','S_Z'], [float]*3))
D_TYPE = list(zip(['iteration','EID', 'PID'], [int]*3)) + VARS

NICA_EL_LBLS = np.insert(np.load('nica_element_names.npy'),0,'INJ')
NICA_EL_LBLS = np.array([e+' ['+ str(i) + ']' for i,e in enumerate(NICA_EL_LBLS)])

dat = np.loadtxt(HOME+DIR+'TRPSPI:TREL.dat', D_TYPE, skiprows=2)
nray = dat['PID'].max() + 1
dat.shape = (-1, nray)
dat = dat[:,1:]; nray -= 1 # removing the zero ray

plot_decoh_meas(dat)

a = ana.Analysis(dat[:, :250])
fig, ax = plt.subplots(1,1)
ax.plot(a.Pval, '--.')
ax.ticklabel_format(axis='y', style='sci', scilimits=(0,0), useMathText=True)
ax.set_ylabel('P')
ax.set_xlabel('element #')
nn = np.arange(0,a.Pval.shape[0])
popt, pcov = curve_fit(lambda x, a,b: a + b*x, nn, a.Pval)
ax.plot(nn, popt[0] + popt[1]*nn, 'r-', label=r'$(\beta_0 = {:4.2e}, \beta_1 = {:4.2e})$'.format(*popt))
ax.legend()

S_X, S_Y, S_Z = (a.S[lbl][[0,10,50,200,300,400,450, 471]] for lbl in ['X','Y','Z'])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.view_init(30, 60)
ax.set_xlabel('X')
ax.set_ylabel('Z')
ax.set_zlabel('Y')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

quiver = ax.quiver(*get_arrow(0, S_X, S_Z, S_Y))

anim = animation.FuncAnimation(fig, update, fargs=(S_X, S_Z, S_Y), interval=600, blit=False, frames=S_X.shape[0])
anim.save('../reports/depol_sources-longit_spin.gif')
