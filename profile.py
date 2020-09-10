import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import matplotlib.colors as colors
from cycler import cycler
import matplotlib.cm as mplcm

def plotContour( xgrid, ygrid, zgrid, xlabel, ylabel, zlabel, title, outputFile, zlim = [], xlim =[], cmap='bwr', figureResolution = 100):
    """
    Plot a color contour plot. 
    An example using Jacobians:
                            xgrid --> channel numbers/wavelengths
                            ygrid --> pressure levels
                            zgrid --> jacobian[channel, pressure level]
                            xlabel --> 'Channel Number'
                            ylabel --> 'Pressure [hPa]'
                            outputFile --> 'IASI_Ozone_Jacobians_Contour.png'
                            figureResolution --> resolution on DPI 

    """
    fig =  plt.figure()
    if(len(zlim)==0):
        zlim = zgrid.min().min(), zgrid.max().max()
    plt.pcolormesh(xgrid, ygrid, zgrid.T,vmin=zlim[0], vmax=zlim[1], cmap=cmap ) 
    cb = plt.colorbar(orientation='horizontal',pad=0.2)
    cb.set_label(zlabel)
    plt.ylabel( ylabel )
    plt.xlabel( xlabel )
    plt.gca().set_yscale('log')
    plt.gca().invert_yaxis()
    if(len(xlim)>0): plt.xlim(xlim)
    plt.yticks(np.array([1100.0,1000.0, 100.0, 10.0, 1.0, 0.1 ]),['','1000.0','100.0','10.0','1.0','0.1',])
    #plt.tight_layout() 
    print('Saving {}'.format(outputFile))
    #plt.ylim([ygrid.max().max(),ygrid.min().min()])
    fig.suptitle(title)
    plt.savefig(outputFile, dpi=figureResolution)
    plt.close()

def plotContourLabelIdx( xgrid, ygrid, zgrid, xlabel, ylabel, zlabel, title, outputFile, zlim = [], cmap='bwr', figureResolution = 100):
    """
    Plot a color contour plot. 
    An example using Jacobians:
                            xgrid --> channel numbers/wavelengths
                            ygrid --> pressure levels
                            zgrid --> jacobian[channel, pressure level]
                            xlabel --> 'Channel Number'
                            ylabel --> 'Pressure [hPa]'
                            outputFile --> 'IASI_Ozone_Jacobians_Contour.png'
                            figureResolution --> resolution on DPI 

    """
    fig = plt.figure()
    if(len(zlim)==0):
        zlim = zgrid.min().min(), zgrid.max().max()
    plt.pcolormesh(np.arange(len(xgrid)+1), ygrid, zgrid.T, vmin=zlim[0], vmax=zlim[1], cmap=cmap ) 
    cb = plt.colorbar(orientation='horizontal', pad=0.35)
    cb.set_label( zlabel ) 
    plt.ylabel( ylabel )
    plt.xlabel( xlabel )
    plt.gca().set_yscale('log')
    plt.gca().invert_yaxis()
    plt.xticks(np.arange(len(xgrid)), xgrid, rotation='vertical')
    plt.yticks(np.array([1100.0, 1000.0, 100.0, 10.0, 1.0, 0.1]),['','1000.0','100.0','10.0','1.0','0.1'])
    #plt.tight_layout() 
    fig.suptitle(title)
    print('Saving {}'.format(outputFile))
    plt.savefig(outputFile, dpi=figureResolution)
    plt.close()
def plotLines ( xgrid, ygrid, xlabel, ylabel, legendList, title, outputFile, xlim = [], ylim=[], legendFont = 6, legendColumns = 3, figureResolution = 100 ):
    """
    Plot a line plot of profiles;
    An example using Jacobians:
                               xgrid --> jacobians[nchannels,npressures]
                               ygrid --> pressure levels
                               xlabel --> 'Sensitivity [K]'
                               ylabel --> 'Pressure [hPa]'
                               legendList --> list of whatever you want to label channels/shows up on legend.
                               xlim --> [min,max] limit the range of x
                               legendFont --> font size of legend
                               legendColumns --> number of columns to use in the figure legend
                               figureResolution --> resolution on DPI 
    """
    fig =  plt.figure()
    NUM_COLORS = len(legendList)
    cm = plt.get_cmap('brg')
    cNorm  = colors.Normalize(vmin=0, vmax=NUM_COLORS-1)
    scalarMap = mplcm.ScalarMappable(norm=cNorm, cmap=cm)
    plt.gca().set_prop_cycle(cycler('color', [scalarMap.to_rgba(i) for i in range(NUM_COLORS)]))

    # plot a line for each profile.
    for i in range(xgrid.shape[0]):
        plt.plot( xgrid[i,:], ygrid )
    plt.gca().set_yscale('log')
    plt.gca().invert_yaxis()
    if(len(ylim)>0):
        plt.gca().set_ylim(ylim[0],ylim[1])

    # set limits if speficied.
    if(len(xlim)>0):
        plt.gca().set_xlim(xlim[0],xlim[1])

    # set static pressure limits.
    plt.gca().invert_yaxis()
    plt.yticks(np.array([1000.0, 100.0, 10.0, 1.0, 0.1]),['1000.0','100.0','10.0','1.0','0.1'])
    plt.legend(legendList, fontsize=legendFont,  ncol=legendColumns)
    plt.ylabel(ylabel)
    fig.suptitle(title)
    plt.savefig(outputFile)
    plt.close()
 
