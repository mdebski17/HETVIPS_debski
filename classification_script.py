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
virus_class_1=np.loadtxt('C:\\Users\\mdebs\\OneDrive\\Desktop\\HETVIPS\\hetvips_unique_class_01')
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

#Load redshift information
#sdss_z=np.loadtxt('C:\\Users\\mdebs\\OneDrive\\Desktop\\VIRUS\\redshifts_correct')
#z=h["zs"].data
#sdss_z=np.array(sdss_z)

#galaxy_star_z=[]

#Look specifically at SDSS Galaxy/Diagnose star
#for i in np.arange(len(galaxy_star_isolated)):
    #j=galaxy_star_isolated[i]
    #galaxy_star_z.append(sdss_z[j])
    
#redshift_zero=0

#Find the number of SDSS Galaxies that should be stars
#for i in np.arange(len(galaxy_star_z)):
    #if abs(galaxy_star_z[i])<0.001:
        #redshift_zero+=1
        
#wave=np.linspace(3470,5540,1036)
#sel=galaxy_star_isolated

#Display plots for SDSS Galaxy/Diagnose star
#g=fits.open("classification_100.fits")
#f=fits.open('sdss_and_diagnose.fits')
#for s in sel:
    #plt.figure(figsize=(12,5))
    #plt.plot(wave,f[0].data[s,3],lw=1)
    #plt.plot(wave,g[0].data[s,0],lw=1,label='star')
    #plt.plot(wave,g[0].data[s,1],lw=1,label='galaxy')
    #print(s,g[2].data[s,1],g[1].data[s],g[4].data[s,1],f[6].data[s])
    #plt.legend()
    #plt.show()
    #ans=input()
    #if ans == 'q':
        #break
#trend=0
#for i in np.arange(len(galaxy_star_isolated)):
    #j=galaxy_star_isolated[i]
    #y=z[j][1]
    #x=z[j][2]
    #print(y,x)

        

    