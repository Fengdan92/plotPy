import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import random

def colors(n):
	'''
	Input:
	------
	n: int. number of colors to generate

	Return:
	-------
	ret: list of (r,g,b) tuples.
	'''
	ret = []
	r = int(random.random() * 256)
	g = int(random.random() * 256)
	b = int(random.random() * 256)
	step = 256 / n
	for i in range(n):
		r += step
		g += step
		b += step
		r = int(r) % 256
		g = int(g) % 256
		b = int(b) % 256
		ret.append((float(r)/255,float(g)/255,float(b)/255)) 
	return ret

def draw_errorbar_multiple_dataset_in_one_plot(lst_x, lst_y, lst_yerr, lst_labels, xlabel, ylabel, title, outfile, axes_linewidth = 2, fsize = (8,4), fancy = True):
	'''
	Input:
	------
	lst_x: list of lists. Each element represent one dataset.
	lst_y: list of lists. Each element represent one dataset.
	lst_yerr: list of lists. Each element represent one dataset.
	axes_linewidth: float. Line width of axes.
	fsize: (float, float). Canvas size.
	fc: color, in '#xxxxxx' or 'colorname'. Face color of plot.
	'''
	if len(lst_x) != len(lst_y):
		sys.exit('Error: lst_x and lst_y should have the same length!')
	elif len(lst_y) != len(lst_yerr):
		sys.exit('Error: lst_y and lst_yerr should have the same length!')
	elif len(lst_y) != len(lst_labels):
		sys.exit('Error: missing labels!')
	else:
		print "Number of datasets: " + str(len(lst_x))

	n = int(len(lst_x))
	lst_colors = colors(n)
	print lst_colors

	rc('axes',linewidth = axes_linewidth)
	fig, ax = plt.subplots(figsize=fsize)

	if fancy == True:
		ax = plt.axes(facecolor='#E6E6E6')
		ax.set_axisbelow(True)
		# draw solid white grid lines
		plt.grid(color='w', linestyle='solid')
	
		# hide axis spines
		for spine in ax.spines.values():
			spine.set_visible(False)

	for i in range(n):
		plt.errorbar(lst_x[i], lst_y[i], yerr = lst_yerr[i], marker = 'o', label = lst_labels[i], ms = 8, mfc = lst_colors[i], color = lst_colors[i], ecolor = lst_colors[i], mew=2, elinewidth=2, capsize = 5, capthick = 2)

	ax.set_xlabel(xlabel, fontsize=22)
	ax.set_ylabel(ylabel, fontsize=22)
	#ax.set_xticks([0.2,0.3,0.4,0.5,0.6])
	#ax.set_yticks([0.0,0.5,1,1.5,2,2.5,3])
	ax.tick_params(labelsize=20)
	plt.title(title, fontsize=22)
	plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=16)
	plt.savefig(outfile, format='png',bbox_inches="tight", dpi=300)
	plt.close()


if __name__ == '__main__':
	lst_x = [[1,2,3],[1,2,3],[1,2,3]]
	lst_y = [[1,2,3],[1,3,2],[2,1,3]]
	lst_yerr = [[0.1,0.2,0.3],[0.1,0.3,0.2],[0.2,0.1,0.3]]
	lst_labels = ['1','2','3']
	xlabel = 'x label'
	ylabel = 'y label'
	title = 'Title'
	outfile = './test_plot.png'
	draw_errorbar_multiple_dataset_in_one_plot(lst_x, lst_y, lst_yerr, lst_labels, xlabel, ylabel, title, outfile)
