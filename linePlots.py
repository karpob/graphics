import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import matplotlib.cm as mplcm
import matplotlib.colors as colors
from cycler import cycler


def basicLine(xvals, yvals, xaxisLabel, yaxisLabel, plotTitle, outputFile, legendItems = (), cmap = 'nipy_spectral'):
    NUM_COLORS = 1
    if(yvals.ndim >1): NUM_COLORS = yvals.shape[1]
    cNorm  = colors.Normalize(vmin=0, vmax=NUM_COLORS-1)
    scalarMap = mplcm.ScalarMappable(norm = cNorm, cmap = plt.get_cmap(cmap) )

    plt.figure()
    plt.gca().set_prop_cycle(cycler('color', [scalarMap.to_rgba(i) for i in range(NUM_COLORS)]))

    if(NUM_COLORS==1):
        plt.plot(xvals, yvals,'k')
    else:
        for i in range(yvals.shape[1]):
            plt.plot(xvals,yvals[:,i])
    plt.title(plotTitle)
    plt.xlabel(xaxisLabel)
    plt.ylabel(yaxisLabel)
    if( len(legendItems)>0 ): 
        plt.legend(legendItems)
    print('Saving: '+outputFile)
    plt.savefig(outputFile)
    plt.close()
def linePlotWithVerticalLines(xvals, yvals, verticalLines,  xaxisLabel, yaxisLabel, plotTitle, outputFile, xlim=None, xvals2=None, xvals2Label = '',vlineColor='orange', legendItems = (), cmap = 'nipy_spectral'):
    NUM_COLORS = 1
    if(yvals.ndim >1): NUM_COLORS = yvals.shape[1]
    cNorm  = colors.Normalize(vmin=0, vmax=NUM_COLORS-1)
    scalarMap = mplcm.ScalarMappable(norm = cNorm, cmap = plt.get_cmap(cmap) )

    plt.figure()
    for v in verticalLines: plt.gca().axvline(x = v, color=vlineColor) 
    plt.gca().set_prop_cycle(cycler('color', [scalarMap.to_rgba(i) for i in range(NUM_COLORS)]))

    if(NUM_COLORS==1):
        plt.plot(xvals, yvals,'k')
    else:
        for i in range(yvals.shape[1]):
            plt.plot(xvals,yvals[:,i])
    if xlim != None:
        ax = plt.gca()
        ax.set_xlim(xlim)
    if xvals2 != None:
        ax = plt.gca()
        secax = ax.secondary_xaxis('top', functions=xvals2)
        secax.set_xlabel(xvals2Label)
    plt.title(plotTitle)
    plt.xlabel(xaxisLabel)
    plt.ylabel(yaxisLabel)
    if( len(legendItems)>0 ): 
        plt.legend(legendItems)
    print('Saving: '+outputFile)
    plt.savefig(outputFile)
    plt.close()
   
