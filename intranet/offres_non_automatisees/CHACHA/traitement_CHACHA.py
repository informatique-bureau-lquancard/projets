# -*- coding: utf-8 -*-
import csv
import glob
import re
import time
from unidecode import unidecode
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_CHACHA.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                bEcrire=0
                if row[4]=='':
                    bEcrire=0
                elif row[4]=='Prix € H.T Blle':
                    bEcrire=0
                else:
                    bEcrire=1
                    # Nom du chateau
                    chateau=unidecode(row[0])
                    # année, on garde seulement la date
                    annee=row[1]
                    # Format de la bouteille
                    formatb='BO'
                    # Prix
                    fPrix=repr(row[4])
                    fPrix=fPrix.replace("'","")
                    fPrix=fPrix.replace("\\","")
                    fPrix=fPrix.replace("u202f","")
                    prix=unidecode(fPrix)
                    prix=prix.replace(' EUR','')
                    # quantite
                    quantite=row[3]
                    # conditionnement
                    conditionnement=row[2]
                    conditionnement=conditionnement.replace('CB','CBO')
                    # Commentaire
                    commentaire=''
                    # On fabrique la nouvelle ligne dans l'ordre voulu
                if bEcrire==1:
                    trou=''
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,trou,trou,trou]
                    writer.writerow(newRow)
            monFichierEntre.close()
