import numpy as np
import matplotlib.pyplot as plt; plt.ion()
from mpl_toolkits.mplot3d import Axes3D, proj3d
from matplotlib import animation

## for 3d animation
def get_arrow(index, S_X, S_Y, S_Z):
    return 0, 0, 0, S_X[index], S_Y[index], S_Z[index]

def update(index, S_X, S_Y, S_Z):
    global quiver
    quiver.remove()
    quiver = ax.quiver(*get_arrow(0, S_X, S_Y, S_Z), color='r')
    quiver = ax.quiver(*get_arrow(-1, S_X, S_Y, S_Z), color='k')
    quiver = ax.quiver(*get_arrow(index, S_X, S_Y, S_Z))

##

def svec(r):
    a = [r['S_X'], r['S_Y'], r['S_Z']]
    return np.array(a)

def plot_sp(ray):
    rng = {lbl: 1#ray[lbl].max() - ray[lbl].min()
               for lbl in ['S_X','S_Y','S_Z']}
    mn = {lbl: 0#ray[lbl].mean()
              for lbl in ['S_X','S_Y','S_Z']}
    var = ['S_X','S_Y','S_Z']
    fig, ax = plt.subplots(3,1,sharex=True)
    for i, lbl in enumerate(var):
        ax[i].plot(ray['EID'], np.divide(ray[lbl]-mn[lbl], rng[lbl],
                                             where=rng[lbl]!=0,
                                             out=ray[lbl]-mn[lbl]));
        ax[i].set_ylabel(lbl)
        ax[i].xaxis.grid()
    ax[2].set_xlabel('EID')
    plt.xticks(ticks=ray['EID'], labels=NICA_EL_LBLS[ray['EID']], rotation=45)

    fig, ax = plt.subplots(3,1)
    ax[0].plot(ray['S_Z'], ray['S_X'])
    ax[0].set_xlabel('S_Z'); ax[0].set_ylabel('S_X')
    ax[1].plot(ray['S_Z'], ray['S_Y'])
    ax[1].set_xlabel('S_Z'); ax[1].set_ylabel('S_Y')
    ax[2].plot(ray['S_X'], ray['S_Y'])
    ax[2].set_xlabel('S_X'); ax[2].set_ylabel('S_Y')

def plot_ps(ray):
    fix, ax = plt.subplots(2,1,sharex=True)
    ax[0].plot(ray['EID'], ray['X']); ax[0].set_ylabel('X')
    ax[1].plot(ray['EID'], ray['Y']); ax[1].set_ylabel('Y')
    ax[1].set_xlabel('EID')

case = 'trel'

plot = {'ps': lambda ray: plot_ps(ray), 'sp': lambda ray: plot_sp(ray)}

HOME = '/Users/alexaksentyev/REPOS/NICA-FS/'
NICA_EL_LBLS = np.insert(np.load('nica_element_names.npy'),0,'INJ')
NICA_EL_LBLS = np.array([e+' ['+ str(i) + ']' for i,e in enumerate(NICA_EL_LBLS)])
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


pid = 0
plot['sp'](dat['sp'][:,pid])


## animation of a particle's spin vector evolution
ray = {el : dat[el][:,pid] for el in ['ps','sp']}
S_X = ray['sp']['S_X']
S_Y = ray['sp']['S_Y']
S_Z = ray['sp']['S_Z']


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

quiver = ax.quiver(*get_arrow(0, S_X, S_Y, S_Z))

anim = animation.FuncAnimation(fig, update, fargs=(S_X, S_Y, S_Z), interval=10, blit=False)
