# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 14:38:01 2021

@author: mdebs
"""


import matplotlib.pyplot as plt
plt.rcParams["text.usetex"] = False
from astropy.io import fits
import numpy as np
import seaborn as sns
from matplotlib import rc
from astropy.modeling.models import Polynomial1D
from astropy.modeling.fitting import LevMarLSQFitter
from astropy.convolution import Gaussian1DKernel, convolve
from scipy.interpolate import interp1d
import os as op
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import random

basedir = 'C:\\Users\\mdebs\\OneDrive\\Desktop\\VIRUS'
#file1 = open(op.path.join(basedir, 'paramsMILES_v9.1.txt'), 'r') 
file1=open(op.path.join('C:\\Users\\mdebs\\OneDrive\\Desktop\\VIRUS\\paramsMILES_v9.1.txt'))
Lines = file1.readlines()
info = []
for line in Lines:
    l = line.strip()
    n = l[23:27]
    t, g, m = l[51:72].split()
    if m == '--':
        m = 0.0
    if t == '--':
        continue
    
    t = float(t)
    g = float(g)
    m = float(m)
    info.append([n, t, g, m])

# define wavelength
G = Gaussian1DKernel(1.0)
wave = np.linspace(3470, 5540, 1036)
models = np.zeros((len(info), len(wave)))
i_array = np.zeros((len(info), 3))
for i in np.arange(len(info)):
    g = fits.open(op.path.join(basedir, 's%s.fits' % info[i][0]))
    waveo = (g[0].header['CRVAL1'] + np.linspace(0, len(g[0].data[0])-1,
                                             len(g[0].data[0]))
             * g[0].header['CDELT1'])
    I = interp1d(waveo, g[0].data[0], kind='quadratic', bounds_error=False,
                 fill_value=np.nan)
    models[i] = convolve(I(wave), G, preserve_nan=True) 
    i_array[i] = info[i][1:]

new_models = models*1
new_models[np.isnan(models)]=0

plt.figure()
pca = PCA().fit(new_models.T)

y = np.cumsum(pca.explained_variance_ratio_)
n_components = np.interp(0.99, y, np.arange(len(y))+1)
#results in 5.9... so choose 6 components
n_components=6
   
n_samples=len(info)
pca = PCA(n_components)

H = pca.fit_transform(new_models.T) 

# =============================================================================
# There are better ways to do this, but I thought I would share a plotting
# setup that I enjoy.
# =============================================================================

rc('font',**{'family':'serif','serif':['Times']})
rc('text', usetex=False)

sns.set_context('notebook')
sns.set_style('ticks')


# Load the continuum catalog from parallel observations between 01/2019-08/2020

f = fits.open('C:\\Users\\mdebs\\OneDrive\\Desktop\\VIRUS\\continuum_201901_202008.fits')

# =============================================================================
# The wavelength is never defined in the catalog, but is the default VIRUS
# wavelength to which I rectify all spectra
# =============================================================================
wave = np.linspace(3470, 5540, 1036)

# =============================================================================
# The info about the catalog objects is in extension 1 and includes RA, Dec,
# and signal to noise (sn)
# =============================================================================
info = f[1].data

# =============================================================================
# The spectra are in extension 2
# =============================================================================
spectra = f[2].data


error = f[3].data


weight = f[4].data


# Initialize astropy fitter
fitter = LevMarLSQFitter()

# Build an empty mask array (boolean)
mask = np.zeros(spectra.shape, dtype=bool)

# Loop through the number of spectra
print('Total number of spectra: %i' % spectra.shape[0])
for ind in np.arange(spectra.shape[0])[:]:   
    if (ind % 1000) == 0:
        # print so I know how long this is taking
        print('[Masking] at index %i' % ind)
    # Initialize this polynomial model for 3rd order
    P = Polynomial1D(3)
    # Select values that are not extreme outliers (watch for nans so use nanmedian)
    wmask = weight[ind] > 0.3*np.nanmedian(weight[ind])
    # Fit Polynomial
    fit = fitter(P, wave[wmask], weight[ind][wmask])
    # Mask values below 80% of the fit
    mask[ind] = weight[ind] < 0.8 * fit(wave)

    # Mask neighbor pixels as well because they tend to have issues but don't meet
    # the threshold.  This is a conservative step, but it is done for robustness
    # rather than completeness
    mask[ind, 1:] += mask[ind, :-1]
    mask[ind, :-1] += mask[ind, 1:]
    
    # Mask additionally spectra whose average weight is less than 5%
    badspectra = np.nanmedian(weight, axis=0) < 0.05

    mask[ind,badspectra] = True
    
new_spectra=spectra*1
new_spectra[mask]=np.nan

sn_select=np.where(info['sn']>10)[0]


for i in range(0,20):
    g=random.choice(sn_select)
    plt.figure()
    plt.plot(wave,new_spectra[g])
    select=np.isfinite(new_spectra[g])
    coeff=np.linalg.lstsq(H[select],(new_spectra[g])[select])[0]
    B=np.dot(H,coeff)
    plt.plot(wave,B+np.nanmean(new_spectra[g]))
    





