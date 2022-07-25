# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 10:47:08 2022

@author: mdebs
"""

from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.ticker import (AutoMinorLocator)

matches=np.loadtxt('C:\\Users\\mdebs\\OneDrive\\Desktop\\HETVIPS\\matches_01_22')
idx_virus=np.loadtxt('C:\\Users\\mdebs\\OneDrive\\Desktop\\HETVIPS\\idx_hetvips_unique')
h=fits.open('C:\\Users\\mdebs\\OneDrive\\Desktop\\HETVIPS\\classification_102.fits')


sdss_class=[None]*len(matches)
text_file=open('C:\\Users\\mdebs\\OneDrive\\Desktop\\HETVIPS\\sdss_class_unique.txt','r')
sdss_class=text_file.readlines()
text_file.close()
sdss_class=np.array(sdss_class)
sdss_z=np.loadtxt('C:\\Users\\mdebs\\OneDrive\\Desktop\\HETVIPS\\sdss_z_unique')
sdss_z=np.array(sdss_z)
sdss_z=sdss_z.astype(float)

thresh=np.arange(0,2.0,0.2)
percent=[]
c=6

for i in np.arange(len(thresh)):
    if i==4:
        virus_class_1=h[1].data
        virus_class_1=np.array(virus_class_1).astype(int)
        virus_class=[]
        for i in np.arange(len(idx_virus)):
            virus_class.append(virus_class_1[i])
        virus_class_2=np.array(h[15].data).astype(int)
        class_2=[]
        for i in np.arange(len(idx_virus)):
            class_2.append(virus_class_2[i])
        c=15
        
    else:
        c=c+1
        virus_class_1=h[c].data
        virus_class_1=np.array(virus_class_1)
        virus_class_1=virus_class_1.astype(int)
        virus_class=[]
        for i in np.arange(len(idx_virus)):
            #j=idx_virus[i]
            virus_class.append(virus_class_1[i])
        c=c+1
        virus_class_2=np.array(h[c].data).astype(int)
        class_2=[]
        for i in np.arange(len(idx_virus)):
            class_2.append(virus_class_2[i])
    star_match,star_galaxy,star_qso,star_und=(0,0,0,0)
    galaxy_match,galaxy_star,galaxy_qso,galaxy_und=(0,0,0,0)
    qso_match,qso_star,qso_galaxy,qso_und=(0,0,0,0)
    for i in np.arange(len(matches)):
        k=idx_virus[i]
        j=matches[i]
        if sdss_class[i]=="STAR  \n":
            if virus_class[i]==1:
                star_match+=1
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
            else:
                qso_und+=1
    for i in np.arange(len(matches)):
        k=idx_virus[i]
        j=matches[i]
        if sdss_class[i]=="STAR  \n":
            if virus_class_2[i]==1:
                star_match+=1
            elif virus_class_2[i]==2:
                star_galaxy+=1
            elif virus_class_2[i]==3:
                star_qso+=1
            else:
                star_und+=1
        elif sdss_class[i]=="GALAXY\n":
            if abs(sdss_z[i])<0.001:
                if virus_class_2[i]==1:
                    star_match+=1
                elif virus_class_2[i]==2:
                    star_galaxy+=1
                elif virus_class_2[i]==3:
                    star_qso+=1
                else:
                    star_und+=1
            else:
                if virus_class_2[i]==1:
                    galaxy_star+=1
                elif virus_class_2[i]==2:
                    galaxy_match+=1
                elif virus_class_2[i]==3:
                    galaxy_qso+=1
                else:
                    galaxy_und+=1
        else:
            if virus_class_2[i]==1:
                qso_star+=1
            elif virus_class_2[i]==2:
                qso_galaxy+=1
            elif virus_class_2[i]==3:
                qso_match+=1
            else:
                qso_und+=1
    total=star_match+star_galaxy+star_qso+galaxy_star+galaxy_match+galaxy_qso+qso_star+qso_galaxy+qso_match
    correct=star_match+galaxy_match+qso_match
    per=(correct/total)*100
    percent.append(per)

fig,ax=plt.subplots();    
plt.step(thresh,percent)
plt.xlim([0,1.8])
plt.ylim([90,97])
ax.yaxis.set_major_formatter(mtick.PercentFormatter())
plt.fill_between(thresh,percent, step='pre',alpha=0.4);
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.xaxis.set_minor_locator(AutoMinorLocator())
plt.xlabel("Multiple of Diagnose Thresh")
plt.ylabel("Percent of Sources")
plt.title("Diagnose Correct Labels with Varying Chi^2 Thresh")

