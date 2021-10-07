# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 17:18:59 2021

@author: mdebs
"""
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import scipy


matches=np.loadtxt('C:\\Users\\mdebs\\OneDrive\\Desktop\\HETVIPS\\matches_unique')
idx_virus=np.loadtxt('C:\\Users\\mdebs\\OneDrive\\Desktop\\HETVIPS\\idx_hetvips_unique')
h=fits.open('C:\\Users\\mdebs\\OneDrive\\Desktop\\HETVIPS\\classification_102.fits')
virus_class_1=h[8].data
virus_class_1=np.array(virus_class_1)
virus_class_1=virus_class_1.astype(int)
virus_class=[]
idx_virus=np.array(idx_virus)
idx_virus=idx_virus.astype(int)
for i in np.arange(len(idx_virus)):
    #j=idx_virus[i]
    virus_class.append(virus_class_1[i])
star_match,star_galaxy,star_qso,star_und=(0,0,0,0)
galaxy_match,galaxy_star,galaxy_qso,galaxy_und=(0,0,0,0)
qso_match,qso_star,qso_galaxy,qso_und=(0,0,0,0)
star,galaxy,qso=([],[],[])
star_sdss,galaxy_sdss,qso_sdss=([],[],[])
star_idx,galaxy_idx,qso_idx=([],[],[])
sdss_class=[None]*len(matches)
text_file=open('C:\\Users\\mdebs\\OneDrive\\Desktop\\HETVIPS\\sdss_class_unique.txt','r')
sdss_class=text_file.readlines()
text_file.close()
sdss_class=np.array(sdss_class)
sdss_z=np.loadtxt('C:\\Users\\mdebs\\OneDrive\\Desktop\\HETVIPS\\sdss_z_unique')
sdss_z=np.array(sdss_z)
sdss_z=sdss_z.astype(float)
for i in np.arange(len(matches)):
    k=idx_virus[i]
    j=matches[i]
    if sdss_class[i]=="STAR  \n":
        if virus_class[i]==1:
            star_match+=1
            star.append(k)
            star_idx.append(i)
            star_sdss.append(j)
        elif virus_class[i]==2:
            star_galaxy+=1
        elif virus_class[i]==3:
            star_qso+=1
        else:
            star_und+=1
    elif sdss_class[i]=="GALAXY\n":
        if abs(sdss_z[i])<0.001:
            if virus_class[i]==1:
                star_match+=1
                star.append(k)
                star_idx.append(i)
                star_sdss.append(j)
            elif virus_class[i]==2:
                star_galaxy+=1
            elif virus_class[i]==3:
                star_qso+=1
            else:
                star_und+=1
        else:
            if virus_class[i]==1:
                galaxy_star+=1
            elif virus_class[i]==2:
                galaxy_match+=1
                galaxy.append(k)
                galaxy_idx.append(i)
                galaxy_sdss.append(j)
            elif virus_class[i]==3:
                galaxy_qso+=1
            else:
                galaxy_und+=1
    else:
        if virus_class[i]==1:
            qso_star+=1
        elif virus_class[i]==2:
            qso_galaxy+=1
        elif virus_class[i]==3:
            qso_match+=1
            qso.append(k)
            qso_idx.append(i)
            qso_sdss.append(j)
        else:
            qso_und+=1

print(star_match,star_galaxy,star_qso,star_und)
print(" ")
print(galaxy_star,galaxy_match,galaxy_qso,galaxy_und)
print(" ")
print(qso_star,qso_galaxy,qso_match,qso_und)