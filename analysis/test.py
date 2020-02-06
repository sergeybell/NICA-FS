import numpy as np
import matplotlib.pyplot as plt; plt.ion()

HOME = '/Users/alexaksentyev/REPOS/NICA-FS/'
DIR  = 'data/TEST/'

D_TYPE_BASE = list(zip(['iteration', 'PID'], [int]*2))
VARS_PS = list(zip(['X','A','Y','B','T','D'], [float]*6))
VARS_SP = list(zip(['X','Y','Z'], [float]*3))
D_TYPE_PS = D_TYPE_BASE + VARS_PS
D_TYPE_SP = D_TYPE_BASE + VARS_SP

def plot_spin(data, turns):
    fig1, ax1 = plt.subplots(4,1, sharex=True)
    for i, var in enumerate(['X','Y','Z']):
        ax1[i].plot(data[var][:turns])
        ax1[i].set_ylabel('S_'+var)
        ax1[i].ticklabel_format(axis='both', style='sci', scilimits=(0,0), useMathText=True)
    S_X, S_Y, S_Z = (data[lbl] for lbl in ['X','Y','Z'])
    Snorm = np.sqrt(S_X**2 + S_Y**2 + S_Z**2)
    ax1[3].plot(Snorm[:turns]-1)
    ax1[3].set_ylabel('|S|-1')
    ax1[3].ticklabel_format(axis='both', style='sci', scilimits=(0,0), useMathText=True)

def plot_ps(data, varx, vary, turns):
    fig2, ax2 = plt.subplots(1,1)
    ax2.plot(data[varx][:turns], data[vary][:turns], '-.')
    ax2.set_ylabel(vary)
    ax2.set_xlabel(varx)
    ax2.ticklabel_format(axis='both', style='sci', scilimits=(0,0), useMathText=True)


if __name__ == '__main__':
    ps =  np.loadtxt(HOME+DIR+'TRPRAY:COSY.dat', D_TYPE_PS, skiprows=2)
    sp =  np.loadtxt(HOME+DIR+'TRPSPI:COSY.dat', D_TYPE_SP, skiprows=2)
    nray = ps['PID'].max() + 1
    ps.shape = (-1, nray); sp.shape = (-1, nray)
    ps = ps[:,1:]; sp = sp[:, 1:]; nray -= 1 # removing the zero ray

   
    def plot_main(i0, varx='T', vary='D', turns=50):
        ii = np.arange(i0, nray, 4)
        spb = sp[:, ii]
        psb = ps[:, ii]
        plot_spin(spb, turns)
        plot_ps(psb, varx,vary, turns)
        return psb, spb

    psb, spb = plot_main(0,'iteration','X',turns=10)
