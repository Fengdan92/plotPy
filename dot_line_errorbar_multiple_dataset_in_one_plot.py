import matplotlib.pyplot as plt
from pylab import *

rc('axes',linewidth=3)
fig, ax = plt.subplots(figsize=(8,4))

ax = plt.axes(facecolor='#E6E6E6')
ax.set_axisbelow(True)
# draw solid white grid lines
plt.grid(color='w', linestyle='solid')
# hide axis spines
for spine in ax.spines.values():
    spine.set_visible(False)

plt.errorbar(x, m_dape_tape, yerr = stdm_dape_tape, marker = 'o', label = 'Dape - Tape', ms = 8, mfc = '#d1881b', color = '#d1881b', ecolor = '#d1881b', mew=2, elinewidth=2, capsize = 5, capthick = 2)
plt.errorbar(x, m_date_tate, yerr = stdm_date_tate, marker = 'o', label = 'Date - Tate', ms = 8, mfc = '#bed11b', color = '#bed11b', ecolor = '#bed11b', mew=2, elinewidth=2, capsize = 5, capthick = 2)
plt.errorbar(x, m_gake_cake, yerr = stdm_gake_cake, marker = 'o', label = 'Gake - Cake', ms = 8, mfc = '#1b63d1', color = '#1b63d1', ecolor = '#1b63d1', mew=2, elinewidth=2, capsize = 5, capthick = 2)
plt.errorbar(x, m_gate_cate, yerr = stdm_gate_cate, marker = 'o', label = 'Gate - Cate', ms = 8, mfc = '#2d1bd1', color = '#2d1bd1', ecolor = '#2d1bd1', mew=2, elinewidth=2, capsize = 5, capthick = 2)


ax.set_xlabel('VOT', fontsize=22)
ax.set_ylabel('Modularity', fontsize=22)
#ax.set_xticks([0.2,0.3,0.4,0.5,0.6])
#ax.set_yticks([0.0,0.5,1,1.5,2,2.5,3])
ax.tick_params(labelsize=20)
plt.title('Time window: 0 - 500 ms', fontsize=22)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=16)
plt.savefig("../figures/M_vs_VOT_4pairs.png", format='png',bbox_inches="tight", dpi=300)
plt.show()