import matplotlib.pyplot as plt
from pylab import *

rc('axes',linewidth=2)
fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4,ncols=1, sharex=True, sharey=True, figsize=(10,8))

# set facecolor of plots and grid styles
#ax1.set_facecolor('#E6E6E6')
#ax1.grid(color='#2d4cb5', linestyle='--', alpha=0.6)
#ax2.set_facecolor('#E6E6E6')
#ax2.grid(color='#2d4cb5', linestyle='--', alpha=0.6)
#ax3.set_facecolor('#E6E6E6')
#ax3.grid(color='#2d4cb5', linestyle='--', alpha=0.6)
#ax4.set_facecolor('#E6E6E6')
#ax4.grid(color='#2d4cb5', linestyle='--', alpha=0.6)

l1=ax1.errorbar(x, m_dape_tape, yerr = stdm_dape_tape, marker = 'o', label = 'Dape - Tape', ms = 8, mfc = '#2d4cb5', color = '#2d4cb5', ecolor = '#2d4cb5', mew=2, elinewidth=2, capsize = 5, capthick = 2)
l2=ax2.errorbar(x, m_date_tate, yerr = stdm_date_tate, marker = 'o', label = 'Date - Tate', ms = 8, mfc = '#2d4cb5', color = '#2d4cb5', ecolor = '#2d4cb5', mew=2, elinewidth=2, capsize = 5, capthick = 2)
l3=ax3.errorbar(x, m_gake_cake, yerr = stdm_gake_cake, marker = 'o', label = 'Gake - Cake', ms = 8, mfc = '#2d4cb5', color = '#2d4cb5', ecolor = '#2d4cb5', mew=2, elinewidth=2, capsize = 5, capthick = 2)
l4=ax4.errorbar(x, m_gate_cate, yerr = stdm_gate_cate, marker = 'o', label = 'Gate - Cate', ms = 8, mfc = '#2d4cb5', color = '#2d4cb5', ecolor = '#2d4cb5', mew=2, elinewidth=2, capsize = 5, capthick = 2)

ax1b = ax1.twinx()
l5=ax1b.errorbar(x, c_dape_tape, yerr = stdc_dape_tape, marker = 'o', label = 'Dape - Tape', ms = 8, mfc = '#952db5', color = '#952db5', ecolor = '#952db5', mew=2, elinewidth=2, capsize = 5, capthick = 2)
ax2b = ax2.twinx()
l6=ax2b.errorbar(x, c_date_tate, yerr = stdc_date_tate, marker = 'o', label = 'Date - Tate', ms = 8, mfc = '#952db5', color = '#952db5', ecolor = '#952db5', mew=2, elinewidth=2, capsize = 5, capthick = 2)
ax3b = ax3.twinx()
l7=ax3b.errorbar(x, c_gake_cake, yerr = stdc_gake_cake, marker = 'o', label = 'Gake - Cake', ms = 8, mfc = '#952db5', color = '#952db5', ecolor = '#952db5', mew=2, elinewidth=2, capsize = 5, capthick = 2)
ax4b = ax4.twinx()
l8=ax4b.errorbar(x, c_gate_cate, yerr = stdc_gate_cate, marker = 'o', label = 'Gate - Cate', ms = 8, mfc = '#952db5', color = '#952db5', ecolor = '#952db5', mew=2, elinewidth=2, capsize = 5, capthick = 2)

# more grid styling
#ax1b.grid(color='#952db5', linestyle='--', alpha=0.6)
#ax2b.grid(color='#952db5', linestyle='--', alpha=0.6)
#ax3b.grid(color='#952db5', linestyle='--', alpha=0.6)
#ax4b.grid(color='#952db5', linestyle='--', alpha=0.6)

# legend
#ax1.legend(loc='center left', bbox_to_anchor=(1.12, 0.65), fontsize=14)
#ax1b.legend(loc='center left', bbox_to_anchor=(1.12, 0.35), fontsize=14)
#ax2.legend(loc='center left', bbox_to_anchor=(1.12, 0.65), fontsize=14)
#ax2b.legend(loc='center left', bbox_to_anchor=(1.12, 0.35), fontsize=14)
#ax3.legend(loc='center left', bbox_to_anchor=(1.12, 0.65), fontsize=14)
#ax3b.legend(loc='center left', bbox_to_anchor=(1.12, 0.35), fontsize=14)
#ax4.legend(loc='center left', bbox_to_anchor=(1.12, 0.65), fontsize=14)
#ax4b.legend(loc='center left', bbox_to_anchor=(1.12, 0.35), fontsize=14)

# change ticks and labels color
ax1.spines['left'].set_color('#2d4cb5')
ax1.spines['right'].set_color('#952db5')
ax1b.spines['left'].set_color('#2d4cb5')
ax1b.spines['right'].set_color('#952db5')
ax1.tick_params(axis='y', colors='#2d4cb5',labelsize=14)
ax1b.tick_params(axis='y', colors='#952db5',labelsize=14)
ax1.set_yticks([0.33,0.34,0.35,0.36])
ax1b.set_yticks([0.882,0.885,0.888,0.891,0.894])

ax2.spines['left'].set_color('#2d4cb5')
ax2.spines['right'].set_color('#952db5')
ax2b.spines['left'].set_color('#2d4cb5')
ax2b.spines['right'].set_color('#952db5')
ax2.tick_params(axis='y', colors='#2d4cb5',labelsize=14)
ax2b.tick_params(axis='y', colors='#952db5',labelsize=14)
ax2.set_yticks([0.33,0.34,0.35,0.36])
ax2b.set_yticks([0.882,0.885,0.888,0.891,0.894])

ax3.spines['left'].set_color('#2d4cb5')
ax3.spines['right'].set_color('#952db5')
ax3b.spines['left'].set_color('#2d4cb5')
ax3b.spines['right'].set_color('#952db5')
ax3.tick_params(axis='y', colors='#2d4cb5',labelsize=14)
ax3b.tick_params(axis='y', colors='#952db5',labelsize=14)
ax3.set_yticks([0.33,0.34,0.35,0.36])
ax3b.set_yticks([0.882,0.885,0.888,0.891,0.894])

ax4.spines['left'].set_color('#2d4cb5')
ax4.spines['right'].set_color('#952db5')
ax4b.spines['left'].set_color('#2d4cb5')
ax4b.spines['right'].set_color('#952db5')
ax4.tick_params(axis='y', colors='#2d4cb5',labelsize=14)
ax4b.tick_params(axis='y', colors='#952db5',labelsize=14)
ax4.tick_params(axis='x', labelsize=16)
ax4.set_yticks([0.32,0.33,0.34,0.35,0.36])
ax4b.set_yticks([0.879,0.882,0.885,0.888,0.891])

# Fine-tune figure; make subplots close to each other and hide x ticks for
# all but bottom plot.
fig.subplots_adjust(hspace=0)
#plt.setp([a.get_xticklabels() for a in fig.axes[:-1]], visible=False)

# manually put in labels
fig.text(0.515, 0.05, 'VOT(ms)', fontsize = 22, ha='center')
fig.text(0.03, 0.515, 'Modularity', fontsize = 22, va='center', rotation='vertical', color = '#2d4cb5')
fig.text(0.97, 0.515, 'CCC', fontsize = 22, va='center', rotation=-90, color = '#952db5')
fig.text(0.515, 0.9, '0 - 498 ms', fontsize = 22, ha='center')

fig.text(0.79, 0.855, 'Dape - Tape', fontsize = 16, ha='center', color='r')
fig.text(0.79, 0.67, 'Date - Tate', fontsize = 16, ha='center', color='r')
fig.text(0.79, 0.48, 'Gake - Cake', fontsize = 16, ha='center', color='r')
fig.text(0.79, 0.29, 'Gate - Cate', fontsize = 16, ha='center', color='r')

# save
plt.savefig("../figures/M_and_CCC_vs_VOT_4pairs_separated.png", format='png',bbox_inches="tight", dpi=300)
plt.show()