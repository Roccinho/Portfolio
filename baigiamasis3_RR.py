# Nustatyti, kiek asmenų, turinčių aukštąjį išsilavinimą,
# gyveno butuose, namuose, kaime/mieste, kuriame
# regione, kaip šis kiekis kito?

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

asm11=pd.read_csv('2011 asmenys.csv')
nu11=pd.read_csv('2011 namu ukiai.csv')
asm15=pd.read_csv('2015 asmenys.csv')
nu15=pd.read_csv('2015 namu ukiai.csv')
asm19=pd.read_csv('2019 asmenys.csv')
nu19=pd.read_csv('2019 namu ukiai.csv')

bendras_2011=pd.merge (asm11, nu11, on='HB030')
bendras_2015=pd.merge (asm15, nu15, on='HB030')
bendras_2019=pd.merge (asm19, nu19, on='HB030')

#kaimas name 2011

#miestai=['Alytus', 'Kaunas', 'Klaipėda', 'Marijampolė', 'Panevėžys', 'Šiauliai', 'Tauragė', 
#Telšiai', 'Utena', 'Vilnius']

namaik11=bendras_2011[bendras_2011['PE040']==5].groupby(['HH010', 'M_K_y'])
namai_kaime11=len(namaik11.get_group((1,2))['PB030'].values)
butaik11=bendras_2011[bendras_2011['PE040']==5].groupby(['HH010', 'M_K_y'])
butai_kaime11=len(butaik11.get_group((4,2))['PB030'].values)
namaim11=bendras_2011[bendras_2011['PE040']==5].groupby(['HH010', 'M_K_y'])
namai_mieste11=len(namaim11.get_group((1,1))['PB030'].values)
butaim11=bendras_2011[bendras_2011['PE040']==5].groupby(['HH010', 'M_K_y'])
butai_mieste11=len(butaim11.get_group((4,1))['PB030'].values)

#2015 bakalauras

namaik15=bendras_2015[bendras_2015['PE040']==600].groupby(['HH010', 'M_K_y'])
namai_kaime15=namaik15.get_group((1,2))['PB030'].values
butaik15=bendras_2015[bendras_2015['PE040']==600].groupby(['HH010', 'M_K_y'])
butai_kaime15=butaik15.get_group((4,2))['PB030'].values
namaim15=bendras_2015[bendras_2015['PE040']==600].groupby(['HH010', 'M_K_y'])
namai_mieste15=namaim15.get_group((1,1))['PB030'].values
butaim15=bendras_2015[bendras_2015['PE040']==600].groupby(['HH010', 'M_K_y'])
butai_mieste15=butaim15.get_group((4,1))['PB030'].values

#2015 magistras

namaik15m=bendras_2015[bendras_2015['PE040']==700].groupby(['HH010', 'M_K_y'])
namai_kaime15mag=namaik15m.get_group((1,2))['PB030'].values
butaik15m=bendras_2015[bendras_2015['PE040']==700].groupby(['HH010', 'M_K_y'])
butai_kaime15mag=butaik15m.get_group((4,2))['PB030'].values
namaim15m=bendras_2015[bendras_2015['PE040']==700].groupby(['HH010', 'M_K_y'])
namai_mieste15mag=namaim15m.get_group((1,1))['PB030'].values
butaim15m=bendras_2015[bendras_2015['PE040']==700].groupby(['HH010', 'M_K_y'])
butai_mieste15mag=butaim15m.get_group((4,1))['PB030'].values

#2015 bendras

nam_kaim_aukst15=np.append(namai_kaime15,namai_kaime15mag)
but_kaim_aukst15=np.append(butai_kaime15, butai_kaime15mag)
nam_miest_aukst15=np.append(namai_mieste15, namai_mieste15mag)
but_miest_aukst15=np.append(butai_mieste15, butai_mieste15mag)

#2019

namaik19=bendras_2019[bendras_2019['PE040']==600].groupby(['HH010', 'M_K_y'])
namai_kaime19=namaik19.get_group((1,2))['PB030'].values
butaik19=bendras_2019[bendras_2019['PE040']==600].groupby(['HH010', 'M_K_y'])
butai_kaime19=butaik19.get_group((4,2))['PB030'].values
namaim19=bendras_2019[bendras_2019['PE040']==600].groupby(['HH010', 'M_K_y'])
namai_mieste19=namaim19.get_group((1,1))['PB030'].values
butaim19=bendras_2019[bendras_2019['PE040']==600].groupby(['HH010', 'M_K_y'])
butai_mieste19=butaim19.get_group((4,1))['PB030'].values

#2019magistras

namaik19m=bendras_2019[bendras_2019['PE040']==700].groupby(['HH010', 'M_K_y'])
namai_kaime19_mag=namaik19m.get_group((1,2))['PB030'].values
butaik19m=bendras_2019[bendras_2019['PE040']==700].groupby(['HH010', 'M_K_y'])
butai_kaime19_mag=butaik19m.get_group((4,2))['PB030'].values
namaim19m=bendras_2019[bendras_2019['PE040']==700].groupby(['HH010', 'M_K_y'])
namai_mieste19_mag=namaim19m.get_group((1,1))['PB030'].values
butaim19m=bendras_2019[bendras_2019['PE040']==700].groupby(['HH010', 'M_K_y'])
butai_mieste19_mag=butaim19m.get_group((4,1))['PB030'].values

#2019 bendras

nam_kaim_aukst19=np.append(namai_kaime19, namai_kaime19_mag)
but_kaim_aukst19=np.append(butai_kaime19, butai_kaime19_mag)
nam_miest_aukst19=np.append(namai_mieste19, namai_mieste19_mag)
but_miest_aukst19=np.append(butai_mieste19, butai_mieste19_mag)


fig, ax=plt.subplots()

kategorijos=['Namai kaime', 'Butai kaime', 'Namai mieste', 'Butai mieste']

duom11=[namai_kaime11, butai_kaime11, namai_mieste11, butai_mieste11]
duom15=[len(nam_kaim_aukst15), len(but_kaim_aukst15), len(nam_miest_aukst15), len(but_miest_aukst15)]
duom19=[len(nam_kaim_aukst19), len(but_kaim_aukst19), len(nam_miest_aukst19), len(but_miest_aukst19)]

x=np.arange(1,len(kategorijos)+1,1)

duomenys11=ax.bar(x-0.25, duom11, width=0.25, color='maroon')
duomenys15=ax.bar(x, duom15, width=0.25, color='sienna')
duomenys19=ax.bar(x+0.25, duom19, width=0.25, color='burlywood')

ax.set_xticks(x)
ax.set_xticklabels(kategorijos, fontsize=12)

ax.set_title('''Žmonių su aukštuoju skaičius pagal būsto tipą ir gyvenvietę''')
ax.legend(['2011', '2015', '2019'])

ax.bar_label(duomenys11, fontsize=11)
ax.bar_label(duomenys15, fontsize=11)
ax.bar_label(duomenys19, fontsize=11)


fig.tight_layout()
plt.show()


# k_alytus_n11=bendras_2011[bendras_2011['AP_y']==1].groupby(['PE040', 'HH010', 'M_K_y',])
# kaimas_alytus_n11=k_alytus_n11.get_group((5,1,2))['PB030'].values
# k_kaunas_n11=bendras_2011[bendras_2011['AP_y']==2].groupby(['PE040', 'HH010', 'M_K_y',])
# kaimas_kaunas_n11=k_kaunas_n11.get_group((5,1,2))['PB030'].values
# k_klaipeda_n11=bendras_2011[bendras_2011['AP_y']==3].groupby(['PE040', 'HH010', 'M_K_y',])
# kaimas_klaipeda_n11=k_klaipeda_n11.get_group((5,1,2))['PB030'].values
# k_marijampole_n11=bendras_2011[bendras_2011['AP_y']==4].groupby(['PE040', 'HH010', 'M_K_y',])
# kaimas_marijampole_n11=k_marijampole_n11.get_group((5,1,2))['PB030'].values
# k_panevezys_n11=bendras_2011[bendras_2011['AP_y']==5].groupby(['PE040', 'HH010', 'M_K_y',])
# kaimas_panevezys_n11=k_panevezys_n11.get_group((5,1,2))['PB030'].values
# k_siauliai_n11=bendras_2011[bendras_2011['AP_y']==6].groupby(['PE040', 'HH010', 'M_K_y',])
# kaimas_siauliai_n11=k_siauliai_n11.get_group((5,1,2))['PB030'].values
# k_taurage_n11=bendras_2011[bendras_2011['AP_y']==7].groupby(['PE040', 'HH010', 'M_K_y',])
# kaimas_taurage_n11=k_taurage_n11.get_group((5,1,2))['PB030'].values
# k_telsiai_n11=bendras_2011[bendras_2011['AP_y']==8].groupby(['PE040', 'HH010', 'M_K_y',])
# kaimas_telsiai_n11=k_telsiai_n11.get_group((5,1,2))['PB030'].values
# k_utena_n11=bendras_2011[bendras_2011['AP_y']==9].groupby(['PE040', 'HH010', 'M_K_y',])
# kaimas_utena_n11=k_utena_n11.get_group((5,1,2))['PB030'].values
# k_vilnius_n11=bendras_2011[bendras_2011['AP_y']==10].groupby(['PE040', 'HH010', 'M_K_y',])
# kaimas_vilnius_n11=k_vilnius_n11.get_group((5,1,2))['PB030'].values

# # kaimas bute 2011

# k_alytus_b11=bendras_2011[bendras_2011['AP_y']==1].groupby(['PE040', 'HH010', 'M_K_y',])
# kaimas_alytus_b11=k_alytus_b11.get_group((5,4,2))['PB030'].values
# k_kaunas_b11=bendras_2011[bendras_2011['AP_y']==2].groupby(['PE040', 'HH010', 'M_K_y',])
# kaimas_kaunas_b11=k_kaunas_b11.get_group((5,4,2))['PB030'].values
# k_klaipeda_b11=bendras_2011[bendras_2011['AP_y']==3].groupby(['PE040', 'HH010', 'M_K_y',])
# kaimas_klaipeda_b11=k_klaipeda_b11.get_group((5,4,2))['PB030'].values
# k_marijampole_b11=bendras_2011[bendras_2011['AP_y']==4].groupby(['PE040', 'HH010', 'M_K_y',])
# kaimas_marijampole_b11=k_marijampole_b11.get_group((5,4,2))['PB030'].values
# k_panevezys_b11=bendras_2011[bendras_2011['AP_y']==5].groupby(['PE040', 'HH010', 'M_K_y',])
# kaimas_panevezys_b11=k_panevezys_b11.get_group((5,4,2))['PB030'].values
# k_siauliai_b11=bendras_2011[bendras_2011['AP_y']==6].groupby(['PE040', 'HH010', 'M_K_y',])
# kaimas_siauliai_b11=k_siauliai_b11.get_group((5,4,2))['PB030'].values
# k_taurage_b11=bendras_2011[bendras_2011['AP_y']==7].groupby(['PE040', 'HH010', 'M_K_y',])
# kaimas_taurage_b11=k_taurage_b11.get_group((5,4,2))['PB030'].values
# k_telsiai_b11=bendras_2011[bendras_2011['AP_y']==8].groupby(['PE040', 'HH010', 'M_K_y',])
# kaimas_telsiai_b11=k_telsiai_b11.get_group((5,4,2))['PB030'].values
# k_utena_b11=bendras_2011[bendras_2011['AP_y']==9].groupby(['PE040', 'HH010', 'M_K_y',])
# kaimas_utena_b11=k_utena_b11.get_group((5,4,2))['PB030'].values
# k_vilnius_b11=bendras_2011[bendras_2011['AP_y']==10].groupby(['PE040', 'HH010', 'M_K_y',])
# kaimas_vilnius_b11=k_vilnius_b11.get_group((5,4,2))['PB030'].values

# #miestas name 

# m_alytus_n11=bendras_2011[bendras_2011['AP_y']==1].groupby(['PE040', 'HH010', 'M_K_y',])
# miestas_alytus_n11=m_alytus_n11.get_group((5,1,1))['PB030'].values
# m_kaunas_n11=bendras_2011[bendras_2011['AP_y']==2].groupby(['PE040', 'HH010', 'M_K_y',])
# miestas_kaunas_n11=m_kaunas_n11.get_group((5,1,1))['PB030'].values
# m_klaipeda_n11=bendras_2011[bendras_2011['AP_y']==3].groupby(['PE040', 'HH010', 'M_K_y',])
# miestas_klaipeda_n11=m_klaipeda_n11.get_group((5,1,1))['PB030'].values
# m_marijampole_n11=bendras_2011[bendras_2011['AP_y']==4].groupby(['PE040', 'HH010', 'M_K_y',])
# miestas_marijampole_n11=m_marijampole_n11.get_group((5,1,1))['PB030'].values
# m_panevezys_n11=bendras_2011[bendras_2011['AP_y']==5].groupby(['PE040', 'HH010', 'M_K_y',])
# miestas_panevezys_n11=m_panevezys_n11.get_group((5,1,1))['PB030'].values
# m_siauliai_n11=bendras_2011[bendras_2011['AP_y']==6].groupby(['PE040', 'HH010', 'M_K_y',])
# miestas_siauliai_n11=m_siauliai_n11.get_group((5,1,1))['PB030'].values
# m_taurage_n11=bendras_2011[bendras_2011['AP_y']==7].groupby(['PE040', 'HH010', 'M_K_y',])
# miestas_taurage_n11=m_taurage_n11.get_group((5,1,1))['PB030'].values
# m_telsiai_n11=bendras_2011[bendras_2011['AP_y']==8].groupby(['PE040', 'HH010', 'M_K_y',])
# miestas_telsiai_n11=m_telsiai_n11.get_group((5,1,1))['PB030'].values
# m_utena_n11=bendras_2011[bendras_2011['AP_y']==9].groupby(['PE040', 'HH010', 'M_K_y',])
# miestas_utena_n11=m_utena_n11.get_group((5,1,1))['PB030'].values
# m_vilnius_n11=bendras_2011[bendras_2011['AP_y']==10].groupby(['PE040', 'HH010', 'M_K_y',])
# miestas_vilnius_n11=m_vilnius_n11.get_group((5,1,1))['PB030'].values


# #meistas bute 2011

# m_alytus_b11=bendras_2011[bendras_2011['AP_y']==1].groupby(['PE040', 'HH010', 'M_K_y',])
# miestas_alytus_b11=m_alytus_b11.get_group((5,4,1))['PB030'].values
# m_kaunas_b11=bendras_2011[bendras_2011['AP_y']==2].groupby(['PE040', 'HH010', 'M_K_y',])
# miestas_kaunas_b11=m_kaunas_b11.get_group((5,4,1))['PB030'].values
# m_klaipeda_b11=bendras_2011[bendras_2011['AP_y']==3].groupby(['PE040', 'HH010', 'M_K_y',])
# miestas_klaipeda_b11=m_klaipeda_b11.get_group((5,4,1))['PB030'].values
# m_marijampole_b11=bendras_2011[bendras_2011['AP_y']==4].groupby(['PE040', 'HH010', 'M_K_y',])
# miestas_marijampole_b11=m_marijampole_b11.get_group((5,4,1))['PB030'].values
# m_panevezys_b11=bendras_2011[bendras_2011['AP_y']==5].groupby(['PE040', 'HH010', 'M_K_y',])
# miestas_panevezys_b11=m_panevezys_b11.get_group((5,4,1))['PB030'].values
# m_siauliai_b11=bendras_2011[bendras_2011['AP_y']==6].groupby(['PE040', 'HH010', 'M_K_y',])
# miestas_siauliai_b11=m_siauliai_b11.get_group((5,4,1))['PB030'].values
# m_taurage_b11=bendras_2011[bendras_2011['AP_y']==7].groupby(['PE040', 'HH010', 'M_K_y',])
# miestas_taurage_b11=m_taurage_b11.get_group((5,4,1))['PB030'].values
# m_telsiai_b11=bendras_2011[bendras_2011['AP_y']==8].groupby(['PE040', 'HH010', 'M_K_y',])
# miestas_telsiai_b11=m_telsiai_b11.get_group((5,4,1))['PB030'].values
# m_utena_b11=bendras_2011[bendras_2011['AP_y']==9].groupby(['PE040', 'HH010', 'M_K_y',])
# miestas_utena_b11=m_utena_b11.get_group((5,4,1))['PB030'].values
# m_vilnius_b11=bendras_2011[bendras_2011['AP_y']==10].groupby(['PE040', 'HH010', 'M_K_y',])
# miestas_vilnius_b11=m_vilnius_b11.get_group((5,4,1))['PB030'].values
