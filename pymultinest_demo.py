import pymultinest
import math
import os
if not os.path.exists("chains"): os.mkdir("chains")

# our probability functions
# Taken from the eggbox problem.

def myprior(cube, ndim, nparams):
	#print "cube before", [cube[i] for i in range(ndim)]
	for i in range(ndim):
		cube[i] = cube[i] * 10 * math.pi
	#print "cube after", [cube[i] for i in range(ndim)]

def myloglike(cube, ndim, nparams):
	chi = 1.
	#print "cube", [cube[i] for i in range(ndim)], cube
	for i in range(ndim):
		chi *= math.cos(cube[i] / 2.)
	#print "returning", math.pow(2. + chi, 5)
	return math.pow(2. + chi, 5)

# number of dimensions our problem has
n_params = 2

# we want to see some output while it is running
progress = pymultinest.ProgressPrinter(n_params = n_params)
progress.start()
# run MultiNest
pymultinest.run(myloglike, myprior, n_params, resume = True, verbose = True, sampling_efficiency = 0.3)
# ok, done. Stop our progress watcher
progress.stop()

# lets analyse the results
a = pymultinest.Analyzer(n_params = n_params)
s = a.get_stats()

import json
json.dump(s, file('%s.json' % a.outputfiles_basename, 'w'), indent=2)
print
print "Global Evidence:\n\t%.15e +- %.15e" % ( s['global evidence'], s['global evidence error'] )

import matplotlib.pyplot as plt
plt.clf()

# Here we will plot all the marginals and whatnot, just to show off
# You may configure the format of the output here, or in matplotlibrc
# All pymultinest does is filling in the data of the plot.
p = pymultinest.PlotMarginal(a)
for i in range(n_params):
	outfile = '%s-marginal-%d.pdf' % (a.outputfiles_basename,i)
	p.plot_conditional(i, None, with_ellipses = True, with_points = False)
	plt.savefig(outfile, format='pdf', bbox_inches='tight')
	plt.close()
	
	outfile = '%s-mode-marginal-%d.pdf' % (a.outputfiles_basename,i)
	p.plot_modes_marginal(i, with_ellipses = True, with_points = False)
	plt.savefig(outfile, format='pdf', bbox_inches='tight')
	plt.close()
	
	outfile = '%s-mode-marginal-cumulative-%d.pdf' % (a.outputfiles_basename,i)
	p.plot_modes_marginal(i, cumulative = True, with_ellipses = True, with_points = False)
	plt.savefig(outfile, format='pdf', bbox_inches='tight')
	plt.close()
	
	for j in range(i):
		p.plot_conditional(i, j, with_ellipses = True, with_points = False)
		outfile = '%s-conditional-%d-%d.pdf' % (a.outputfiles_basename,i,j)
		plt.savefig(outfile, format='pdf', bbox_inches='tight')
		plt.close()
print "take a look at the pdf files in chains/" 



 
