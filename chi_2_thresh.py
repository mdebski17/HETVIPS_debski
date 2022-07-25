# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 11:46:09 2021

@author: mdebs
"""
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import matplotlib.ticker as mtick
from matplotlib.ticker import (AutoMinorLocator)

matches=np.loadtxt('C:\\Users\\mdebs\\OneDrive\\Desktop\\HETVIPS\\matches_unique')
h=fits.open('C:\\Users\\mdebs\\OneDrive\\Desktop\\HETVIPS\\classification_102.fits')

virus_class=np.array(h[1].data).astype(int)
class_1=np.array(h[7].data).astype(int)
class_2=np.array(h[8].data).astype(int)
class_3=np.array(h[9].data).astype(int)
class_4=np.array(h[10].data).astype(int)
class_5=np.array(h[11].data).astype(int)
class_6=np.array(h[12].data).astype(int)
class_7=np.array(h[13].data).astype(int)
class_8=np.array(h[14].data).astype(int)
class_9=np.array(h[15].data).astype(int)
class_11=np.array(h[16].data).astype(int)
class_12=np.array(h[17].data).astype(int)
class_13=np.array(h[18].data).astype(int)
class_14=np.array(h[19].data).astype(int)
class_15=np.array(h[20].data).astype(int)
class_16=np.array(h[21].data).astype(int)
class_17=np.array(h[22].data).astype(int)
class_18=np.array(h[23].data).astype(int)
class_19=np.array(h[24].data).astype(int)
class_20=np.array(h[25].data).astype(int)


known1,known2,known3,known4=(0,0,0,0)
known10,known5,known6,known7,known8=(0,0,0,0,0)
known9,known11,known12,known13,known14,known15,known16,known17=(0,0,0,0,0,0,0,0)
known18,known19,known20=(0,0,0)
for i in np.arange(len(virus_class)):
    if virus_class[i]==4:
        known10+=1
    if class_1[i]==4:
        known1+=1
    if class_2[i]==4:
        known2+=1
    if class_3[i]==4:
        known3+=1
    if class_4[i]==4:
        known4+=1
    if class_5[i]==4:
        known5+=1
    if class_6[i]==4:
        known6+=1
    if class_7[i]==4:
        known7+=1
    if class_8[i]==4:
        known8+=1
    if class_9[i]==4:
        known9+=1
    if class_11[i]==4:
        known11+=1
    if class_12[i]==4:
        known12+=1
    if class_13[i]==4:
        known13+=1
    if class_14[i]==4:
        known14+=1
    if class_15[i]==4:
        known15+=1
    if class_16[i]==4:
        known16+=1
    if class_17[i]==4:
        known17+=1
    if class_18[i]==4:
        known18+=1
    if class_19[i]==4:
        known19+=1
    if class_20[i]==4:
        known20+=1

total=len(virus_class)
known1=known1/total*100
known2=known2/total*100
known3=known3/total*100
known4=known4/total*100
known5=known5/total*100
known6=known6/total*100
known7=known7/total*100
known8=known8/total*100
known9=known9/total*100
known10=known10/total*100
known11=known11/total*100
known12=known12/total*100
known13=known13/total*100
known14=known14/total*100
known15=known15/total*100
known16=known16/total*100
known17=known17/total*100
known18=known18/total*100
known19=known19/total*100
known20=known20/total*100

x=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0]
y=[known1,known2,known3,known4,known5,known6,known7,known8,known9,known10,known11,known12,known13,known14,known15,known16,known17,known18,known19,known20]
y2=[100-known1,100-known2,100-known3,100-known4,100-known5,100-known6,100-known7,100-known8,100-known9,100-known10,100-known11,100-known12,100-known13,100-known14,100-known15,100-known16,100-known17,100-known18,100-known19,100-known20]
y3=[89.3,90.1,90.8,91.9,93.0,93.2,93.9,94.5,94.7,95.0,95.1,95.4,95.6,95.6,95.9,95.9,96,96.1,96.1,96.1]
star=[90.2,91.1,92.1,93.4,95.3,96.4,97,97,97,96.9,97.1,97.5,97.5,97.7,97.6,97.8,97.8,97.8,97.8,97.8]
galaxy=[93.9,94.2,94.1,94.2,94.1,94.1,94.1,94.4,94.6,94.7,95.1,95.3,95.4,95.4,95.4,95.5,95.6,95.7,95.7,96.0]
qso=[75.7,77.6,80.1,83.6,86.1,88.4,90,90.6,91.3,92.3,92.5,92.8,93.1,93,93.3,93.1,93.8,94.2,94.2,94.2]
fig,ax=plt.subplots();
plt.plot(x,y3,color='dodgerblue',label="Correct Label Overall")
#plt.plot(x,star,color='lightseagreen',label="Correct Star Label")
#plt.plot(x,galaxy,color='gold',label="Correct Galaxy Label")
#plt.plot(x,qso,color='dodgerblue', label="Correct Quasar Label")
plt.plot(x,y2,color='darkorchid',label="Known")
plt.legend();
plt.xlim([0.1,2])
plt.title('Diagnose Chi^2 Threshold')
plt.xlabel('Multiple of Diagnose Thresh')
plt.ylabel('Percentage of Sources')
plt.yticks(np.arange(60, 110, 10))
ax.yaxis.set_major_formatter(mtick.PercentFormatter());
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.xaxis.set_minor_locator(AutoMinorLocator())
plt.show()
    




