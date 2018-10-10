import numpy as np
import matplotlib.pyplot as plt
from pylab import *

rc('axes',linewidth=2)
fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4,ncols=1, sharex=True, sharey=True, figsize=(10,8))

ax1.set_facecolor('#E6E6E6')
ax1.grid(color='w', linestyle='solid')
ax2.set_facecolor('#E6E6E6')
ax2.grid(color='w', linestyle='solid')
ax3.set_facecolor('#E6E6E6')
ax3.grid(color='w', linestyle='solid')
ax4.set_facecolor('#E6E6E6')
ax4.grid(color='w', linestyle='solid')

l1=ax1.errorbar(x, m_dape_tape, yerr = stdm_dape_tape, marker = 'o', label = 'Dape - Tape', ms = 8, mfc = '#d1881b', color = '#d1881b', ecolor = '#d1881b', mew=2, elinewidth=2, capsize = 5, capthick = 2)
l2=ax2.errorbar(x, m_date_tate, yerr = stdm_date_tate, marker = 'o', label = 'Date - Tate', ms = 8, mfc = '#bed11b', color = '#bed11b', ecolor = '#bed11b', mew=2, elinewidth=2, capsize = 5, capthick = 2)
l3=ax3.errorbar(x, m_gake_cake, yerr = stdm_gake_cake, marker = 'o', label = 'Gake - Cake', ms = 8, mfc = '#1b63d1', color = '#1b63d1', ecolor = '#1b63d1', mew=2, elinewidth=2, capsize = 5, capthick = 2)
l4=ax4.errorbar(x, m_gate_cate, yerr = stdm_gate_cate, marker = 'o', label = 'Gate - Cate', ms = 8, mfc = '#2d1bd1', color = '#2d1bd1', ecolor = '#2d1bd1', mew=2, elinewidth=2, capsize = 5, capthick = 2)

# Fine-tune figure; make subplots close to each other and hide x ticks for
# all but bottom plot.
fig.subplots_adjust(hspace=0)
plt.setp([a.get_xticklabels() for a in fig.axes[:-1]], visible=False)

fig.text(0.515, 0.05, 'VOT', fontsize = 22, ha='center')
fig.text(0.05, 0.515, 'Modularity', fontsize = 22, va='center', rotation='vertical')
fig.text(0.515, 0.9, '0 - 500 ms', fontsize = 22, ha='center')

fig.text(0.81, 0.85, 'Dape - Tape', fontsize = 16, ha='center')
fig.text(0.81, 0.66, 'Date - Tate', fontsize = 16, ha='center')
fig.text(0.81, 0.47, 'Gake - Cake', fontsize = 16, ha='center')
fig.text(0.81, 0.28, 'Gate - Cate', fontsize = 16, ha='center')
plt.savefig("../figures/M_vs_VOT_4pairs_separated.png", format='png',bbox_inches="tight", dpi=300)
plt.show()