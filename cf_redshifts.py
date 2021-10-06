import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

import seaborn as sns
sns.set_context("talk") # options include: talk, poster, paper
sns.set_style("ticks")
sns.set_style({"xtick.direction": "in","ytick.direction": "in",
               "xtick.top":True, "ytick.right":True,
               "xtick.major.size":12, "xtick.minor.size":4,
               "ytick.major.size":12, "ytick.minor.size":4,
               })
### color palettes
colors = ["windows blue", "amber", "greyish", "faded green", "dusty purple"]
colors += ["cloudy blue", "browny orange", "dark sea green"]
sns.set_palette(sns.xkcd_palette(colors))
orig_palette = sns.color_palette()


def find_outlier_fraction(z_phot, z_spec, thresh=0.1):
    '''
    use to find fraction (and indices) of outlier objects given
    a threshold (provided object has a spec z measurement)

    Parameters
    ----------
    z_phot : 1d array
        photometric redshifts
    z_spec : 1d array
        spec-z's ("truth")
    thresh : float
        threshold to consider it an "outlier" (difference normalized by 1+z)
    
    Returns
    -------
    frac : float
        outlier fraction
    idx_outliers : 1d array
        indices of outliers
    '''
    idx_outliers = np.where( (np.abs(z_phot - z_spec) / (1. + z_spec)) > float(thresh) )[0]
    frac = len(idx_outliers) / len(z_phot)
    return frac, idx_outliers

def find_s_NMAD(z_phot, z_spec):
    '''
    use to find normalized median absolute deviation of objects
    that have a spec z measurement (i.e. z_spec > 0)

    Parameters
    ----------
    z_phot : 1d array
        photometric redshifts
    z_spec : 1d array
        spec-z's ("truth")
    thresh : float
        threshold to consider it an "outlier" (difference normalized by 1+z)
    
    Returns
    -------
    s_NMAD : float
        normalized median absolute deviation
    '''

    tup = [(i,j) for i,j in zip(z_phot, z_spec) if j > 0]
    phot_z, spec_z = zip(*tup)

    dif = [(i - j) for i,j in zip(phot_z, spec_z) ]
    dif_med = np.median(dif)

    num = [ abs(i-j-dif_med)/(1+j) for i,j in zip(phot_z, spec_z)]
    s_NMAD = 1.48*np.median(num)

    return s_NMAD

def mkplot_cf_redshifts(z_phot, z_spec):
    '''
    compare the redshifts

    assume z_spec == "truth" (plotted along x-axis)
    '''
    zphot_label = 'Photometric Redshift'
    zspec_label = 'Spectroscopic Redshift'

    scatter_kwargs = {'marker':'s', 's':40, 'zorder':2}
    plot_kwargs = {'ls':'--','c':'grey','lw':1.5,'zorder':1}

    gs=GridSpec(4,1)
    fig=plt.figure(figsize=(5,6))

    ax1 = fig.add_subplot(gs[0:-1])
    ax1.minorticks_on()
    ax1.scatter(z_spec, z_phot, **scatter_kwargs)
    lims = [ 0, 1.1*np.max(np.hstack([z_phot, z_spec])) ]
    ax1.plot(lims, lims, **plot_kwargs) 
    ax1.set_xlim(lims)
    ax1.set_ylim(lims)
    ax1.set_ylabel(zphot_label)
    plt.setp(ax1.get_xticklabels(),visible=False)

    ax2 = fig.add_subplot(gs[-1], sharex=ax1)
    ax2.minorticks_on()
    dz = (z_spec - z_phot) / (1. + z_spec)
    ax2.scatter(z_spec, dz, **scatter_kwargs)
    ax2.plot(lims, [0, 0], **plot_kwargs) 
    ax2.set_xlim(lims)
    ax2.set_xlabel(zspec_label)
    ax2.set_ylabel(r'$\Delta z$ / ($1+z$)')

    plt.tight_layout()
    plt.subplots_adjust(hspace=0.0)

 
