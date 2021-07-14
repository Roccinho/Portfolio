# Nustatyti, kuriame regione namų ūkių turėjo mažiausiai kompiuterių,
# telefonų, namų/butų su kanalizacija,
# pateikti kitimą kas metus.

#Kompiuteriai

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

alytuskomp11=nu11[nu11['AP']==1].groupby('HS090')
alytus_komp11=alytuskomp11.get_group(1)['HB030'].values
kaunaskomp11=nu11[nu11['AP']==2].groupby('HS090')
kaunas_komp11=kaunaskomp11.get_group(1)['HB030'].values
klaipedakomp11=nu11[nu11['AP']==3].groupby('HS090')
klaipeda_komp11=klaipedakomp11.get_group(1)['HB030'].values
marijampolekomp11=nu11[nu11['AP']==4].groupby('HS090')
marijampole_komp11=marijampolekomp11.get_group(1)['HB030'].values
panevezyskomp11=nu11[nu11['AP']==5].groupby('HS090')
panevezys_komp11=panevezyskomp11.get_group(1)['HB030'].values
siauliaikomp11=nu11[nu11['AP']==6].groupby('HS090')
siauliai_komp11=siauliaikomp11.get_group(1)['HB030'].values
tauragekomp11=nu11[nu11['AP']==7].groupby('HS090')
taurage_komp11=tauragekomp11.get_group(1)['HB030'].values
telsiaikomp11=nu11[nu11['AP']==8].groupby('HS090')
telsiai_komp11=telsiaikomp11.get_group(1)['HB030'].values
utenakomp11=nu11[nu11['AP']==9].groupby('HS090')
utena_komp11=utenakomp11.get_group(1)['HB030'].values
vilniuskomp11=nu11[nu11['AP']==10].groupby('HS090')
vilnius_komp11=vilniuskomp11.get_group(1)['HB030'].values

alytuskomp15=nu15[nu15['AP']==1].groupby('HS090')
alytus_komp15=alytuskomp15.get_group(1)['HB030'].values
kaunaskomp15=nu15[nu15['AP']==2].groupby('HS090')
kaunas_komp15=kaunaskomp15.get_group(1)['HB030'].values
klaipedakomp15=nu15[nu15['AP']==3].groupby('HS090')
klaipeda_komp15=klaipedakomp15.get_group(1)['HB030'].values
marijampolekomp15=nu15[nu15['AP']==4].groupby('HS090')
marijampole_komp15=marijampolekomp15.get_group(1)['HB030'].values
panevezyskomp15=nu15[nu15['AP']==5].groupby('HS090')
panevezys_komp15=panevezyskomp15.get_group(1)['HB030'].values
siauliaikomp15=nu15[nu15['AP']==6].groupby('HS090')
siauliai_komp15=siauliaikomp15.get_group(1)['HB030'].values
tauragekomp15=nu15[nu15['AP']==7].groupby('HS090')
taurage_komp15=tauragekomp15.get_group(1)['HB030'].values
telsiaikomp15=nu15[nu15['AP']==8].groupby('HS090')
telsiai_komp15=telsiaikomp15.get_group(1)['HB030'].values
utenakomp15=nu15[nu15['AP']==9].groupby('HS090')
utena_komp15=utenakomp15.get_group(1)['HB030'].values
vilniuskomp15=nu15[nu15['AP']==10].groupby('HS090')
vilnius_komp15=vilniuskomp15.get_group(1)['HB030'].values

alytuskomp19=nu19[nu19['AP']==1].groupby('HS090')
alytus_komp19=alytuskomp19.get_group(1)['HB030'].values
kaunaskomp19=nu19[nu19['AP']==2].groupby('HS090')
kaunas_komp19=kaunaskomp19.get_group(1)['HB030'].values
klaipedakomp19=nu19[nu19['AP']==3].groupby('HS090')
klaipeda_komp19=klaipedakomp19.get_group(1)['HB030'].values
marijampolekomp19=nu19[nu19['AP']==4].groupby('HS090')
marijampole_komp19=marijampolekomp19.get_group(1)['HB030'].values
panevezyskomp19=nu19[nu19['AP']==5].groupby('HS090')
panevezys_komp19=panevezyskomp19.get_group(1)['HB030'].values
siauliaikomp19=nu19[nu19['AP']==6].groupby('HS090')
siauliai_komp19=siauliaikomp19.get_group(1)['HB030'].values
tauragekomp19=nu19[nu19['AP']==7].groupby('HS090')
taurage_komp19=tauragekomp19.get_group(1)['HB030'].values
telsiaikomp19=nu19[nu19['AP']==8].groupby('HS090')
telsiai_komp19=telsiaikomp19.get_group(1)['HB030'].values
utenakomp19=nu19[nu19['AP']==9].groupby('HS090')
utena_komp19=utenakomp19.get_group(1)['HB030'].values
vilniuskomp19=nu19[nu19['AP']==10].groupby('HS090')
vilnius_komp19=vilniuskomp19.get_group(1)['HB030'].values

nukomp11=[len(alytus_komp11), len(kaunas_komp11), len(klaipeda_komp11), len(marijampole_komp11),
len(panevezys_komp11), len(siauliai_komp11), len(taurage_komp11), len(telsiai_komp11), len(utena_komp11),
len(vilnius_komp11)]

nukomp15=[len(alytus_komp15), len(kaunas_komp15), len(klaipeda_komp15), len(marijampole_komp15),
len(panevezys_komp15), len(siauliai_komp15), len(taurage_komp15), len(telsiai_komp15), len(utena_komp15),
len(vilnius_komp15)]

nukomp19=[len(alytus_komp19), len(kaunas_komp19), len(klaipeda_komp19), len(marijampole_komp19),
len(panevezys_komp19), len(siauliai_komp19), len(taurage_komp19), len(telsiai_komp19), len(utena_komp19),
len(vilnius_komp19)]

#telefonai

alytustel11=nu11[nu11['AP']==1].groupby('HS070')
alytus_tel11=alytustel11.get_group(1)['HB030'].values
kaunastel11=nu11[nu11['AP']==2].groupby('HS070')
kaunas_tel11=kaunastel11.get_group(1)['HB030'].values
klaipedatel11=nu11[nu11['AP']==3].groupby('HS070')
klaipeda_tel11=klaipedatel11.get_group(1)['HB030'].values
marijampoletel11=nu11[nu11['AP']==4].groupby('HS070')
marijampole_tel11=marijampoletel11.get_group(1)['HB030'].values
panevezystel11=nu11[nu11['AP']==5].groupby('HS070')
panevezys_tel11=panevezystel11.get_group(1)['HB030'].values
siauliaitel11=nu11[nu11['AP']==6].groupby('HS070')
siauliai_tel11=siauliaitel11.get_group(1)['HB030'].values
tauragetel11=nu11[nu11['AP']==7].groupby('HS070')
taurage_tel11=tauragetel11.get_group(1)['HB030'].values
telsiaitel11=nu11[nu11['AP']==8].groupby('HS070')
telsiai_tel11=telsiaitel11.get_group(1)['HB030'].values
utenatel11=nu11[nu11['AP']==9].groupby('HS070')
utena_tel11=utenatel11.get_group(1)['HB030'].values
vilniustel11=nu11[nu11['AP']==10].groupby('HS070')
vilnius_tel11=vilniustel11.get_group(1)['HB030'].values

alytustel15=nu15[nu15['AP']==1].groupby('HS070')
alytus_tel15=alytustel15.get_group(1)['HB030'].values
kaunastel15=nu15[nu15['AP']==2].groupby('HS070')
kaunas_tel15=kaunastel15.get_group(1)['HB030'].values
klaipedatel15=nu15[nu15['AP']==3].groupby('HS070')
klaipeda_tel15=klaipedatel15.get_group(1)['HB030'].values
marijampoletel15=nu15[nu15['AP']==4].groupby('HS070')
marijampole_tel15=marijampoletel15.get_group(1)['HB030'].values
panevezystel15=nu15[nu15['AP']==5].groupby('HS070')
panevezys_tel15=panevezystel15.get_group(1)['HB030'].values
siauliaitel15=nu15[nu15['AP']==6].groupby('HS070')
siauliai_tel15=siauliaitel15.get_group(1)['HB030'].values
tauragetel15=nu15[nu15['AP']==7].groupby('HS070')
taurage_tel15=tauragetel15.get_group(1)['HB030'].values
telsiaitel15=nu15[nu15['AP']==8].groupby('HS070')
telsiai_tel15=telsiaitel15.get_group(1)['HB030'].values
utenatel15=nu15[nu15['AP']==9].groupby('HS070')
utena_tel15=utenatel15.get_group(1)['HB030'].values
vilniustel15=nu15[nu15['AP']==10].groupby('HS070')
vilnius_tel15=vilniustel15.get_group(1)['HB030'].values

nutel11=[len(alytus_tel11), len(kaunas_tel11), len(klaipeda_tel11), len(marijampole_tel11),
len(panevezys_tel11), len(siauliai_tel11), len(taurage_tel11), len(telsiai_tel11), len(utena_tel11),
len(vilnius_tel11)]

nutel15=[len(alytus_tel15), len(kaunas_tel15), len(klaipeda_tel15), len(marijampole_tel15),
len(panevezys_tel15), len(siauliai_tel15), len(taurage_tel15), len(telsiai_tel15), len(utena_tel15),
len(vilnius_tel15)]

#kanalizacijos

alytuskanal11=nu11[nu11['AP']==1].groupby('HH091')
alytus_kanal11=alytuskanal11.get_group(1)['HB030'].values
kaunaskanal11=nu11[nu11['AP']==2].groupby('HH091')
kaunas_kanal11=kaunaskanal11.get_group(1)['HB030'].values
klaipedakanal11=nu11[nu11['AP']==3].groupby('HH091')
klaipeda_kanal11=klaipedakanal11.get_group(1)['HB030'].values
marijampolekanal11=nu11[nu11['AP']==4].groupby('HH091')
marijampole_kanal11=marijampolekanal11.get_group(1)['HB030'].values
panevezyskanal11=nu11[nu11['AP']==5].groupby('HH091')
panevezys_kanal11=panevezyskanal11.get_group(1)['HB030'].values
siauliaikanal11=nu11[nu11['AP']==6].groupby('HH091')
siauliai_kanal11=siauliaikanal11.get_group(1)['HB030'].values
tauragekanal11=nu11[nu11['AP']==7].groupby('HH091')
taurage_kanal11=tauragekanal11.get_group(1)['HB030'].values
telsiaikanal11=nu11[nu11['AP']==8].groupby('HH091')
telsiai_kanal11=telsiaikanal11.get_group(1)['HB030'].values
utenakanal11=nu11[nu11['AP']==9].groupby('HH091')
utena_kanal11=utenakanal11.get_group(1)['HB030'].values
vilniuskanal11=nu11[nu11['AP']==10].groupby('HH091')
vilnius_kanal11=vilniuskanal11.get_group(1)['HB030'].values

alytuskanal15=nu15[nu15['AP']==1].groupby('HH091')
alytus_kanal15=alytuskanal15.get_group(1)['HB030'].values
kaunaskanal15=nu15[nu15['AP']==2].groupby('HH091')
kaunas_kanal15=kaunaskanal15.get_group(1)['HB030'].values
klaipedakanal15=nu15[nu15['AP']==3].groupby('HH091')
klaipeda_kanal15=klaipedakanal15.get_group(1)['HB030'].values
marijampolekanal15=nu15[nu15['AP']==4].groupby('HH091')
marijampole_kanal15=marijampolekanal15.get_group(1)['HB030'].values
panevezyskanal15=nu15[nu15['AP']==5].groupby('HH091')
panevezys_kanal15=panevezyskanal15.get_group(1)['HB030'].values
siauliaikanal15=nu15[nu15['AP']==6].groupby('HH091')
siauliai_kanal15=siauliaikanal15.get_group(1)['HB030'].values
tauragekanal15=nu15[nu15['AP']==7].groupby('HH091')
taurage_kanal15=tauragekanal15.get_group(1)['HB030'].values
telsiaikanal15=nu15[nu15['AP']==8].groupby('HH091')
telsiai_kanal15=telsiaikanal15.get_group(1)['HB030'].values
utenakanal15=nu15[nu15['AP']==9].groupby('HH091')
utena_kanal15=utenakanal15.get_group(1)['HB030'].values
vilniuskanal15=nu15[nu15['AP']==10].groupby('HH091')
vilnius_kanal15=vilniuskanal15.get_group(1)['HB030'].values

alytuskanal19=nu19[nu19['AP']==1].groupby('HH091')
alytus_kanal19=alytuskanal19.get_group(1)['HB030'].values
kaunaskanal19=nu19[nu19['AP']==2].groupby('HH091')
kaunas_kanal19=kaunaskanal19.get_group(1)['HB030'].values
klaipedakanal19=nu19[nu19['AP']==3].groupby('HH091')
klaipeda_kanal19=klaipedakanal19.get_group(1)['HB030'].values
marijampolekanal19=nu19[nu19['AP']==4].groupby('HH091')
marijampole_kanal19=marijampolekanal19.get_group(1)['HB030'].values
panevezyskanal19=nu19[nu19['AP']==5].groupby('HH091')
panevezys_kanal19=panevezyskanal19.get_group(1)['HB030'].values
siauliaikanal19=nu19[nu19['AP']==6].groupby('HH091')
siauliai_kanal19=siauliaikanal19.get_group(1)['HB030'].values
tauragekanal19=nu19[nu19['AP']==7].groupby('HH091')
taurage_kanal19=tauragekanal19.get_group(1)['HB030'].values
telsiaikanal19=nu19[nu19['AP']==8].groupby('HH091')
telsiai_kanal19=telsiaikanal19.get_group(1)['HB030'].values
utenakanal19=nu19[nu19['AP']==9].groupby('HH091')
utena_kanal19=utenakanal19.get_group(1)['HB030'].values
vilniuskanal19=nu19[nu19['AP']==10].groupby('HH091')
vilnius_kanal19=vilniuskanal19.get_group(1)['HB030'].values

nukanal11=[len(alytus_kanal11), len(kaunas_kanal11), len(klaipeda_komp11), len(marijampole_kanal11),
len(panevezys_kanal11), len(siauliai_kanal11), len(taurage_kanal11), len(telsiai_kanal11),
len(utena_kanal11), len(vilnius_kanal11)]

nukanal15=[len(alytus_kanal15), len(kaunas_kanal15), len(klaipeda_komp15), len(marijampole_kanal15),
len(panevezys_kanal15), len(siauliai_kanal15), len(taurage_kanal15), len(telsiai_kanal15),
len(utena_kanal15), len(vilnius_kanal15)]

nukanal19=[len(alytus_kanal19), len(kaunas_kanal19), len(klaipeda_komp19), len(marijampole_kanal19),
len(panevezys_kanal19), len(siauliai_kanal19), len(taurage_kanal19), len(telsiai_kanal19),
len(utena_kanal19), len(vilnius_kanal19)]

fig1, ax=plt.subplots()
miestai=['Alytus', 'Kaunas', 'Klaipėda', 'Marijampolė', 'Panevėžys', 'Šiauliai', 'Tauragė', 
'Telšiai', 'Utena', 'Vilnius']

x=np.arange(1,len(miestai)+1,1)

kompsk11=ax.bar(x-0.25, nukomp11, width=0.25, color='silver')
kompsk15=ax.bar(x, nukomp15, width=0.25, color='dimgray')
kompsk19=ax.bar(x+0.25, nukomp19, width=0.25, color='black')

ax.set_title('''2011-2019 namų ūkių, turėjusių kompiuterį, skaičius''')
ax.set_xticks(x)
ax.set_xticklabels(miestai, rotation=75, fontsize=12)
ax.set_xlabel('Regionai', fontsize=14, fontstyle='italic')
ax.legend(['2011', '2015', '2019'])

ax.bar_label(kompsk11, padding=1)
ax.bar_label(kompsk15, padding=1)
ax.bar_label(kompsk19, padding=1)
fig1.tight_layout()

fig2, ax=plt.subplots()

ax.set_title('''2011-2015 namų ūkių, turėjusių telefoną, skaičius*''')
textstr='''*2019 metais duomenys
dėl telefono nerinkti'''
plt.figtext(0.87, 0.05, textstr)
ax.set_xticks(x)
ax.set_xticklabels(miestai, rotation=75, fontsize=12)
ax.set_xlabel('Regionai', fontsize=14, fontstyle='italic')
ax.legend(['2011', '2015'])

telsk11=ax.bar(x-0.25, nukomp11, width=0.25, color='mediumpurple')
telsk15=ax.bar(x, nukomp15, width=0.25, color='indigo')

ax.bar_label(telsk11, padding=1)
ax.bar_label(telsk15, padding=1)

fig3, ax=plt.subplots()

kanalsk11=ax.bar(x-0.25, nukanal11, width=0.25, color='khaki')
kanalsk15=ax.bar(x, nukanal15, width=0.25, color='darkkhaki')
kanalsk19=ax.bar(x+0.25, nukanal19, width=0.25, color='goldenrod')

ax.set_title('''2011-2019 namų ūkių, turėjusių kanalizaciją, skaičius''')
ax.set_xticks(x)
ax.set_xticklabels(miestai, rotation=75, fontsize=12)
ax.set_xlabel('Regionai', fontsize=14, fontstyle='italic')
ax.legend(['2011', '2015', '2019'])

ax.bar_label(kanalsk11, padding=1)
ax.bar_label(kanalsk15, padding=1)
ax.bar_label(kanalsk19, padding=1)
fig3.tight_layout()

plt.show()


