# Nustatyti, kuriame regione (AP) buvo daugiausiai
# asmenų su aukštuoju išsilavinimu (PE040), gyenanančių butuose (HH010), turinčių
# kompiuterį (HS090), televizorių(HS080), galinčių keliauti bent kartą per metus (HS040).

# Pateikti šių dydžių kitimą kas metus.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

asm11=pd.read_csv('2011 asmenys.csv')
nu11=pd.read_csv('2011 namu ukiai.csv')
asm15=pd.read_csv('2015 asmenys.csv')
nu15=pd.read_csv('2015 namu ukiai.csv')
asm19=pd.read_csv('2019 asmenys.csv')
nu19=pd.read_csv('2019 namu ukiai.csv')

bendras_2011=pd.merge(asm11, nu11, on='HB030')
bendras_2015=pd.merge (asm15, nu15, on='HB030')
bendras_2019=pd.merge (asm19, nu19, on='HB030')

#aukštesnys ar aukštasis iš daugiabučių su 10+butų
asm_alytus=bendras_2011[bendras_2011['AP_y']==1].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
alytiškiai=asm_alytus.get_group((5,4,1,1,1))['PB030'].values
asm_kaunas=bendras_2011[bendras_2011['AP_y']==2].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
kaunieciai=asm_kaunas.get_group((5,4,1,1,1))['PB030'].values
asm_klaipeda=bendras_2011[bendras_2011['AP_y']==3].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
klaipedieciai=asm_klaipeda.get_group((5,4,1,1,1))['PB030'].values
asm_marijampole=bendras_2011[bendras_2011['AP_y']==4].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
marijampolieciai=asm_marijampole.get_group((5,4,1,1,1))['PB030'].values
asm_panevezys=bendras_2011[bendras_2011['AP_y']==5].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
panevezieciai=asm_panevezys.get_group((5,4,1,1,1))['PB030'].values
asm_siauliai=bendras_2011[bendras_2011['AP_y']==6].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
siaulieciai=asm_siauliai.get_group((5,4,1,1,1))['PB030'].values
asm_taurage=bendras_2011[bendras_2011['AP_y']==7].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
tauragiskiai=asm_taurage.get_group((5,4,1,1,1))['PB030'].values
asm_telsiai=bendras_2011[bendras_2011['AP_y']==8].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
telsiskiai=asm_telsiai.get_group((5,4,1,1,1))['PB030'].values
asm_utena=bendras_2011[bendras_2011['AP_y']==9].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
uteniskiai=asm_utena.get_group((5,4,1,1,1))['PB030'].values
asm_vilnius=bendras_2011[bendras_2011['AP_y']==10].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
vilnieciai=asm_vilnius.get_group((5,4,1,1,1))['PB030'].values

#2015 bakalauras 

asm_alytus15=bendras_2015[bendras_2015['AP_y']==1].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
alytiškiai15=asm_alytus15.get_group((600,4,1,1,1))['PB030'].values
asm_kaunas15=bendras_2015[bendras_2015['AP_y']==2].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
kaunieciai15=asm_kaunas15.get_group((600,4,1,1,1))['PB030'].values
asm_klaipeda15=bendras_2015[bendras_2015['AP_y']==3].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
klaipedieciai15=asm_klaipeda15.get_group((600,4,1,1,1))['PB030'].values
asm_marijampole15=bendras_2015[bendras_2015['AP_y']==4].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
marijampolieciai15=asm_marijampole15.get_group((600,4,1,1,1))['PB030'].values
asm_panevezys15=bendras_2015[bendras_2015['AP_y']==5].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
panevezieciai15=asm_panevezys15.get_group((600,4,1,1,1))['PB030'].values
asm_siauliai15=bendras_2015[bendras_2015['AP_y']==6].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
siaulieciai15=asm_siauliai15.get_group((600,4,1,1,1))['PB030'].values
asm_taurage15=bendras_2015[bendras_2015['AP_y']==7].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
tauragiskiai15=asm_taurage15.get_group((600,4,1,1,1))['PB030'].values
asm_telsiai15=bendras_2015[bendras_2015['AP_y']==8].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
telsiskiai15=asm_telsiai15.get_group((600,4,1,1,1))['PB030'].values
asm_utena15=bendras_2015[bendras_2015['AP_y']==9].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
uteniskiai15=asm_utena15.get_group((600,4,1,1,1))['PB030'].values
asm_vilnius15=bendras_2015[bendras_2015['AP_y']==10].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
vilnieciai15=asm_vilnius15.get_group((600,4,1,1,1))['PB030'].values

#2015 magistras

asm_alytus15_mag=bendras_2015[bendras_2015['AP_y']==1].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
alytiškiai15_mag=asm_alytus15_mag.get_group((700,4,1,1,1))['PB030'].values
asm_kaunas15_mag=bendras_2015[bendras_2015['AP_y']==2].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
kaunieciai15_mag=asm_kaunas15_mag.get_group((700,4,1,1,1))['PB030'].values
asm_klaipeda15_mag=bendras_2015[bendras_2015['AP_y']==3].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
klaipedieciai15_mag=asm_klaipeda15_mag.get_group((700,4,1,1,1))['PB030'].values
asm_marijampole15_mag=bendras_2015[bendras_2015['AP_y']==4].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
marijampolieciai15_mag=asm_marijampole15_mag.get_group((700,4,1,1,1))['PB030'].values
asm_panevezys15_mag=bendras_2015[bendras_2015['AP_y']==5].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
panevezieciai15_mag=asm_panevezys15_mag.get_group((700,4,1,1,1))['PB030'].values
asm_siauliai15_mag=bendras_2015[bendras_2015['AP_y']==6].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
siaulieciai15_mag=asm_siauliai15_mag.get_group((700,4,1,1,1))['PB030'].values
asm_taurage15_mag=bendras_2015[bendras_2015['AP_y']==7].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
tauragiskiai15_mag=asm_taurage15_mag.get_group((700,4,1,1,1))['PB030'].values
asm_telsiai15_mag=bendras_2015[bendras_2015['AP_y']==8].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
telsiskiai15_mag=asm_telsiai15_mag.get_group((700,4,1,1,1))['PB030'].values
asm_utena15_mag=bendras_2015[bendras_2015['AP_y']==9].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
uteniskiai15_mag=asm_utena15_mag.get_group((700,4,1,1,1))['PB030'].values
asm_vilnius15_mag=bendras_2015[bendras_2015['AP_y']==10].groupby(['PE040', 'HH010', 'HS090', 'HS080', 'HS040'])
vilnieciai15_mag=asm_vilnius15_mag.get_group((700,4,1,1,1))['PB030'].values

#2015 bendri

alytus15=np.append(alytiškiai15, alytiškiai15_mag)
kaunas15=np.append(kaunieciai15, kaunieciai15_mag)
klaipeda15=np.append(klaipedieciai15, klaipedieciai15_mag)
marijampole15=np.append(marijampolieciai15, marijampolieciai15_mag)
panevezys15=np.append(panevezieciai15, panevezieciai15_mag)
siauliai15=np.append(siaulieciai15, siaulieciai15_mag)
taurage15=np.append(tauragiskiai15, tauragiskiai15_mag)
telsiai15=np.append(telsiskiai15, telsiskiai15_mag)
utena15=np.append(uteniskiai15, uteniskiai15_mag)
vilnius15=np.append(vilnieciai15, vilnieciai15_mag)

#2019 bakalauras butuose virš 10 (nebuvo skaičiuojami televizoriai)

asm_alytus19=bendras_2019[bendras_2019['AP_y']==1].groupby(['PE040', 'HH010', 'HS090', 'HS040'])
alytiškiai19=asm_alytus19.get_group((600,4,1,1))['PB030'].values
asm_kaunas19=bendras_2019[bendras_2019['AP_y']==2].groupby(['PE040', 'HH010', 'HS090', 'HS040'])
kaunieciai19=asm_kaunas19.get_group((600,4,1,1))['PB030'].values
asm_klaipeda19=bendras_2019[bendras_2019['AP_y']==3].groupby(['PE040', 'HH010', 'HS090', 'HS040'])
klaipedieciai19=asm_klaipeda19.get_group((600,4,1,1))['PB030'].values
asm_marijampole19=bendras_2019[bendras_2019['AP_y']==4].groupby(['PE040', 'HH010', 'HS090', 'HS040'])
marijampolieciai19=asm_marijampole19.get_group((600,4,1,1))['PB030'].values
asm_panevezys19=bendras_2019[bendras_2019['AP_y']==5].groupby(['PE040', 'HH010', 'HS090', 'HS040'])
panevezieciai19=asm_panevezys19.get_group((600,4,1,1))['PB030'].values
asm_siauliai19=bendras_2019[bendras_2019['AP_y']==6].groupby(['PE040', 'HH010', 'HS090', 'HS040'])
siaulieciai19=asm_siauliai19.get_group((600,4,1,1))['PB030'].values
asm_taurage19=bendras_2019[bendras_2019['AP_y']==7].groupby(['PE040', 'HH010', 'HS090', 'HS040'])
tauragiskiai19=asm_taurage19.get_group((600,4,1,1))['PB030'].values
asm_telsiai19=bendras_2019[bendras_2019['AP_y']==8].groupby(['PE040', 'HH010', 'HS090', 'HS040'])
telsiskiai19=asm_telsiai19.get_group((600,4,1,1))['PB030'].values
asm_utena19=bendras_2019[bendras_2019['AP_y']==9].groupby(['PE040', 'HH010', 'HS090', 'HS040'])
uteniskiai19=asm_utena19.get_group((600,4,1,1))['PB030'].values
asm_vilnius19=bendras_2019[bendras_2019['AP_y']==10].groupby(['PE040', 'HH010', 'HS090', 'HS040'])
vilnieciai19=asm_vilnius19.get_group((600,4,1,1))['PB030'].values

#2019 magistras

asm_alytus19_mag=bendras_2019[bendras_2019['AP_y']==1].groupby(['PE040', 'HH010', 'HS090', 'HS040'])
alytiškiai19_mag=asm_alytus19_mag.get_group((700,4,1,1))['PB030'].values
asm_kaunas19_mag=bendras_2019[bendras_2019['AP_y']==2].groupby(['PE040', 'HH010', 'HS090', 'HS040'])
kaunieciai19_mag=asm_kaunas19_mag.get_group((700,4,1,1))['PB030'].values
asm_klaipeda19_mag=bendras_2019[bendras_2019['AP_y']==3].groupby(['PE040', 'HH010', 'HS090', 'HS040'])
klaipedieciai19_mag=asm_klaipeda19_mag.get_group((700,4,1,1))['PB030'].values
asm_marijampole19_mag=bendras_2019[bendras_2019['AP_y']==4].groupby(['PE040', 'HH010', 'HS090', 'HS040'])
marijampolieciai19_mag=asm_marijampole19_mag.get_group((700,4,1,1))['PB030'].values
asm_panevezys19_mag=bendras_2019[bendras_2019['AP_y']==5].groupby(['PE040', 'HH010', 'HS090', 'HS040'])
panevezieciai19_mag=asm_panevezys19_mag.get_group((700,4,1,1))['PB030'].values
asm_siauliai19_mag=bendras_2019[bendras_2019['AP_y']==6].groupby(['PE040', 'HH010', 'HS090', 'HS040'])
siaulieciai19_mag=asm_siauliai19_mag.get_group((700,4,1,1))['PB030'].values
asm_taurage19_mag=bendras_2019[bendras_2019['AP_y']==7].groupby(['PE040', 'HH010', 'HS090', 'HS040'])
tauragiskiai19_mag=asm_taurage19_mag.get_group((700,4,1,1))['PB030'].values
asm_telsiai19_mag=bendras_2019[bendras_2019['AP_y']==8].groupby(['PE040', 'HH010', 'HS090', 'HS040'])
telsiskiai19_mag=asm_telsiai19_mag.get_group((700,4,1,1))['PB030'].values
asm_utena19_mag=bendras_2019[bendras_2019['AP_y']==9].groupby(['PE040', 'HH010', 'HS090', 'HS040'])
uteniskiai19_mag=asm_utena19_mag.get_group((700,4,1,1))['PB030'].values
asm_vilnius19_mag=bendras_2019[bendras_2019['AP_y']==10].groupby(['PE040', 'HH010', 'HS090', 'HS040'])
vilnieciai19_mag=asm_vilnius19_mag.get_group((700,4,1,1))['PB030'].values

#2019 bendri

alytus19=np.append(alytiškiai19, alytiškiai19_mag)
kaunas19=np.append(kaunieciai19, kaunieciai19_mag)
klaipeda19=np.append(klaipedieciai19, klaipedieciai19_mag)
marijampole19=np.append(marijampolieciai19, marijampolieciai19_mag)
panevezys19=np.append(panevezieciai19, panevezieciai19_mag)
siauliai19=np.append(siaulieciai19, siaulieciai19_mag)
taurage19=np.append(tauragiskiai19, tauragiskiai19_mag)
telsiai19=np.append(telsiskiai19, telsiskiai19_mag)
utena19=np.append(uteniskiai19, uteniskiai19_mag)
vilnius19=np.append(vilnieciai19, vilnieciai19_mag)


fig, ax=plt.subplots()
miestai=['Alytus', 'Kaunas', 'Klaipėda', 'Marijampolė', 'Panevėžys', 'Šiauliai', 'Tauragė', 
'Telšiai', 'Utena', 'Vilnius']
asmenys11=[len(alytiškiai), len(kaunieciai), len(klaipedieciai), len(marijampolieciai),
len(panevezieciai), len(siaulieciai), len(tauragiskiai), len(telsiskiai), len(uteniskiai),
len(vilnieciai)]

asmenys15=[len(alytus15), len(kaunas15), len(klaipeda15), len(marijampole15), len(panevezys15),
len(siauliai15), len(taurage15), len(telsiai15), len(utena15), len(vilnius15)]

asmenys19=[len(alytus19), len(kaunas19), len(klaipeda19), len(marijampole19), len(panevezys19),
len(siauliai19), len(taurage19), len(telsiai19), len(utena19), len(vilnius19)]

x=np.arange(1,len(miestai)+1,1)

asmenusk11=ax.bar(x-0.25, asmenys11, width=0.25, color='purple')
asmenusk15=ax.bar(x, asmenys15, width=0.25, color='orange')
asmenusk19=ax.bar(x+0.25, asmenys19, width=0.25, color='green')

ax.set_title('''2011-2019 asmenys su aukštuoju išsilavinimu, gyenanantys butuose, 
turintys kompiuterį, televizorių, galintys keliauti bent kartą per metus''')
ax.set_xticks(x)
ax.set_xticklabels(miestai, rotation=75, fontsize=14)
ax.set_xlabel('Regionai', fontsize=14, fontstyle='italic')
ax.legend(['2011', '2015', '2019'])

textstr='''*2019 metais duomenys
dėl televizoriaus nerinkti'''
plt.figtext(0.87, 0.05, textstr)

ax.bar_label(asmenusk11, padding=1)
ax.bar_label(asmenusk15, padding=1)
ax.bar_label(asmenusk19, padding=1)


fig.tight_layout()
plt.show()
