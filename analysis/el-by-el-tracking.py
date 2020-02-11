import numpy as np
import matplotlib.pyplot as plt; plt.ion()
from analysis import HOMEDIR, load_ps

DATADIR = 'data/EL-BY-EL-TRACKING/'

ps = load_ps(HOMEDIR+DATADIR)

fig, ax = plt.subplots(2,1,sharex=True)
ax[0].plot(ps['X'][:471]); ax[0].set_ylabel('X')
ax[1].plot(ps['Y'][:471]); ax[1].set_ylabel('Y')
