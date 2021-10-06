from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

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

star=0
c=0
for i in np.arange(len(sdss_class)):
	if sdss_class[i]=="STAR  \n":
		star+=1
star_only,sdss_star_only=([None]*star,[None]*star)
for i in np.arange(len(matches)):
	if sdss_class[i]=="STAR  \n":
		star_only[c]=i
		sdss_star_only[c]=i
		c+=1

sn=np.loadtxt('C:\\Users\\mdebs\\OneDrive\\Desktop\\HETVIPS\\hetvips_sn_unique')
sn=np.array(sn)
sn=sn.astype(float)
sn_star=[]
for i in np.arange(len(star_only)):
	j=star_only[i]
	sn_star.append(sn[j])
bin1_yes,bin1_und,bin1_no=(0,0,0)
bin2_yes,bin2_und,bin2_no=(0,0,0)
bin3_yes,bin3_und,bin3_no=(0,0,0)
bin4_yes,bin4_und,bin4_no=(0,0,0)
bin5_yes,bin5_und,bin5_no=(0,0,0)
bin6_yes,bin6_und,bin6_no=(0,0,0)
bin7_yes,bin7_und,bin7_no=(0,0,0)
bin8_yes,bin8_und,bin8_no=(0,0,0)
bin9_yes,bin9_und,bin9_no=(0,0,0)
bin10_yes,bin10_und,bin10_no=(0,0,0)
bin11_yes,bin11_und,bin11_no=(0,0,0)
bin12_yes,bin12_und,bin12_no=(0,0,0)
bin13_yes,bin13_und,bin13_no=(0,0,0)
bin14_yes,bin14_und,bin14_no=(0,0,0)
bin15_yes,bin15_und,bin15_no=(0,0,0)
bin16_yes,bin16_und,bin16_no=(0,0,0)
bin17_yes,bin17_und,bin17_no=(0,0,0)
bin18_yes,bin18_und,bin18_no=(0,0,0)
bin19_yes,bin19_und,bin19_no=(0,0,0)
bin20_yes,bin20_und,bin20_no=(0,0,0)
bin1,bin2,bin3,bin4,bin5,bin6,bin7,bin8,bin9,bin10=(0,0,0,0,0,0,0,0,0,0)
bin11,bin12,bin13,bin14,bin15,bin16,bin17,bin18,bin19,bin20=(0,0,0,0,0,0,0,0,0,0)
for i in np.arange(len(star_only)):
	j=star_only[i]
	k=sdss_star_only[i]
	if 0<=sn_star[i]<=2:
		if sdss_class[k]=="STAR  \n" and virus_class[j]==1:
			bin1_yes+=1
		elif sdss_class[k]=="STAR  \n" and virus_class[j]==4:
			bin1_und+=1
		else:
			bin1_no+=1
		bin1+=1
	if 2<=sn_star[i]<=4:
                if sdss_class[k]=="STAR  \n" and virus_class[j]==1:
                        bin2_yes+=1
                elif sdss_class[k]=="STAR  \n" and virus_class[j]==4:
                        bin2_und+=1
                else:
                        bin2_no+=1
                bin2+=1
	if 4<=sn_star[i]<=6:
                if sdss_class[k]=="STAR  \n" and virus_class[j]==1:
                        bin3_yes+=1
                elif sdss_class[k]=="STAR  \n" and virus_class[j]==4:
                        bin3_und+=1
                else:
                        bin3_no+=1
                bin3+=1
	if 6<=sn_star[i]<=8:
                if sdss_class[k]=="STAR  \n" and virus_class[j]==1:
                        bin4_yes+=1
                elif sdss_class[k]=="STAR  \n" and virus_class[j]==4:
                        bin4_und+=1
                else:
                        bin4_no+=1
                bin4+=1
	if 8<=sn_star[i]<=10:
                if sdss_class[k]=="STAR  \n" and virus_class[j]==1:
                        bin5_yes+=1
                elif sdss_class[k]=="STAR  \n" and virus_class[j]==4:
                        bin5_und+=1
                else:
                        bin5_no+=1
                bin5+=1
	if 10<=sn_star[i]<=12:
                if sdss_class[k]=="STAR  \n" and virus_class[j]==1:
                        bin6_yes+=1
                elif sdss_class[k]=="STAR  \n" and virus_class[j]==4:
                        bin6_und+=1
                else:
                        bin6_no+=1
                bin6+=1
	if 12<=sn_star[i]<=14:
                if sdss_class[k]=="STAR  \n" and virus_class[j]==1:
                        bin7_yes+=1
                elif sdss_class[k]=="STAR  \n" and virus_class[j]==4:
                        bin7_und+=1
                else:
                        bin7_no+=1
                bin7+=1
	if 14<=sn_star[i]<=16:
                if sdss_class[k]=="STAR  \n" and virus_class[j]==1:
                        bin8_yes+=1
                elif sdss_class[k]=="STAR  \n" and virus_class[j]==4:
                        bin8_und+=1
                else:
                        bin8_no+=1
                bin8+=1
	if 16<=sn_star[i]<=18:
                if sdss_class[k]=="STAR  \n" and virus_class[j]==1:
                        bin9_yes+=1
                elif sdss_class[k]=="STAR  \n" and virus_class[j]==4:
                        bin9_und+=1
                else:
                        bin9_no+=1
                bin9+=1
	if 18<=sn_star[i]<=20:
                if sdss_class[k]=="STAR  \n" and virus_class[j]==1:
                        bin10_yes+=1
                elif sdss_class[k]=="STAR  \n" and virus_class[j]==4:
                        bin10_und+=1
                else:
                        bin10_no+=1
                bin10+=1
	if 20<=sn_star[i]<=22:
                if sdss_class[k]=="STAR  \n" and virus_class[j]==1:
                        bin11_yes+=1
                elif sdss_class[k]=="STAR  \n" and virus_class[j]==4:
                        bin11_und+=1
                else:
                        bin11_no+=1
                bin11+=1
	if 22<=sn_star[i]<=24:
                if sdss_class[k]=="STAR  \n" and virus_class[j]==1:
                        bin12_yes+=1
                elif sdss_class[k]=="STAR  \n" and virus_class[j]==4:
                        bin12_und+=1
                else:
                        bin12_no+=1
                bin12+=1
	if 24<=sn_star[i]<=26:
                if sdss_class[k]=="STAR  \n" and virus_class[j]==1:
                        bin13_yes+=1
                elif sdss_class[k]=="STAR  \n" and virus_class[j]==4:
                        bin13_und+=1
                else:
                        bin13_no+=1
                bin13+=1
	if 26<=sn_star[i]<=28:
                if sdss_class[k]=="STAR  \n" and virus_class[j]==1:
                        bin14_yes+=1
                elif sdss_class[k]=="STAR  \n" and virus_class[j]==4:
                        bin14_und+=1
                else:
                        bin14_no+=1
                bin14+=1
	if 28<=sn_star[i]<=30:
                if sdss_class[k]=="STAR  \n" and virus_class[j]==1:
                        bin15_yes+=1
                elif sdss_class[k]=="STAR  \n" and virus_class[j]==4:
                        bin15_und+=1
                else:
                        bin15_no+=1
                bin15+=1
	if 30<=sn_star[i]<=32:
                if sdss_class[k]=="STAR  \n" and virus_class[j]==1:
                        bin16_yes+=1
                elif sdss_class[k]=="STAR  \n" and virus_class[j]==4:
                        bin16_und+=1
                else:
                        bin16_no+=1
                bin16+=1
	if 32<=sn_star[i]<=34:
                if sdss_class[k]=="STAR  \n" and virus_class[j]==1:
                        bin17_yes+=1
                elif sdss_class[k]=="STAR  \n" and virus_class[j]==4:
                        bin17_und+=1
                else:
                        bin17_no+=1
                bin17+=1
	if 34<=sn_star[i]<=36:
                if sdss_class[k]=="STAR  \n" and virus_class[j]==1:
                        bin18_yes+=1
                elif sdss_class[k]=="STAR  \n" and virus_class[j]==4:
                        bin18_und+=1
                else:
                        bin18_no+=1
                bin18+=1
	if 36<=sn_star[i]<=38:
                if sdss_class[k]=="STAR  \n" and virus_class[j]==1:
                        bin19_yes+=1
                elif sdss_class[k]=="STAR  \n" and virus_class[j]==4:
                        bin19_und+=1
                else:
                        bin19_no+=1
                bin19+=1
	if 38<=sn_star[i]<=40:
                if sdss_class[k]=="STAR  \n" and virus_class[j]==1:
                        bin20_yes+=1
                elif sdss_class[k]=="STAR  \n" and virus_class[j]==4:
                        bin20_und+=1
                else:
                        bin20_no+=1
                bin20+=1

galaxy=0
c=0
for i in np.arange(len(sdss_class)):
	if sdss_class[i]=="GALAXY\n":
		galaxy+=1
galaxy_only,sdss_galaxy_only,galaxy_idx_only=([None]*galaxy,[None]*galaxy,[None]*galaxy)
for i in np.arange(len(matches)):
	j=idx_virus[i]
	if sdss_class[i]=="GALAXY\n":
		galaxy_only[c]=j
		galaxy_idx_only[c]=i
		sdss_galaxy_only[c]=i
		c+=1
galaxy_only=np.array(galaxy_only)
galaxy_only=galaxy_only.astype(int)
sn_galaxy=[]
for i in np.arange(len(galaxy_only)):
	j=galaxy_only[i]
	sn_galaxy.append(sn[j])

for i in np.arange(len(galaxy_only)):
	j=galaxy_idx_only[i]
	k=sdss_galaxy_only[i]
	if 0<=sn_galaxy[i]<=2:
		if sdss_class[k]=="GALAXY\n" and virus_class[j]==2:
			bin1_yes+=1
		elif sdss_class[k]=="GALAXY\n" and virus_class[j]==4:
			bin1_und+=1
		else:
			bin1_no+=1
		bin1+=1
	if 2<=sn_galaxy[i]<=4:
                if sdss_class[k]=="GALAXY\n" and virus_class[j]==2:
                        bin2_yes+=1
                elif sdss_class[k]=="GALAXY\n" and virus_class[j]==4:
                        bin2_und+=1
                else:
                        bin2_no+=1
                bin2+=1
	if 4<=sn_galaxy[i]<=6:
                if sdss_class[k]=="GALAXY\n" and virus_class[j]==2:
                        bin3_yes+=1
                elif sdss_class[k]=="GALAXY\n" and virus_class[j]==4:
                        bin3_und+=1
                else:
                        bin3_no+=1
                bin3+=1
	if 6<=sn_galaxy[i]<=8:
                if sdss_class[k]=="GALAXY\n" and virus_class[j]==2:
                        bin4_yes+=1
                elif sdss_class[k]=="GALAXY\n" and virus_class[j]==4:
                        bin4_und+=1
                else:
                        bin4_no+=1
                bin4+=1
	if 8<=sn_galaxy[i]<=10:
                if sdss_class[k]=="GALAXY\n" and virus_class[j]==2:
                        bin5_yes+=1
                elif sdss_class[k]=="GALAXY\n" and virus_class[j]==4:
                        bin5_und+=1
                else:
                        bin5_no+=1
                bin5+=1
	if 10<=sn_galaxy[i]<=12:
                if sdss_class[k]=="GALAXY\n" and virus_class[j]==2:
                        bin6_yes+=1
                elif sdss_class[k]=="GALAXY\n" and virus_class[j]==4:
                        bin6_und+=1
                else:
                        bin6_no+=1
                bin6+=1
	if 12<=sn_galaxy[i]<=14:
                if sdss_class[k]=="GALAXY\n" and virus_class[j]==2:
                        bin7_yes+=1
                elif sdss_class[k]=="GALAXY\n" and virus_class[j]==4:
                        bin7_und+=1
                else:
                        bin7_no+=1
                bin7+=1
	if 14<=sn_galaxy[i]<=16:
                if sdss_class[k]=="GALAXY\n" and virus_class[j]==2:
                        bin8_yes+=1
                elif sdss_class[k]=="GALAXY\n" and virus_class[j]==4:
                        bin8_und+=1
                else:
                        bin8_no+=1
                bin8+=1
	if 16<=sn_galaxy[i]<=18:
                if sdss_class[k]=="GALAXY\n" and virus_class[j]==2:
                        bin9_yes+=1
                elif sdss_class[k]=="GALAXY\n" and virus_class[j]==4:
                        bin9_und+=1
                else:
                        bin9_no+=1
                bin9+=1
	if 18<=sn_galaxy[i]<=20:
                if sdss_class[k]=="GALAXY\n" and virus_class[j]==2:
                        bin10_yes+=1
                elif sdss_class[k]=="GALAXY\n" and virus_class[j]==4:
                        bin10_und+=1
                else:
                        bin10_no+=1
                bin10+=1
	if 20<=sn_galaxy[i]<=22:
		if sdss_class[k]=="GALAXY\n" and virus_class[j]==2:
			bin11_yes+=1
		elif sdss_class[k]=="GALAXY\n" and virus_class[j]==4:
			bin11_und+=1
		else:
			bin11_no+=1
		bin11+=1
	if 22<=sn_galaxy[i]<=24:
                if sdss_class[k]=="GALAXY\n" and virus_class[j]==2:
                        bin12_yes+=1
                elif sdss_class[k]=="GALAXY\n" and virus_class[j]==4:
                        bin12_und+=1
                else:
                        bin12_no+=1
                bin12+=1
	if 24<=sn_galaxy[i]<=26:
                if sdss_class[k]=="GALAXY\n" and virus_class[j]==2:
                        bin13_yes+=1
                elif sdss_class[k]=="GALAXY\n" and virus_class[j]==4:
                        bin13_und+=1
                else:
                        bin13_no+=1
                bin13+=1
	if 26<=sn_galaxy[i]<=28:
                if sdss_class[k]=="GALAXY\n" and virus_class[j]==2:
                        bin14_yes+=1
                elif sdss_class[k]=="GALAXY\n" and virus_class[j]==4:
                        bin14_und+=1
                else:
                        bin14_no+=1
                bin14+=1
	if 28<=sn_galaxy[i]<=30:
                if sdss_class[k]=="GALAXY\n" and virus_class[j]==2:
                        bin15_yes+=1
                elif sdss_class[k]=="GALAXY\n" and virus_class[j]==4:
                        bin15_und+=1
                else:
                        bin15_no+=1
                bin15+=1
	if 30<=sn_galaxy[i]<=32:
                if sdss_class[k]=="GALAXY\n" and virus_class[j]==2:
                        bin16_yes+=1
                elif sdss_class[k]=="GALAXY\n" and virus_class[j]==4:
                        bin16_und+=1
                else:
                        bin16_no+=1
                bin16+=1
	if 32<=sn_galaxy[i]<=34:
                if sdss_class[k]=="GALAXY\n" and virus_class[j]==2:
                        bin17_yes+=1
                elif sdss_class[k]=="GALAXY\n" and virus_class[j]==4:
                        bin17_und+=1
                else:
                        bin17_no+=1
                bin17+=1
	if 34<=sn_galaxy[i]<=36:
                if sdss_class[k]=="GALAXY\n" and virus_class[j]==2:
                        bin18_yes+=1
                elif sdss_class[k]=="GALAXY\n" and virus_class[j]==4:
                        bin18_und+=1
                else:
                        bin18_no+=1
                bin18+=1
	if 36<=sn_galaxy[i]<=38:
                if sdss_class[k]=="GALAXY\n" and virus_class[j]==2:
                        bin19_yes+=1
                elif sdss_class[k]=="GALAXY\n" and virus_class[j]==4:
                        bin19_und+=1
                else:
                        bin19_no+=1
                bin19+=1
	if 38<=sn_galaxy[i]<=40:
                if sdss_class[k]=="GALAXY\n" and virus_class[j]==2:
                        bin20_yes+=1
                elif sdss_class[k]=="GALAXY\n" and virus_class[j]==4:
                        bin20_und+=1
                else:
                        bin20_no+=1
                bin20+=1
                
qso=0
c=0
for i in np.arange(len(sdss_class)):
	if sdss_class[i]=="QSO   \n":
		qso+=1
qso_only,sdss_qso_only,qso_idx_only=([None]*qso,[None]*qso,[None]*qso)
for i in np.arange(len(matches)):
	j=idx_virus[i]
	if sdss_class[i]=="QSO   \n":
		qso_only[c]=j
		qso_idx_only[c]=i
		sdss_qso_only[c]=i
		c+=1
qso_only=np.array(qso_only)
qso_only=qso_only.astype(int)
sn_qso=[]
for i in np.arange(len(qso_only)):
	j=qso_only[i]
	sn_qso.append(sn[j])
for i in np.arange(len(qso_only)):
	j=qso_idx_only[i]
	k=sdss_qso_only[i]
	if 0<=sn_qso[i]<=2:
		if sdss_class[k]=="QSO   \n" and virus_class[j]==3:
			bin1_yes+=1
		elif sdss_class[k]=="QSO   \n" and virus_class[j]==4:
			bin1_und+=1
		else:
			bin1_no+=1
		bin1+=1
	if 2<=sn_qso[i]<=4:
                if sdss_class[k]=="QSO   \n" and virus_class[j]==3:
                        bin2_yes+=1
                elif sdss_class[k]=="QSO   \n" and virus_class[j]==4:
                        bin2_und+=1
                else:
                        bin2_no+=1
                bin2+=1
	if 4<=sn_qso[i]<=6:
                if sdss_class[k]=="QSO   \n" and virus_class[j]==3:
                        bin3_yes+=1
                elif sdss_class[k]=="QSO   \n" and virus_class[j]==4:
                        bin3_und+=1
                else:
                        bin3_no+=1
                bin3+=1
	if 6<=sn_qso[i]<=8:
                if sdss_class[k]=="QSO   \n" and virus_class[j]==3:
                        bin4_yes+=1
                elif sdss_class[k]=="QSO   \n" and virus_class[j]==4:
                        bin4_und+=1
                else:
                        bin4_no+=1
                bin4+=1
	if 8<=sn_qso[i]<=10:
                if sdss_class[k]=="QSO   \n" and virus_class[j]==3:
                        bin5_yes+=1
                elif sdss_class[k]=="QSO   \n" and virus_class[j]==4:
                        bin5_und+=1
                else:
                        bin5_no+=1
                bin5+=1
	if 10<=sn_qso[i]<=12:
                if sdss_class[k]=="QSO   \n" and virus_class[j]==3:
                        bin6_yes+=1
                elif sdss_class[k]=="QSO   \n" and virus_class[j]==4:
                        bin6_und+=1
                else:
                        bin6_no+=1
                bin6+=1
	if 12<=sn_qso[i]<=14:
                if sdss_class[k]=="QSO   \n" and virus_class[j]==3:
                        bin7_yes+=1
                elif sdss_class[k]=="QSO   \n" and virus_class[j]==4:
                        bin7_und+=1
                else:
                        bin7_no+=1
                bin7+=1
	if 14<=sn_qso[i]<=16:
                if sdss_class[k]=="QSO   \n" and virus_class[j]==3:
                        bin8_yes+=1
                elif sdss_class[k]=="QSO   \n" and virus_class[j]==4:
                        bin8_und+=1
                else:
                        bin8_no+=1
                bin8+=1
	if 16<=sn_qso[i]<=18:
                if sdss_class[k]=="QSO   \n" and virus_class[j]==3:
                        bin9_yes+=1
                elif sdss_class[k]=="QSO   \n" and virus_class[j]==4:
                        bin9_und+=1
                else:
                        bin9_no+=1
                bin9+=1
	if 18<=sn_qso[i]<=20:
                if sdss_class[k]=="QSO   \n" and virus_class[j]==3:
                        bin10_yes+=1
                elif sdss_class[k]=="QSO   \n" and virus_class[j]==4:
                        bin10_und+=1
                else:
                        bin10_no+=1
                bin10+=1
	if 20<=sn_qso[i]<=22:
		if sdss_class[k]=="QSO   \n" and virus_class[j]==3:
			bin11_yes+=1
		elif sdss_class[k]=="QSO   \n" and virus_class[j]==4:
			bin11_und+=1
		else:
			bin11_no+=1
		bin11+=1
	if 22<=sn_qso[i]<=24:
                if sdss_class[k]=="QSO   \n" and virus_class[j]==3:
                        bin12_yes+=1
                elif sdss_class[k]=="QSO   \n" and virus_class[j]==4:
                        bin12_und+=1
                else:
                        bin12_no+=1
                bin12+=1
	if 24<=sn_qso[i]<=26:
                if sdss_class[k]=="QSO   \n" and virus_class[j]==3:
                        bin13_yes+=1
                elif sdss_class[k]=="QSO   \n" and virus_class[j]==4:
                        bin13_und+=1
                else:
                        bin13_no+=1
                bin13+=1
	if 26<=sn_qso[i]<=28:
                if sdss_class[k]=="QSO   \n" and virus_class[j]==3:
                        bin14_yes+=1
                elif sdss_class[k]=="QSO   \n" and virus_class[j]==4:
                        bin14_und+=1
                else:
                        bin14_no+=1
                bin14+=1
	if 28<=sn_qso[i]<=30:
                if sdss_class[k]=="QSO   \n" and virus_class[j]==3:
                        bin15_yes+=1
                elif sdss_class[k]=="QSO   \n" and virus_class[j]==4:
                        bin15_und+=1
                else:
                        bin15_no+=1
                bin15+=1
	if 30<=sn_qso[i]<=32:
                if sdss_class[k]=="QSO   \n" and virus_class[j]==3:
                        bin16_yes+=1
                elif sdss_class[k]=="QSO   \n" and virus_class[j]==4:
                        bin16_und+=1
                else:
                        bin16_no+=1
                bin16+=1
	if 32<=sn_qso[i]<=34:
                if sdss_class[k]=="QSO   \n" and virus_class[j]==3:
                        bin17_yes+=1
                elif sdss_class[k]=="QSO   \n" and virus_class[j]==4:
                        bin17_und+=1
                else:
                        bin17_no+=1
                bin17+=1
	if 34<=sn_qso[i]<=36:
                if sdss_class[k]=="QSO   \n" and virus_class[j]==3:
                        bin18_yes+=1
                elif sdss_class[k]=="QSO   \n" and virus_class[j]==4:
                        bin18_und+=1
                else:
                        bin18_no+=1
                bin18+=1
	if 36<=sn_qso[i]<=38:
                if sdss_class[k]=="QSO   \n" and virus_class[j]==3:
                        bin19_yes+=1
                elif sdss_class[k]=="QSO   \n" and virus_class[j]==4:
                        bin19_und+=1
                else:
                        bin19_no+=1
                bin19+=1
	if 38<=sn_qso[i]<=40:
                if sdss_class[k]=="QSO   \n" and virus_class[j]==3:
                        bin20_yes+=1
                elif sdss_class[k]=="QSO   \n" and virus_class[j]==4:
                        bin20_und+=1
                else:
                        bin20_no+=1
                bin20+=1
                
bin1_yes=(bin1_yes/bin1)*100
bin1_no=(bin1_no/bin1)*100
bin1_und=(bin1_und/bin1)*100
bin2_yes=bin2_yes*100/bin2
bin2_no=bin2_no*100/bin2
bin2_und=bin2_und*100/bin2
bin3_yes=bin3_yes*100/bin3
bin3_no=bin3_no*100/bin3
bin3_und=bin3_und*100/bin3
bin4_yes=bin4_yes*100/bin4
bin4_no=bin4_no*100/bin4
bin4_und=bin4_und*100/bin4
bin5_yes=bin5_yes*100/bin5
bin5_no=bin5_no*100/bin5
bin5_und=bin5_und*100/bin5
bin6_yes=bin6_yes*100/bin6
bin6_no=bin6_no*100/bin6
bin6_und=bin6_und*100/bin6
bin7_yes=bin7_yes*100/bin7
bin7_no=bin7_no*100/bin7
bin7_und=bin7_und*100/bin7
bin8_yes=bin8_yes*100/bin8
bin8_no=bin8_no*100/bin8
bin8_und=bin8_und*100/bin8
bin9_yes=bin9_yes*100/bin9
bin9_no=bin9_no*100/bin9
bin9_und=bin9_und*100/bin9
bin10_yes=bin10_yes*100/bin10
bin10_no=bin10_no*100/bin10
bin10_und=bin10_und*100/bin10              
bin11_yes=(bin11_yes/bin11)*100
bin11_no=(bin11_no/bin11)*100
bin11_und=(bin11_und/bin11)*100
bin12_yes=bin12_yes*100/bin12
bin12_no=bin12_no*100/bin12
bin12_und=bin12_und*100/bin12
bin13_yes=bin13_yes*100/bin13
bin13_no=bin13_no*100/bin13
bin13_und=bin13_und*100/bin13
bin14_yes=bin14_yes*100/bin14
bin14_no=bin14_no*100/bin14
bin14_und=bin14_und*100/bin14
bin15_yes=bin15_yes*100/bin15
bin15_no=bin15_no*100/bin15
bin15_und=bin15_und*100/bin15
bin16_yes=bin16_yes*100/bin16
bin16_no=bin16_no*100/bin16
bin16_und=bin16_und*100/bin16
bin17_yes=bin17_yes*100/bin17
bin17_no=bin17_no*100/bin17
bin17_und=bin17_und*100/bin17
bin18_yes=bin18_yes*100/bin18
bin18_no=bin18_no*100/bin18
bin18_und=bin18_und*100/bin18
bin19_yes=bin19_yes*100/bin19
bin19_no=bin19_no*100/bin19
bin19_und=bin19_und*100/bin19
bin20_yes=bin20_yes*100/bin20
bin20_no=bin20_no*100/bin20
bin20_und=bin20_und*100/bin20

x=[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38]
y1=[bin1_yes,bin2_yes,bin3_yes,bin4_yes,bin5_yes,bin6_yes,bin7_yes,bin8_yes,bin9_yes,bin10_yes,bin11_yes,bin12_yes,bin13_yes,bin14_yes,bin15_yes,bin16_yes,bin17_yes,bin18_yes,bin19_yes,bin20_yes]
y2=[bin1_no,bin2_no,bin3_no,bin4_no,bin5_no,bin6_no,bin7_no,bin8_no,bin9_no,bin10_no,bin11_no,bin12_no,bin13_no,bin14_no,bin15_no,bin16_no,bin17_no,bin18_no,bin19_no,bin20_no]
y3=[bin1_und,bin2_und,bin3_und,bin4_und,bin5_und,bin6_und,bin7_und,bin8_und,bin9_und,bin10_und,bin11_und,bin12_und,bin13_und,bin14_und,bin15_und,bin16_und,bin17_und,bin18_und,bin19_und,bin20_und]

fig,ax=plt.subplots();
plt.step(x,y1,label='Correct Class',color='mediumturquoise');
plt.step(x,y3,label='Unknown',color='gold');
plt.step(x,y2,label='Incorrect Class',color='steelblue');
plt.legend();
plt.xlabel('S/N');
plt.ylabel('Fraction of Sources (per bin)');
plt.title('S/N vs Diagnose Class Accuracy');
plt.fill_between(x,y1, step='pre',alpha=0.4,color='mediumturquoise');
plt.fill_between(x,y2, step='pre',alpha=0.4,color='steelblue');
plt.fill_between(x,y3,step='pre',alpha=0.4,color='gold');
plt.grid(color='0.95');
plt.yticks(np.arange(0, 110, 10))
ax.yaxis.set_major_formatter(mtick.PercentFormatter());
plt.show()









