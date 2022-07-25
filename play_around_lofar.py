# -*- coding: utf-8 -*-
"""
Created on Mon May 16 15:21:45 2022

@author: mdebs
"""

from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

f=fits.open("C:\\Users\\mdebs\\OneDrive\\Desktop\\HETVIPS\\classification_203.fits")
info=f["class"].data
zs=f['zs'].data



idx=[]

for i in np.arange(len(info)):
    idx.append(i)
    
sel=idx

wave=np.linspace(3470,5540,1036)

for s in sel:
    plt.figure(figsize=(12,5))
    plt.plot(wave,f[0].data[s,3],lw=1,color="black")
    plt.xlabel(r"Wavelength ($\mathring{A}$)")
    plt.show()
    ans=input()
    if ans == 'q':
        break
