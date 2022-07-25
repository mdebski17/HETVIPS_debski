# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 12:17:34 2022

@author: mdebs
"""

import numpy as np
import matplotlib.pyplot as plt

sn=np.loadtxt('C:\\Users\\mdebs\\OneDrive\\Desktop\\HETVIPS\\sn_unique_catalog')
chi2=np.loadtxt('C:\\Users\\mdebs\\OneDrive\\Desktop\\HETVIPS\\chi2_unique_catalog')
sn=np.array(sn).astype(float)
chi2=np.array(chi2).astype(float)

delta_chi2=[]
for i in np.arange(len(chi2)):
    x=chi2[i]
    a,b=np.partition(x,1)[0:2]
    delta_chi2.append(abs(a-b))
    
delta_chi2=np.array(delta_chi2).astype(float)

value=np.where(sn>5)
high_sn=[]
high_chi2=[]
for i in np.arange(len(value)):
    j=value[i]
    high_sn.append(sn[j])
    high_chi2.append(delta_chi2[j])

high_sn=np.array(high_sn[0])
high_chi2=np.array(high_chi2[0])

value2=np.where(sn<5)
low_sn=[]
low_chi2=[]
for i in np.arange(len(value2)):
    j=value2[i]
    low_sn.append(sn[j])
    low_chi2.append(delta_chi2[j])
    
low_sn=np.array(low_sn[0])
low_chi2=np.array(low_chi2[0])
bins_high=np.linspace(0,20,num=201)
bins_low=np.linspace(0,33000,num=34)

high_indices=np.digitize(high_chi2,bins_high)
low_indices=np.digitize(low_chi2,bins_low)

high_chi2_dist=[]
for j in np.arange(len(bins_high)):
    c=j+1
    count=len(np.where(high_indices==c)[0])
    high_chi2_dist.append(count)

high_chi2_dist=np.array(high_chi2_dist).astype(int)
high_chi2_dist=high_chi2_dist/len(high_chi2)*100
    
low_chi2_dist=[]
for j in np.arange(len(bins_low)):
    c=j+1
    count=len(np.where(low_indices==c)[0])
    low_chi2_dist.append(count)

 
#plt.plot(bins_high,high_chi2_dist)


plt.scatter(sn,delta_chi2,alpha=0.1)
plt.xlim(5,200)
plt.ylim(0,500)
plt.xlabel('S/N')
plt.ylabel('Delta Chi2')



        



