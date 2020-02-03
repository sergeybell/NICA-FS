import numpy as np
import matplotlib.pyplot as plt; plt.ion()

HOME = '/Users/alexaksentyev/REPOS/NICA-FS/'
DIR  = 'data/TEST/'

VARS_PS = list(zip(['X','A','Y','B','T','D'], [float]*6))
D_TYPE_PS = list(zip(['iteration', 'PID'], [int]*2)) + VARS_PS
ps =  np.loadtxt(HOME+DIR+'TRPRAY:COSY.dat', D_TYPE_PS, skiprows=2)
nray = ps['PID'].max() + 1
ps.shape = (-1, nray)
ps = ps[:,1:]; nray -= 1 # removing the zero ray

#ii = np.arange(3, nray, 4)
#bunch = ps[:, ii]
