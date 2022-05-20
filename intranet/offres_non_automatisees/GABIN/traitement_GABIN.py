import csv
import glob
import re
import time
from unidecode import unidecode
# coding: utf-8


for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_GABIN.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar=';', quotechar='')
            for row in reader:
                if row[0]=='':
                    continue
                else :
                    # Nom du chateau
                    if row[0]=='Bordeaux':
                        chateau=unidecode(row[3])
                    else:
                        chateau=unidecode(row[3])+' '+unidecode(row[4])
                    chateau = chateau.replace(';',' ')
                    # chateau=re.sub(r'[0-9]','',chateau) ??

                    # année
                    if row[2]=='':
                        annee='NV'
                    else:
                        annee=row[2]


                    # Format de la bouteille
                    if row[6]=='0,375':
                        formatb='DE'
                    elif row[6]=='0,75' or '0,7':
                        formatb='BO'
                    elif row[6]=='0,70':
                        formatb='BO'
                    elif row[6]=='1,5':
                        formatb='MG'
                    elif row[6]=='5 l' or '5':
                        formatb='JE'
                    elif row[6]=='3 L' or '3':
                        formatb='DM'
                    elif row[6]=='6 l':
                        formatb='IM'
                    else:
                        formatb=row[6]

                    # Prix
                    fPrix=repr(row[8])
                    fPrix=fPrix.replace("'","")
                    fPrix=fPrix.replace("\\","")
                    fPrix=fPrix.replace("u202f","")
                    prix=unidecode(fPrix)
                    prix=prix.replace(" EUR","")
                    prix=prix.replace(".",",")

                    # quantite
                    quantite=row[5]


                    #conditionnement
                    conditionnement=row[7].upper()
                    conditionnement=conditionnement.replace('OWC','CBO')
                    conditionnement=conditionnement.replace('CO','CC')
                    conditionnement=conditionnement.replace('DEMI BT','UNITE')
                    conditionnement=conditionnement.replace('BT','UNITE')
                    conditionnement=conditionnement.replace('MAG','UNITE')
                    conditionnement=conditionnement.replace('BAG IN BOX','UNITE')
                    if 'CBO' or 'CC' in conditionnement :
                        conditionnement = conditionnement
                    else:
                        conditionnement = 'UNITE'


                    #commentaires
                    if row[7]=='Bag in box':
                        commentaire=row[7]+' - '+row[11]
                    else:
                        commentaire=row[11]


                    trou=''
                    chateau = chateau.strip()
                    chateau = chateau.replace(',','')
                    commentaire = commentaire.strip()
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,trou,trou,trou]
                    writer.writerow(newRow)
            monFichierEntre.close()
